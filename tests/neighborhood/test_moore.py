import pytest

from pycells.neighborhood.moore import MooreNeighborhood


def test_get_neighborhood_none_matrix():
    with pytest.raises(ValueError):
        MooreNeighborhood.get_neighborhood(None, 0, 0)


def test_get_neighborhood_negative_row():
    matrix = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

    with pytest.raises(ValueError):
        MooreNeighborhood.get_neighborhood(matrix, -1, 0)


def test_get_neighborhood_negative_col():
    matrix = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

    with pytest.raises(ValueError):
        MooreNeighborhood.get_neighborhood(matrix, 0, -2)


def test_get_neighborhood_gold_flow():
    matrix = [
        [0, 0, 0, 0],
        [0, 1, 1, 1],
        [0, 1, 1, 1],
        [0, 1, 1, 1],
    ]
    neighborhood = MooreNeighborhood.get_neighborhood(matrix, 2, 2)

    expected = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ]
    assert neighborhood == expected


@pytest.mark.parametrize(
    ["row", "col", "expected"],
    [
        (0, 1, [[0, 0, 0], [1, 1, 1], [1, 1, 1]]),
        (1, 0, [[0, 1, 1], [0, 1, 1], [0, 1, 1]]),
        (2, 1, [[1, 1, 1], [1, 1, 1], [0, 0, 0]]),
        (1, 2, [[1, 1, 0], [1, 1, 0], [1, 1, 0]]),
        (0, 0, [[0, 0, 0], [0, 1, 1], [0, 1, 1]]),
        (2, 2, [[1, 1, 0], [1, 1, 0], [0, 0, 0]]),
    ],
)
def test_get_neighborhood_edges(row, col, expected):
    matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

    neighborhood = MooreNeighborhood.get_neighborhood(matrix, row, col)

    assert neighborhood == expected
