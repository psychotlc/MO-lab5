import numpy as np
from game_with_nature import GameWithNature

ALPHA = 0.5
MATRIX = np.array([[7, 19, 1, 19, 8],
                   [7, 18, 5, 2, 6],
                   [15, 3, 16, 19, 4],
                   [5, 12, 19, 14, 18]])

if __name__ == "__main__":
    game_with_nature_instance = GameWithNature(matrix=MATRIX, ALPHA=ALPHA)
    game_with_nature_instance.solve()