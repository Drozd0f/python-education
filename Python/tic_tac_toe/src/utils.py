"""This module contains utils for tic-tac-toe"""
import re
import typing as t


def refactor_name(name: str) -> str:
    """This function returns name without * char"""
    return re.sub(r'\s?[*]\s?', '', name)


def get_mark_list() -> t.List[str]:
    """This function returns list game mark"""
    return ['X', 'O']
