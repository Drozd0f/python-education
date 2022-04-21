"""This module contains state for tic-tac-toe"""
from enum import Enum


class ButtonState(Enum):
    """This class describes button state"""
    ABSTRACT_BUTTON = -1
    PLAY = 0
    SHOW_WINNERS = 1
    CLEAR_WINNERS_STATS = 2
    EXIT = 3
