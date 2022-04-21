"""This module contains exercise Python - practice tic-tac-toe"""
from curses import wrapper

from src.control import Controller
from src.views_terminal.view import TerminalView
from config import config_logger


def tic_tac_toe(screen):
    """This function returns Controller object"""
    return Controller(view=TerminalView(screen)).menu()


def main():
    """This function launches the application"""
    config_logger()
    wrapper(tic_tac_toe)


if __name__ == '__main__':
    main()
