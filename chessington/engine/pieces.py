"""
Definitions of each of the different chess pieces.
"""

from abc import ABC, abstractmethod

from chessington.engine.data import Player, Square

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player):
        self.player = player

    @abstractmethod
    def get_available_moves(self, board):
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """

    def get_available_moves(self, board):
        # Basic move 
        current_square = board.find_piece(self)
        possible_moves = []

        direction = -1 if self.player == Player.BLACK else +1
        start_row = 6 if self.player == Player.BLACK else 1
        
        next_step_forward = Square.at(current_square.row + direction, current_square.col)
        if next_step_forward.row > 7 or next_step_forward.row < 0:
            return []

        diagonal_left_move = Square.at(current_square.row + direction, current_square.col-1)
        diagonal_right_move = Square.at(current_square.row + direction, current_square.col+1)
        if diagonal_left_move.col >= 0: 
            if board.get_piece(diagonal_left_move) and not board.get_piece(diagonal_left_move).player == self.player:
                possible_moves += [diagonal_left_move]
        if diagonal_right_move.col <= 7:
            if board.get_piece(diagonal_right_move) and not board.get_piece(diagonal_right_move).player == self.player:
                possible_moves += [diagonal_right_move]

        if board.get_piece(next_step_forward) is None:
            possible_moves += [next_step_forward]
            pawn_extra_step_forward = Square.at(current_square.row + (2 * direction), current_square.col)
            if current_square.row == start_row and not board.get_piece(pawn_extra_step_forward):
                possible_moves += [pawn_extra_step_forward]
        
        return list(filter(lambda move: move.row <= 7 and move.row >= 0 , possible_moves))


class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        current_square = board.find_piece(self)
        directions = {
            'left': {'row':0, 'col':-1},
            'right': {'row':0, 'col':+1},
            'up': {'row':+1, 'col':0},
            'down': {'row':-1, 'col':0},
            'diag-up-left': {'row':+1, 'col':-1},
            'diag-up-right': {'row':+1, 'col':+1},
            'diag-down-left': {'row':-1, 'col':-1},
            'down-down-right': {'row':-1, 'col':+1},
        }

        possible_moves = []
        for next_direction in directions.values():
            possible_moves += [Square.at(current_square.row + next_direction['row'], current_square.col + next_direction['col'])]
        return possible_moves