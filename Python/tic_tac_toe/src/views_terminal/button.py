"""This module contains button view for terminal version tic-tac-toe"""
import sys
import subprocess
import typing as t
from abc import ABC, abstractmethod
import curses

from src.state import ButtonState
from config import WindowResolution, LOG_DIR


class ButtonNotFound(Exception):
    """This class describes instance error for button class"""

    def __init__(self, string: t.Optional[str] = None):
        self._string = string
        super().__init__()

    def __str__(self):
        if self._string is None:
            return 'This value not button'
        return f'This value \'{self._string}\' not button'


class Button(ABC):
    """This abstract class describes base functional button"""
    button = ButtonState.ABSTRACT_BUTTON
    text = ''

    def _paint(self, screen, coord_y: int, coord_x: int):
        """This method paints the button in the specified color pair"""
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        screen.attron(curses.color_pair(1))
        screen.addstr(coord_y, coord_x, self.text)
        screen.attroff(curses.color_pair(1))

    def draw(self, screen, selected_button_idx: int):
        """The method draw button"""
        wind = WindowResolution(*screen.getmaxyx())
        coord_x = int(wind.width / 2 - len(self.text) / 2)
        coord_y = int(wind.height / 2 - 4 / 2 + self.button.value)
        if self.button.value == selected_button_idx:
            self._paint(screen, coord_y, coord_x)
        else:
            screen.addstr(coord_y, coord_x, self.text)

    @abstractmethod
    def enter(self) -> ButtonState:
        """This abstract method describes the behavior of a button when clicked.
        Returns the state of that button
        """
        raise NotImplementedError


class Play(Button):
    """This class describes play button"""
    button = ButtonState.PLAY
    text = 'PLAY'

    def enter(self) -> ButtonState:
        return ButtonState.PLAY


class ShowLogWinners(Button):
    """This class describes show log winners button"""
    button = ButtonState.SHOW_WINNERS
    text = 'SHOW WINNERS'

    def enter(self) -> ButtonState:
        subprocess.call(('xdg-open', LOG_DIR / 'app.log'))
        return self.button


class ClearLogWinners(Button):
    """This class describes clear log winners button"""
    button = ButtonState.CLEAR_WINNERS_STATS
    text = 'CLEAR WINNERS STATS'

    def enter(self) -> ButtonState:
        with open(LOG_DIR / 'app.log', 'w', encoding="utf-8"):
            pass
        return self.button


class Exit(Button):
    """This class describes exit button"""
    button = ButtonState.EXIT
    text = 'EXIT'

    def enter(self):
        sys.exit()


class ButtonList:
    """This class stores buttons list and describes"""
    _buttons = [
        Play(),
        ShowLogWinners(),
        ClearLogWinners(),
        Exit()
    ]

    class _ButtonIter:
        def __init__(self, buttons):
            self._buttons = buttons

        def _gen_button(self):
            return next(self._buttons)

        def __iter__(self):
            return self

        def __next__(self):
            return self._gen_button()

    def __init__(self, *args):
        for button in args:
            if not isinstance(button, Button):
                raise ButtonNotFound(button)
            self._buttons.extend(button.text)

    def __getitem__(self, idx: int):
        if isinstance(idx, int):
            return self._buttons[idx]
        raise IndexError

    def __len__(self):
        return len(self._buttons)

    def __iter__(self):
        return self._ButtonIter(self._gen_buttons())

    def _gen_buttons(self):
        return (button for button in self._buttons)

    @property
    def buttons(self) -> list:
        """This property return buttons list"""
        return self._buttons
