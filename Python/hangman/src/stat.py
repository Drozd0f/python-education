"""This module does work with statistics"""
import os
import sys
import subprocess
import platform
import csv
import logging
from datetime import datetime
import typing as t

from config import BASE_DIR


log = logging.getLogger(__name__)


def is_stat_not_exists() -> bool:
    """This function checks if there was no entry in the statistics file"""
    try:
        with open(BASE_DIR / 'game_stat/stat.csv', newline='', encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile)
            return reader.fieldnames != ['Date', 'Word', 'Result']
    except FileNotFoundError:
        return create_stat_file()


def create_stat_file() -> t.Optional[bool]:
    """This function creates an empty statistics file with csv extension"""
    try:
        with open(BASE_DIR / 'game_stat/stat.csv', 'tw', encoding='utf-8'):
            pass
    except OSError:
        log.error('Failed creating the stat file')
        sys.exit(1)
    else:
        return True


def init_stat():
    """This function performs the creation of columns on the first run of the application"""
    if is_stat_not_exists():
        fieldnames = ['Date', 'Word', 'Result']
        with open(BASE_DIR / 'game_stat/stat.csv', 'a', newline='', encoding="utf8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()


def update_stat(date: str, word: str, result: str):
    """This function adds a line to stat.csv with the values date, word, result"""
    with open(BASE_DIR / 'game_stat/stat.csv', 'a', newline='', encoding="utf8") as csvfile:
        fieldnames = ['Date', 'Word', 'Result']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({
            'Date': date,
            'Word': word,
            'Result': result
        })


def save_stat(word: str, result: bool):
    """This function saves statistics."""
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result = 'Win' if result else 'Lose'
    update_stat(date, word, result)


def stat():
    """This function launches a file with statistics."""
    filepath = BASE_DIR / "game_stat/stat.csv"
    if platform.system() == 'Darwin':  # macOS
        subprocess.call(('open', filepath))
    elif platform.system() == 'Windows':  # Windows
        os.startfile(filepath)
    else:  # linux variants
        subprocess.call(('xdg-open', filepath))
