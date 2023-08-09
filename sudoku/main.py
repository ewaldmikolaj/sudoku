class Cell:
    def __init__(self, x: int, y: int) -> None:
        self._x = x
        self._y = y
        self._row = None
        self._column = None
        self._box = None
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Row:
    def __init__(self, x: int) -> None:
        self._x = x
        self._cells = []


class Column:
    def __init__(self, y: int) -> None:
        self._y = y
        self._cells = []


class Box:
    def __init__(self, x: int, y: int, box_size: int) -> None:
        self._x = range(x, x + box_size)
        self._y = range(y, y + box_size)
        self._cells = []


class Board:
    def __init__(self, size: int = 9) -> None:
        pass


if __name__ == "__main__":
    pass
