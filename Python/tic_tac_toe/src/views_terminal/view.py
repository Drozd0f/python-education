"""This module contains view for terminal version tic-tac-toe"""
import time
import curses
import typing as t

from config import WindowResolution
from src.base_view import View
from src.state import ButtonState
from src.utils import get_mark_list, refactor_name
from src.keyboard_action import is_enter_press, is_q_press, is_up_or_down_press
from src.views_terminal.button import ButtonList
from src.models.player import PlayerList, Player


class TerminalView(View):
    """This class describes extend base functional view for terminal version tic-tac-toe"""
    _current_but = 0
    _mark = get_mark_list()
    _current_pos = [0, 0]
    _pattern_horizontal_line = '-------------'
    _pattern_vertical_line = '  |  '

    def __init__(self, screen):
        self._screen = screen
        self._button_list = ButtonList()

    def _draw_button(self):
        for button in self._button_list:
            button.draw(self._screen, self._current_but)

    def _change_pos_menu(self, key: int):
        if key == curses.KEY_UP:
            self._current_but = max(self._current_but - 1, 0)
        elif key == curses.KEY_DOWN:
            self._current_but = min(self._current_but + 1, len(self._button_list) - 1)

    def draw_menu(self) -> ButtonState:
        curses.use_default_colors()
        self._screen.nodelay(True)
        curses.curs_set(0)
        self._draw_button()
        while True:
            key = self._screen.getch()
            self._screen.clear()
            if is_up_or_down_press(key):
                self._change_pos_menu(key)
            elif is_enter_press(key):
                return self._button_list[self._current_but].enter()
            self._draw_button()
            self._screen.refresh()
            time.sleep(0.1)

    def _draw_login_interface(self, name: str):
        wind = WindowResolution(*self._screen.getmaxyx())
        text = 'Enter your name (max len 10) and press Enter'
        coord_y = int(wind.height / 2)
        coord_x_text = int(wind.width / 2 - len(text) / 2)
        coord_x_name = int(wind.width / 2 - len(name) / 2)
        self._screen.addstr(coord_y - 1, coord_x_text, text)
        self._screen.addstr(coord_y + 1, coord_x_name, name)

    def login(self, double: bool, player_list: PlayerList) -> PlayerList:
        name = ''
        player_number = 0
        while True:
            key = self._screen.getch()
            self._screen.clear()
            self._draw_login_interface(name)
            if is_enter_press(key):
                player_list.save(
                    player_number,
                    name,
                    self._mark[player_number]
                )
                player_number += 1
                name = ''
                # TODO: variant with bot  # pylint: disable=W0511 (fixme)
                if double and player_number == 2:
                    return player_list
            elif key != -1:
                name += chr(key).upper()
            self._screen.refresh()
            time.sleep(0.1)

    def _change_pos_gui(self, key: int):
        if key == curses.KEY_RIGHT:
            self._current_pos[0] = min(self._current_pos[0] + 1, 2)
        elif key == curses.KEY_LEFT:
            self._current_pos[0] = max(self._current_pos[0] - 1, 0)
        elif key == curses.KEY_UP:
            self._current_pos[1] = max(self._current_pos[1] - 1, 0)
        elif key == curses.KEY_DOWN:
            self._current_pos[1] = min(self._current_pos[1] + 1, 2)

    def _draw_player(self, player, right: bool = False):
        wind = WindowResolution(*self._screen.getmaxyx())
        coord_y = int(wind.height * 0.1)
        if right:
            coord_x = int(wind.width * 0.9)
            self._screen.addstr(coord_y, int(coord_x - len(player.name) / 2), player.name)
            self._screen.addstr(coord_y + 1, coord_x, player.mark)
            if player.streak > 1:
                text = f'Current streak = {player.streak}'
                self._screen.addstr(coord_y + 2, int(coord_x - len(text) / 2), text)
        else:
            coord_x = int(wind.width * 0.1)
            self._screen.addstr(coord_y, coord_x, player.name)
            self._screen.addstr(coord_y + 1, coord_x, player.mark)
            if player.streak > 1:
                text = f'Current streak = {player.streak}'
                self._screen.addstr(coord_y + 2, coord_x, text)

    def _draw_opponent(self, player_list: PlayerList):
        self._draw_player(player_list[0])
        self._draw_player(player_list[1], right=True)

    def _draw_horizontal_line(self, coord_y: int, coord_x: int):
        self._screen.addstr(coord_y, coord_x, self._pattern_horizontal_line)

    def _draw_vertical_line(self, coord_y: int, coord_x: int):
        self._screen.addstr(coord_y, coord_x, self._pattern_vertical_line)

    def _paint(self, coord_y: int, coord_x: int, mark):
        """This method paints the position on field in the specified color pair"""
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        self._screen.attron(curses.color_pair(1))
        self._screen.addstr(coord_y, coord_x, mark)
        self._screen.attroff(curses.color_pair(1))

    def _draw_board(self, board: list):
        wind = WindowResolution(*self._screen.getmaxyx())
        coord_y = int(wind.height / 2 - 3)
        coord_x = int(wind.width / 2 - len(self._pattern_horizontal_line) / 2)
        for y in range(3):  # pylint: disable=C0103 (invalid-name)
            pos_y = coord_y + y * 2
            for x in range(3):  # pylint: disable=C0103 (invalid-name)
                pos_x = coord_x + x * len(self._pattern_vertical_line)
                if [x, y] == self._current_pos:
                    if x != 2:
                        self._paint(pos_y, pos_x, board[x][y])
                        self._draw_vertical_line(pos_y, pos_x + 1)
                    else:
                        self._paint(pos_y, pos_x, board[x][y])
                elif x != 2:
                    self._screen.addstr(pos_y, pos_x, board[x][y])
                    self._draw_vertical_line(pos_y, pos_x + 1)
                else:
                    self._screen.addstr(pos_y, pos_x, board[x][y])
            if y != 2:
                self._draw_horizontal_line(pos_y + 1, coord_x - 1)

    def draw_gui(self, is_game_pending: bool, board: list, player_list: PlayerList) -> list:
        if not isinstance(player_list, PlayerList):
            raise TypeError
        curses.use_default_colors()
        self._screen.nodelay(True)
        while True:
            key = self._screen.getch()
            self._screen.clear()
            self._change_pos_gui(key)
            if is_enter_press(key):
                return self._current_pos
            self._draw_opponent(player_list)
            self._draw_board(board)
            self._screen.refresh()
            time.sleep(0.1)

    def _draw_winner(self, wind: WindowResolution, player: Player):
        name = refactor_name(player.name)
        coord_y = int((wind.height - 1) / 2)
        coord_x = int(wind.width / 2 - len(name) / 2)
        self._screen.addstr(coord_y, coord_x, name)

    def _draw_restart_menu(self, is_draw: bool, player: t.Optional[Player] = None):
        wind = WindowResolution(*self._screen.getmaxyx())
        if not is_draw:
            self._draw_winner(wind, player)
        else:
            text = 'Draw'
            coord_y = int((wind.height - 1) / 2)
            coord_x = int(wind.width / 2 - len(text) / 2)
            self._screen.addstr(coord_y, coord_x, text)
        text = 'Press Enter if you want to play another game or double click Q to exit in menu'
        coord_y = int((wind.height + 1) / 2)
        coord_x = int(wind.width / 2 - len(text) / 2)
        self._screen.addstr(coord_y, coord_x, text)

    def draw_restart(self, is_draw: bool, player: t.Optional[Player] = None) -> bool:
        curses.use_default_colors()
        self._screen.nodelay(True)
        while True:
            key = self._screen.getch()
            self._draw_restart_menu(is_draw, player)
            if is_enter_press(key):
                return True
            if is_q_press(key):
                return False
