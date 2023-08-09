import pytest

from main import Cell, Row, Column, Box, Board


@pytest.fixture
def cell():
    cell = Cell(0, 0)
    yield cell
    del cell


def test_cell_value_should_return_5_when_assigned(cell):
    cell.value = 5

    expected = 5
    actual = cell.value

    assert expected == actual


def test_cell_column_should_return_object_when_assigned(cell):
    pass
