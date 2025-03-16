class Spreadsheet:
    """
    Grade [Medium]
    A spreadsheet is a grid with 26 columns (labeled from 'A' to 'Z') and a given number of rows.
    Each cell in the spreadsheet can hold an integer value between 0 and 105.

    Implement the Spreadsheet class:

    Spreadsheet(int rows) Initializes a spreadsheet with 26 columns (labeled 'A' to 'Z') and
    the specified number of rows. All cells are initially set to 0.
    void setCell(String cell, int value) Sets the value of the specified cell. The cell reference is provided in
    the format "AX" (e.g., "A1", "B10"), where the letter represents the column (from 'A' to 'Z')
    and the number represents a 1-indexed row.
    void resetCell(String cell) Resets the specified cell to 0.
    int getValue(String formula) Evaluates a formula of the form "=X+Y", where X and Y are either cell references or
    non-negative integers, and returns the computed sum.
    Note: If getValue references a cell that has not been explicitly set using setCell, its value is considered 0.

    Note: Please do not copy the description during the contest to maintain the integrity of your submissions.
    """

    def __init__(self, rows: int):
        self.rows = rows
        self.data = [[0 for _ in range(26)] for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        col, row = self._get_col_and_row(cell)
        self.data[row][col] = value

    def resetCell(self, cell: str) -> None:
        col, row = self._get_col_and_row(cell)
        self.data[row][col] = 0

    def getValue(self, formula: str) -> int:
        left, right = formula[1:].split('+')
        if not left.isnumeric():
            col_l, row_l = self._get_col_and_row(left)
            value_l = self.data[row_l][col_l]
        else:
            value_l = int(left)

        if not right.isnumeric():
            col_r, row_r = self._get_col_and_row(right)
            value_r = self.data[row_r][col_r]
        else:
            value_r = int(right)
        return value_l + value_r

    def _get_col_and_row(self, cell):
        col, row = ord(cell[0]) - ord('A'), int(cell[1:]) - 1
        return col, row

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)