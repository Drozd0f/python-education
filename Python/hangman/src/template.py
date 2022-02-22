"""This module stores template functions"""
import curses


def paint_button(stdscr, *args):
    """This function paints the button in the specified color pair."""
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    stdscr.attron(curses.color_pair(1))
    coord_y, coord_x, button = args
    stdscr.addstr(coord_y, coord_x, button)
    stdscr.attroff(curses.color_pair(1))
