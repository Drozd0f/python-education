"""This module contains game model tic-tac-toe"""
import logging
import typing as t

from src.utils import get_mark_list


class Game:
    """This class describes game logic"""
    _is_pending = True
    _mark = get_mark_list()
    _is_draw = False
    _col_count = 0
    _diag_count = 0
    _rev_diag_count = 0

    def player_input(self, board: list, current_pos: list, current_player: int) -> t.Optional[int]:
        """This method return current_player if position on the board not occupied"""
        if board[current_pos[0]][current_pos[1]] not in self._mark:
            board[current_pos[0]][current_pos[1]] = self._mark[current_player]
            return 1 if current_player == 0 else 0
        return None

    def _check_line(self, line: list, mark: str):
        if line.count(mark) == 3:
            self._is_pending = False

    def _check_column(self, mark: str, column: str):
        if column == mark:
            self._col_count += 1
            if self._col_count == 3:
                self._is_pending = False

    def _check_diagonal(self, diag: str, mark: str):
        if diag == mark:
            self._diag_count += 1
            if self._diag_count == 3:
                self._is_pending = False

    def _check_rev_diagonal(self, diag: str, mark: str):
        if diag == mark:
            self._rev_diag_count += 1
            if self._rev_diag_count == 3:
                self._is_pending = False

    def _game_loop(self, board: list, mark: str):
        for idx, line in enumerate(board):
            self._col_count = 0
            self._diag_count = 0
            self._rev_diag_count = 0
            self._check_line(line, mark)
            for jdx in range(len(line[idx:])):
                self._check_column(
                    mark,
                    board[jdx][idx]
                )
                self._check_diagonal(
                    board[idx + jdx][jdx],
                    mark
                )
                self._check_rev_diagonal(
                    board[idx + jdx][-(jdx + 1)],
                    mark
                )
            if not self._is_pending:
                break

    def check_win(self, board: list, mark: str):
        """This method describes board for a winning combination"""
        temp_board = [colum for line in board for colum in line]
        if temp_board.count('0') == 0:
            self._is_pending = False
            self._is_draw = True
        else:
            self._game_loop(board, mark)
            logging.debug(self._is_pending)

    def restart(self):
        """This method describes drop game info"""
        self._is_pending = True
        self._is_draw = False
        self._col_count = 0
        self._diag_count = 0
        self._rev_diag_count = 0

    @property
    def is_pending(self) -> bool:
        """This property return pending status"""
        return self._is_pending

    @property
    def is_draw(self) -> bool:
        """This property return draw status"""
        return self._is_draw
