"""This module displays the game menu"""
import sys
import curses
import time

from config import WindowResolution
from src.game import hangman
from src.stat import stat
from src.template import paint_button


def draw_button(stdscr, selected_button_idx: int):
    """The function draw the menu buttons"""
    window = WindowResolution(*stdscr.getmaxyx())
    buttons = 'Start', 'Last words', 'Exit'
    for idx, button in enumerate(buttons):
        coord_x = int(window.width / 2 - len(button) / 2)
        coord_y = int(window.height / 2 - len(buttons) / 2 + idx)
        if idx == selected_button_idx:
            paint_button(stdscr, coord_y, coord_x, button)
        else:
            stdscr.addstr(coord_y, coord_x, button)


def menu(stdscr):
    """This function executes main loop the menu."""
    curses.use_default_colors()
    stdscr.nodelay(True)
    curses.curs_set(0)
    current_but = 0
    draw_button(stdscr, current_but)
    while True:
        key = stdscr.getch()
        stdscr.clear()
        if key == curses.KEY_UP:
            current_but -= 1
            current_but = max(current_but, 0)
        elif key == curses.KEY_DOWN:
            current_but += 1
            current_but = min(current_but, 2)
        elif key == curses.KEY_ENTER or key in (10, 13):
            if current_but == 0:
                hangman(stdscr)
            elif current_but == 1:
                stat()
            elif current_but == 2:
                sys.exit()

        draw_button(stdscr, current_but)
        stdscr.refresh()
        time.sleep(0.1)
