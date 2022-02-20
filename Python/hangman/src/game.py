"""This module performs the display and execution of the game logic"""
import curses
import sys
from dataclasses import dataclass
import time
import typing as t
import logging

import requests

from config import TEMPLATE_DIR, WindowResolution
from src.stat import save_stat


ESC_CODE = 27
log = logging.getLogger(__name__)


@dataclass
class Game:
    """Class for tracking game information."""
    word: str
    answer: str
    guess: str = ''
    misses: str = ''
    stage: int = 1
    status: bool = False


def get_word() -> str:
    """The function is executed by querying a random word by api.
    Returns the received word."""
    response = requests.get('https://random-word-api.herokuapp.com/word')
    json_response = response.json()
    return json_response[0].upper()


def get_hangman(stage: int) -> t.Optional[list]:
    """The function performs get hangman depending on stage.
    Returns list hangman template.
    """

    try:
        with open(TEMPLATE_DIR / f'man/{stage}_stage.txt', 'r', encoding='utf-8') as file:
            return file.read().split('\n')
    except FileNotFoundError:
        log.error(f'Hangman template {stage}_stage.txt not found')
        sys.exit(1)


def encrypt_word(word: str) -> str:
    """The function hides the letters of the word with the symbol '_'.
    Returns the encrypted word.
    """
    result = ''
    for idx in range(len(word)):
        if idx != len(word) - 1:
            result += '_ '
        else:
            result += '_'
    return result


def check_letter(letter: chr, word: str, answer: str) -> str:
    """This function performs a check to see if a letter exists in a word
    and substitution of the letter in the word by index.
    Returns the word as a string.
    """
    word = word.split()
    for idx, char in enumerate(answer):
        if letter == char:
            word[idx] = letter
    return ' '.join(word)


def draw_interface(stdscr, game: Game, key: int):
    """This function draws the game interface depending on the key pressed."""
    my_window = WindowResolution(*stdscr.getmaxyx())
    if key != -1:
        game.guess = chr(key).upper()
        game.word = check_letter(game.guess, game.word, game.answer)
        if game.guess not in game.word:
            game.misses += f'{game.guess}, '
            game.stage += 1
    interface = (
        f'Word: {game.word}',
        f'Guess: {game.guess}',
        f'Misses: {game.misses}'
    )
    for idx, line in enumerate(interface):
        coord_x = int(my_window.width / 2 - len(line) / 2)
        coord_y = int(my_window.height / 2 - len(interface) / 2 + idx + 6)
        stdscr.addstr(coord_y, coord_x, line)


def draw_hangman(stdscr, stage: int = 1):
    """This function draws the executioner depending on the stage of the game."""
    my_window = WindowResolution(*stdscr.getmaxyx())
    hangman_template = get_hangman(stage)
    for idx, line in enumerate(hangman_template):
        coord_x = int(my_window.width / 2 - len(line) / 2)
        coord_y = int(my_window.height / 2 - len(hangman_template) / 2 + idx)
        stdscr.addstr(coord_y, coord_x, line)


def create_game_result(stdscr, status: bool):
    """This function performs the display of the inscription at the end of the game."""
    if status:
        text = 'You won, congratulations, press ESC to return to the menu'
    else:
        text = 'You lost, press ESC to return to the menu'
    window = WindowResolution(*stdscr.getmaxyx())
    coord_x = int(window.width / 2 - len(text) / 2)
    coord_y = int(window.height / 2)
    stdscr.addstr(coord_y, coord_x, text)


def is_win(word: str, answer: str) -> bool:
    """This function checks the status of the game."""
    return word.replace(' ', '') == answer


def hangman(stdscr):
    """This function executes main loop the game."""
    curses.use_default_colors()
    stdscr.nodelay(True)
    word = get_word()
    game = Game(word=encrypt_word(word), answer=word)
    draw_hangman(stdscr, game.stage)
    while True:
        stdscr.clear()
        key = stdscr.getch()
        if key == ESC_CODE:
            save_stat(game.answer, game.status)
            break
        if game.stage != 7 and game.status is False:
            game.status = is_win(game.word, game.answer)
            draw_hangman(stdscr, game.stage)
            draw_interface(stdscr, game, key)
            if game.status:
                create_game_result(stdscr, game.status)
        else:
            create_game_result(stdscr, game.status)
        stdscr.refresh()
        time.sleep(0.1)
