from pymata.neighborhood.moore import MooreNeighborhood

class Automata:
    def __init__(self, matrix: list[list[int]]) -> None:
        if len(matrix) < 1 or len(matrix[0]) < 1:
            raise ValueError("aaa")

        self.__rows = len(matrix)
        self.__cols = len(matrix[0])
        self.__matrix = matrix

    @classmethod
    def from_size(cls, rows: int, cols: int):
        if rows < 1 or cols < 1:
            raise ValueError("aaa")

        matrix = [[0 for x in range(cols)] for x in range(rows)]
        return cls(matrix)

    def get_matrix(self):
        return self.__matrix

    def set(self, row: int, col: int, value: int):
        if row >= self.__rows:
            raise ValueError("aaa")

        if col >= self.__cols:
            raise ValueError("aaa")

        if row < 0 or col < 0:
            raise ValueError("aaa")

        if not isinstance(value, int):
            raise ValueError("'value' should be integer")

        self.__matrix[row][col] = value

    def __apply_rule(self, row, col):
        neighborhood = MooreNeighborhood.get_neighborhood(self.__matrix, row, col)
        row_1 = sum(neighborhood[0])
        row_2 = neighborhood[1][0] + neighborhood[1][2]
        row_3 = sum(neighborhood[2])
        n_sum = row_1 + row_2 + row_3

        cell = neighborhood[1][1]
        if cell == 0 and n_sum == 3:
            return 1

        if cell == 1 and (n_sum == 2 or n_sum == 3):
            return 1

        if cell == 1 and (n_sum < 2 or n_sum > 3):
            return 0

        return self.__matrix[row][col]

    def transition(self):
        new_matrix: list[int] = [
            [0 for x in range(self.__cols)] for x in range(self.__rows)
        ]

        for idx_row, row in enumerate(self.__matrix):
            for idx_col, _ in enumerate(row):
                new_matrix[idx_row][idx_col] = self.__apply_rule(idx_row, idx_col)

        self.__matrix = new_matrix
