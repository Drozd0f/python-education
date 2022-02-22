"""This module launches the application"""
from curses import wrapper

from src.menu import menu
from src.stat import init_stat


def main():
    """This function launches the application"""
    init_stat()
    wrapper(menu)


if __name__ == '__main__':
    main()
