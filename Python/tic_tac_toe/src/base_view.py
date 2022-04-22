"""This module contains base view for tic-tac-toe"""
from abc import ABC, abstractmethod

from src.models.player import PlayerList, Player


class View(ABC):
    """This abstract class describes base functional view for tic-tac-toe"""
    @abstractmethod
    def draw_menu(self):
        """This abstract method responsible for displaying the menu"""
        raise NotImplementedError

    @abstractmethod
    def login(self, double: bool, player_list: PlayerList) -> PlayerList:
        """This abstract method responsible for change player list"""
        raise NotImplementedError

    @abstractmethod
    def draw_gui(self, is_game_pending: bool, board: list, player_list: PlayerList) -> list:
        """This abstract method responsible for draw game interface"""
        raise NotImplementedError

    @abstractmethod
    def draw_restart(self, is_draw: bool, player: Player):
        """This abstract method responsible for draw restart menu"""
        raise NotImplementedError
