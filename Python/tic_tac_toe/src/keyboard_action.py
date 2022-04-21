"""This module contains processing frequently used keys for terminal version tic-tac-toe"""
import curses


def is_enter_press(key: int) -> bool:
    """This function returns status enter"""
    return key == curses.KEY_ENTER or key in (10, 13)


def is_q_press(key: int) -> bool:
    """This function returns status Q button"""
    return key in (81, 113)


def is_up_or_down_press(key: int) -> bool:
    """This function returns status KEY_UP or KEY_DOWN"""
    return key in (curses.KEY_UP, curses.KEY_DOWN)
