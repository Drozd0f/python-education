"""This module contains board model tic-tac-toe"""


class Board:
    """This class describes working with board"""
    _board = [
        ['0', '0', '0'],
        ['0', '0', '0'],
        ['0', '0', '0']
    ]

    def __setitem__(self, coord_x, value, coord_y=0):
        if coord_y in range(0, 3) and coord_x in range(0, 3):
            self._board[coord_x][coord_y] = value
        else:
            raise IndexError

    def __getitem__(self, index):
        if index in range(0, 3):
            return self._board[index]
        raise IndexError

    def restart(self):
        """This method describes drop board info"""
        self._board = [
            ['0', '0', '0'],
            ['0', '0', '0'],
            ['0', '0', '0']
        ]

    @property
    def board(self) -> list:
        """This property return board"""
        return self._board
