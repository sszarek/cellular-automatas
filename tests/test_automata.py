import pytest
from pymata.automata import Automata


def test_get_matrix():
    sut = Automata.from_size(11, 10)
    matrix = sut.get_matrix()

    assert len(matrix) == 11
    assert len(matrix[0]) == 10


@pytest.mark.parametrize(["row", "col"], [(-1, -1), (2, 1), (1, 2), (2, 2)])
def test_set_invalid_data(row, col):
    sut = Automata.from_size(2, 2)

    with pytest.raises(ValueError):
        sut.set(row, col, 1)


def test_set_non_integer_value():
    sut = Automata.from_size(2, 2)

    with pytest.raises(ValueError):
        sut.set(1, 1, "foobar")


def test_set_valid_data():
    sut = Automata.from_size(2, 2)
    sut.set(1, 1, 1)

    matrix = sut.get_matrix()
    assert matrix == [[0, 0], [0, 1]]


def test_transition_dead_cell():
    sut = Automata.from_size(3, 3)
    sut.set(1, 1, 0)

    sut.transition()

    matrix = sut.get_matrix()
    assert matrix == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def test_transition_dead_cell_reproduction():
    sut = Automata.from_size(3, 3)
    sut.set(1, 1, 1)
    sut.set(0, 0, 1)
    sut.set(0, 1, 1)
    sut.set(1, 0, 1)

    sut.transition()

    matrix = sut.get_matrix()
    assert matrix == [[1, 1, 0], [1, 1, 0], [0, 0, 0]]


def test_transition_live_cell_underpopulation():
    sut = Automata.from_size(3, 3)
    sut.set(1, 1, 1)
    sut.set(0, 0, 1)

    sut.transition()

    matrix = sut.get_matrix()
    assert matrix == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def test_transition_live_cell_survives():
    sut = Automata.from_size(3, 3)
    sut.set(1, 1, 1)
    sut.set(0, 0, 1)
    sut.set(1, 0, 1)

    sut.transition()

    matrix = sut.get_matrix()
    assert matrix == [[1, 0, 0], [1, 1, 0], [0, 0, 0]]
