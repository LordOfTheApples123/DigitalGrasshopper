from enum import Enum


class GameState(Enum):
    PLAYING = 0
    WIN = 1
    FAIL = 2


class CellState(Enum):
    EMPTY = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    CAN_MOVE = -2
    BLOCKED = -1


class Cell:
    def __init__(self, state: CellState = CellState.EMPTY):
        self._state = state

    @property
    def state(self) -> CellState:
        return self._state


class DigitalGrasshopperGame:
    preset_1 = [[Cell(CellState.EMPTY), Cell(CellState.EMPTY), Cell(CellState.ONE), Cell(CellState.THREE)],
                [Cell(CellState.EMPTY), Cell(CellState.EMPTY), Cell(CellState.EMPTY), Cell(CellState.EMPTY)],
                [Cell(CellState.EMPTY), Cell(CellState.TWO), Cell(CellState.ONE), Cell(CellState.EMPTY)],
                [Cell(CellState.THREE), Cell(CellState.EMPTY), Cell(CellState.EMPTY), Cell(CellState.EMPTY)]]
    preset_2 = [[Cell(CellState.EMPTY), Cell(CellState.EMPTY), Cell(CellState.ONE), Cell(CellState.THREE)],
                [Cell(CellState.EMPTY), Cell(CellState.EMPTY), Cell(CellState.EMPTY), Cell(CellState.EMPTY)],
                [Cell(CellState.EMPTY), Cell(CellState.TWO), Cell(CellState.ONE), Cell(CellState.EMPTY)],
                [Cell(CellState.THREE), Cell(CellState.EMPTY), Cell(CellState.EMPTY), Cell(CellState.EMPTY)]]
    preset_3 = [[Cell(CellState.EMPTY), Cell(CellState.EMPTY), Cell(CellState.ONE), Cell(CellState.THREE)],
                [Cell(CellState.EMPTY), Cell(CellState.EMPTY), Cell(CellState.EMPTY), Cell(CellState.EMPTY)],
                [Cell(CellState.EMPTY), Cell(CellState.TWO), Cell(CellState.ONE), Cell(CellState.EMPTY)],
                [Cell(CellState.THREE), Cell(CellState.EMPTY), Cell(CellState.EMPTY), Cell(CellState.EMPTY)]]

    def __init__(self, row_count: int, col_count: int):
        self._curr_lvl = 1
        self._row_count = row_count
        self._col_count = col_count
        self.new_game()

    def get_field(self):
        return self._field

    def new_game(self, ) -> None:
        if self._row_count == 4 and self._col_count == 4:
            self._field = [[Cell(CellState.EMPTY), Cell(CellState.EMPTY), Cell(CellState.ONE), Cell(CellState.THREE)],
                           [Cell(CellState.EMPTY), Cell(CellState.EMPTY), Cell(CellState.EMPTY), Cell(CellState.EMPTY)],
                           [Cell(CellState.EMPTY), Cell(CellState.TWO), Cell(CellState.ONE), Cell(CellState.EMPTY)],
                           [Cell(CellState.THREE), Cell(CellState.EMPTY), Cell(CellState.EMPTY), Cell(CellState.EMPTY)]]
        if self._row_count == 6 and self._col_count == 6:
            self._field = [[Cell(CellState.TWO), Cell(CellState.TWO), Cell(CellState.TWO), Cell(CellState.TWO),
                            Cell(CellState.TWO), Cell(CellState.TWO)],
                           [Cell(CellState.TWO), Cell(CellState.TWO), Cell(CellState.TWO), Cell(CellState.TWO),
                            Cell(CellState.TWO), Cell(CellState.TWO)],
                           [Cell(CellState.TWO), Cell(CellState.TWO), Cell(CellState.TWO), Cell(CellState.TWO),
                            Cell(CellState.TWO), Cell(CellState.TWO)],
                           [Cell(CellState.TWO), Cell(CellState.TWO), Cell(CellState.TWO), Cell(CellState.TWO),
                            Cell(CellState.TWO), Cell(CellState.TWO)],
                           [Cell(CellState.TWO), Cell(CellState.TWO), Cell(CellState.TWO), Cell(CellState.TWO),
                            Cell(CellState.TWO), Cell(CellState.TWO)],
                           [Cell(CellState.TWO), Cell(CellState.TWO), Cell(CellState.TWO), Cell(CellState.TWO),
                            Cell(CellState.TWO), Cell(CellState.TWO)]]
        self._state = GameState.PLAYING

    @property
    def row_count(self) -> int:
        return self._row_count

    @property
    def col_count(self) -> int:
        return self._col_count

    @property
    def state(self) -> GameState:
        return self._state

    def __getitem__(self, indices: tuple) -> Cell:
        return self._field[indices[0]][indices[1]]

    def left_mouse_click(self, row: int, col: int) -> None:
        if self.state != GameState.PLAYING:
            return
        cell = self[row, col]
        if cell.state == CellState.EMPTY or cell.state == CellState.BLOCKED or cell.state == CellState.CAN_MOVE:
            return
        if cell.state != CellState.BLOCKED or CellState.EMPTY:
            self.can_move(row, col, cell.state)
            cell._state = CellState.EMPTY

    to_go_count = 0
    tempRow: int
    tempCol: int
    tempState: CellState

    def can_move(self, row: int, col: int, state: CellState) -> None:
        offset = 0
        if state == CellState.ONE:
            offset = 1
        elif state == CellState.TWO:
            offset = 2
        elif state == CellState.THREE:
            offset = 3
        elif state == CellState.FOUR:
            offset = 4

        self.tempState = self._field[row][col].state
        if row + offset < len(self._field) and col + offset < 4 and self._field[row + offset][
            col + offset].state == CellState.EMPTY:
            self.to_go_count = + 1
            self._field[row][col] = Cell(CellState.CAN_MOVE)
            self._field[row + offset][col + offset] = Cell(CellState.CAN_MOVE)
        if row + offset < 4 and self._field[row + offset][col].state == CellState.EMPTY:
            self._field[row + offset][col] = Cell(CellState.CAN_MOVE)
            self.to_go_count = + 1
            self._field[row][col] = Cell(CellState.CAN_MOVE)
        if col + offset < 4 and self._field[row][col + offset].state == CellState.EMPTY:
            self._field[row][col + offset] = Cell(CellState.CAN_MOVE)
            self.to_go_count = + 1
            self._field[row][col] = Cell(CellState.CAN_MOVE)
        if col - offset >= 0 and row - offset >= 0 and self._field[row - offset][
            col - offset].state == CellState.EMPTY:
            self._field[row - offset][col - offset] = Cell(CellState.CAN_MOVE)
            self.to_go_count = + 1
            self._field[row][col] = Cell(CellState.CAN_MOVE)
        if col - offset >= 0 and self._field[row][col - offset].state == CellState.EMPTY:
            self._field[row][col - offset] = Cell(CellState.CAN_MOVE)
            self.to_go_count = + 1
            self._field[row][col] = Cell(CellState.CAN_MOVE)
        if row - offset >= 0 and self._field[row - offset][col].state == CellState.EMPTY:
            self._field[row - offset][col] = Cell(CellState.CAN_MOVE)
            self.to_go_count = + 1
            self._field[row][col] = Cell(CellState.CAN_MOVE)
        if row - offset >= 0 and col + offset < 4 and self._field[row - offset][
            col + offset].state == CellState.EMPTY:
            self._field[row - offset][col + offset] = Cell(CellState.CAN_MOVE)
            self.to_go_count = + 1
            self._field[row][col] = Cell(CellState.CAN_MOVE)
        if row + offset < 4 and col - offset >= 0 and self._field[row + offset][
            col - offset].state == CellState.EMPTY:
            self._field[row + offset][col - offset] = Cell(CellState.CAN_MOVE)
            self.to_go_count = + 1
            self._field[row][col] = Cell(CellState.CAN_MOVE)
        self.tempRow: int = row
        self.tempCol: int = col
        if self.to_go_count == 0:
            self._state = GameState.FAIL

    def is_win(self):
        win_counter = 0
        for i in range(len(self._field)):
            for j in range(len(self._field[i])):
                if self._field[i][j].state == CellState.ONE or self._field[i][j].state == CellState.TWO \
                        or self._field[i][j].state == CellState.THREE or self._field[i][j].state == CellState.FOUR:
                    win_counter += 1

        if win_counter == 0:
            self._state = GameState.WIN
            return
        elif self.to_go_count == 0 and win_counter == 0:
            self._state = GameState.FAIL
            return
        elif self.to_go_count > 0:
            self._state = GameState.PLAYING
            return

    def clear(self, field) -> None:
        self.to_go_count = 0
        for i in range(len(field)):
            for j in range(len(field[i])):
                if field[i][j].state == CellState.CAN_MOVE:
                    field[i][j] = Cell(CellState.EMPTY)

    def right_mouse_click(self, row: int, col: int) -> None:
        if self._field[row][col].state == CellState.CAN_MOVE:
            if self._field[row][col] == self._field[self.tempRow][self.tempCol]:
                self._field[self.tempRow][self.tempCol]._state = self.tempState
            else:
                cell_to = self[row, col]
                cell_to._state = CellState.BLOCKED
            self.clear(self._field)
            self.is_win()

    def load_level_1(self):
        self._field = self.preset_1.copy()
        self._curr_lvl = 1


    def load_level_2(self):
        self._field = self.preset_2.copy()
        self._curr_lvl = 2

    def load_level_3(self):
        self._field = self.preset_3.copy()
        self._curr_lvl = 3


    def replay_fc(self):
        if(self._curr_lvl == 1):
            self._field = self.preset_1.copy()
        if (self._curr_lvl == 2):
            self._field = self.preset_2.copy()
        if (self._curr_lvl == 3):
            self._field = self.preset_3.copy()