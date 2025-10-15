def row_correct(sudoku: list):
    for rows in sudoku:
        n = []
        for numbers in rows:
            if numbers == 0:
                continue
            elif numbers != 0 and numbers not in n:
                n.append(numbers)
            elif numbers in n:
                return(False)
    return(True)

def column_correct(sudoku: list):
    n = len(sudoku)
    for c in range(n):
        seen = []
        for r in range(n):
            val = sudoku[r][c]
            if val not in seen:
                seen.append(val)
            elif val in seen and val != 0:
                return(False)     
    return(True)

def block_correct(sudoku: list):
    for start_row in (0, 3, 6):
        for start_col in (0, 3, 6):
            block = []
            for r in range(start_row, start_row + 3):
                for c in range(start_col, start_col + 3):
                    val = sudoku[r][c]
                    if val not in block:
                        block.append(val)
                    elif val in block and val != 0:
                        return False
    return True
            

def sudoku_grid_correct(sudoku: list):
    return row_correct(sudoku) and column_correct(sudoku) and block_correct(sudoku)
