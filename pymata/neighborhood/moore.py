MOORE_NEIGHBORHOOD_SIZE = 3
DISABLED_CELL_VALUE = 0


class MooreNeighborhood:
    """Contains logic for calculating Moore neighborhood"""

    @classmethod
    def get_neighborhood(cls, matrix, row: int, col: int):
        if matrix is None:
            raise ValueError("'matrix' argument must not be None")

        if row < 0 or col < 0:
            raise ValueError(
                "'row' and 'col' arguments must be greater or equal to zero"
            )

        output = [
            [DISABLED_CELL_VALUE] * MOORE_NEIGHBORHOOD_SIZE
            for _ in range(MOORE_NEIGHBORHOOD_SIZE)
        ]

        row_upper_bound = len(matrix) - 1
        col_upper_bound = len(matrix[0]) - 1

        output[1][1] = matrix[row][col]

        output[0][0] = (
            matrix[row - 1][col - 1] if row > 0 and col > 0 else DISABLED_CELL_VALUE
        )
        output[0][1] = matrix[row - 1][col] if row > 0 else DISABLED_CELL_VALUE
        output[0][2] = (
            matrix[row - 1][col + 1]
            if row > 0 and col < col_upper_bound
            else DISABLED_CELL_VALUE
        )

        output[1][0] = matrix[row][col - 1] if col > 0 else DISABLED_CELL_VALUE
        output[1][2] = (
            matrix[row][col + 1] if col < col_upper_bound else DISABLED_CELL_VALUE
        )

        output[2][0] = (
            matrix[row + 1][col - 1]
            if row < row_upper_bound and col > 0
            else DISABLED_CELL_VALUE
        )
        output[2][1] = (
            matrix[row + 1][col] if row < row_upper_bound else DISABLED_CELL_VALUE
        )
        output[2][2] = (
            matrix[row + 1][col + 1]
            if row < row_upper_bound and col < col_upper_bound
            else DISABLED_CELL_VALUE
        )

        return output
