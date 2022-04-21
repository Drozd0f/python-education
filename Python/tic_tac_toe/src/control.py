"""This module contains controller for communication view and logic tic-tac-toe"""
import logging
import random


from src.state import ButtonState
from src.base_view import View
from src.models.game import Game
from src.models.player import PlayerList
from src.models.board import Board


class Controller:
    """This class describes communication view and logic"""
    def __init__(self, view: View):
        self._view = view
        self._game = Game()
        self._board = Board()
        self._player_list = PlayerList()

    def menu(self):
        """This method describes processing button presses in the menu"""
        button_state = self._view.draw_menu()
        if button_state is ButtonState.PLAY:
            self.play()
        # TODO: check button for solo player  # pylint: disable=W0511 (fixme)
        else:
            self.menu()

    def _restart(self, double: bool):
        self._game.restart()
        self._board.restart()
        self._player_list.restart()
        self.play(double, restart=True)

    def _game_loop(self):
        board = self._board.board
        while self._game.is_pending:
            self._player_list.change_move()
            pos = self._view.draw_gui(self._game.is_pending, board, self._player_list)
            player_idx = self._game.player_input(
                board, pos, self._player_list.move
            )
            if player_idx is not None:
                self._player_list.move = player_idx
                self._game.check_win(board, self._player_list.cur_player.mark)

    def play(self, double: bool = True, restart: bool = False):
        """This method describes game communication view and logic"""
        if not restart:
            self._player_list = self._view.login(double, PlayerList())
        self._player_list.move = random.choice(range(len(self._player_list)))
        self._game_loop()
        is_draw = self._game.is_draw
        self._player_list.change_streak(is_draw)
        if is_draw:
            logging.info('Draw')
        else:
            logging.info(
                f'Winner {self._player_list.get_winner_name()}, '
                f'Streak: {self._player_list.cur_player.streak}'
            )
        restart = self._view.draw_restart(is_draw, self._player_list.cur_player)
        if restart:
            self._restart(double)
        self.menu()
