import pieces
class Board: 
    def __init__(self): 
        self.white_pawns = pieces.WHITE_PAWNS
        self.white_rooks = pieces.WHITE_ROOKS
        self.white_knights = pieces.WHITE_KNIGHTS
        self.white_bishops = pieces.WHITE_BISHOPS
        self.white_queens = pieces.WHITE_QUEENS
        self.white_king = pieces.WHITE_KING

        self.black_pawns = pieces.BLACK_PAWNS
        self.black_rooks = pieces.BLACK_ROOKS
        self.black_knights = pieces.BLACK_KNIGHTS       
        self.black_bishops = pieces.BLACK_BISHOPS
        self.black_queens = pieces.BLACK_QUEENS
        self.black_king = pieces.BLACK_KING

        self.update_occupancy()

    def update_occupancy(self):
        self.white_occupancy = self.white_pawns | self.white_rooks | self.white_knights | self.white_bishops | self.white_queens | self.white_king
        self.black_occupancy = self.black_pawns | self.black_rooks | self.black_knights | self.black_bishops | self.black_queens | self.black_king
        self.all_occupancy = self.white_occupancy | self.black_occupancy


    def print_board(self):
        board = ""
        for rank in range(7, -1, -1): 
            for file in range(8):
                square = rank * 8 + file

                piece = "."
                for symbol, attr in pieces.PIECE_MAP.items():
                    bb = getattr(self,attr)
                    if (bb >> square) & 1:
                        piece = symbol
                        break

                print(piece, end = "")
            print()
        print()