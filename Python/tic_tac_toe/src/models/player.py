"""This module contains player model tic-tac-toe"""
import typing as t
from dataclasses import dataclass

from src.utils import refactor_name


@dataclass
class Player:
    """This data class stores information and describes behaviors player"""
    name = 'Player {}'
    mark: str
    streak: int = 0
    left_pos: bool = True
    is_move: bool = False

    def change_move(self):
        """This method describes rename according to the move status"""
        if self.is_move:
            if self.left_pos:
                self.name = f'{self.name} *'
            else:
                self.name = f'* {self.name}'
        else:
            self.name = refactor_name(self.name)

    def drop_streak(self):
        """This method drop the streak"""
        self.streak = 0

    def drop_info(self):
        """This method drop player info"""
        self.name = refactor_name(self.name)
        self.is_move = False


class PlayerList:
    """This class stores players list and describes
    the work with the players
    """
    _players: t.List[Player] = []
    _cur_player: Player
    _last_player: t.Optional[Player] = None
    _last_winner: t.Optional[Player] = None
    _move = 0

    def __len__(self) -> int:
        return len(self._players)

    def __getitem__(self, idx) -> Player:
        if idx in range(0, 2):
            return self._players[idx]
        raise IndexError

    def save(self, player_number: int, name: str, mark: str):
        """This method describes append player object to the players list"""
        self._players.append(Player(mark=mark))
        if player_number % 2 != 0:
            self._players[player_number].left_pos = False
        if name != '' and len(name) < 10:
            self._players[player_number].name = name
        else:
            self._players[player_number].name = self._players[player_number].name.format(len(self))

    def change_move(self):
        """This method describes change move players"""
        self.cur_player = self._players[self._move]
        if self._last_player is not None:
            self._last_player.is_move = False
            self._last_player.change_move()
        self.cur_player.is_move = True
        self.cur_player.change_move()
        self._last_player = self.cur_player

    def change_streak(self, is_draw: bool = False):
        """This method describes change streak players"""
        if is_draw:
            self._last_winner = None
            for player in self._players:
                player.drop_streak()
        else:
            if self._last_winner is None:
                self.cur_player.streak += 1
            elif self._last_winner == self.cur_player:
                self.cur_player.streak += 1
            else:
                self.cur_player.drop_streak()
            self._last_winner = self.cur_player

    def get_winner_name(self) -> str:
        """This method return winner name"""
        return refactor_name(self.cur_player.name)

    @property
    def cur_player(self) -> Player:
        """This property return current player"""
        return self._cur_player

    @cur_player.setter
    def cur_player(self, current_player: Player):
        """This property change current player"""
        if not isinstance(current_player, Player):
            raise TypeError
        self._cur_player = current_player

    @property
    def move(self) -> int:
        """This property return index current player is moving"""
        return self._move

    @move.setter
    def move(self, player_idx):
        """This property change index current player is moving"""
        self._move = player_idx

    def restart(self):
        """This method describes drop players info"""
        for player in self._players:
            player.drop_info()
