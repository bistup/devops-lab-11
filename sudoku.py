sudoku = [
    # cell value                # cell number
    0, 0, 4, 0, 5, 0, 0, 0, 0,  #  0,  1,  2,  3,  4,  5,  6,  7,  8,
    9, 0, 0, 7, 3, 4, 6, 0, 0,  #  9, 10, 11, 12, 13, 14, 15, 16, 17,
    0, 0, 3, 0, 2, 1, 0, 4, 9,  # 18, 19, 20, 21, 22, 23, 24, 25, 26,  
    0, 3, 5, 0, 9, 0, 4, 8, 0,  # 27, 28, 29, 30, 31, 32, 33, 34, 35,
    0, 9, 0, 0, 0, 0, 0, 3, 0,  # 36, 37, 38, 39, 40, 41, 42, 43, 44,
    0, 7, 6, 0, 1, 0, 9, 2, 0,  # 45, 46, 47, 48, 49, 50, 51, 52, 53,
    3, 1, 0, 9, 7, 0, 2, 0, 0,  # 54, 55, 56, 57, 58, 59, 60, 61, 62,
    0, 0, 9, 1, 8, 2, 0, 0, 3,  # 63, 64, 65, 66, 67, 68, 69, 70, 71,
    0, 0, 0, 0, 6, 0, 1, 0, 0,  # 72, 73, 74, 75, 76, 77, 78, 79, 80
    # zero = empty.
]
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}

def options(cell, sudoku):
    """ determines the degree of freedom for a cell. """
    column = {v for ix, v in enumerate(sudoku) if ix % 9 == cell % 9}
    row = {v for ix, v in enumerate(sudoku) if ix // 9 == cell // 9}
    box = {v for ix, v in enumerate(sudoku) if (ix // (9 * 3) == cell // (9 * 3)) and ((ix % 9) // 3 == (cell % 9) // 3)}
    return numbers - (box | row | column)

def solve_sudoku(sudoku):
    initial_state = sudoku[:] 
    job_queue = [initial_state] 

    while job_queue:
        state = job_queue.pop(0)
        if not any(i == 0 for i in state): 
            return state

        degrees_of_freedom = [0 if v != 0 else len(options(ix, state)) for ix, v in enumerate(state)]
        if all(v == 0 for v in degrees_of_freedom):
            return state

        least_freedom = min(v for v in degrees_of_freedom if v > 0)
        cell = degrees_of_freedom.index(least_freedom)

        for option in options(cell, state): 
            new_state = state[:]
            new_state[cell] = option
            job_queue.append(new_state)
    
    return state  # Return the last state if no solution is found

# Example usage:
sudoku = [
    0, 0, 4, 0, 5, 0, 0, 0, 0, 9, 0, 0, 7, 3, 4, 6, 0, 0, 0, 0, 3, 0, 2, 1, 0, 4, 9, 0, 3, 5, 0, 9, 0, 4, 8, 0, 0, 9, 0, 0, 0, 0, 0, 3, 0, 0, 7, 6, 0, 1, 0, 9, 2, 0, 3, 1, 0, 9, 7, 0, 2, 0, 0, 0, 0, 9, 1, 8, 2, 0, 0, 3, 0, 0, 0, 0, 6, 0, 1, 0, 0
]

solved_sudoku = solve_sudoku(sudoku)

if solved_sudoku:
    # Print out the solution
    for i in range(9):
        print(solved_sudoku[i * 9:i * 9 + 9])
else:
    print("No solution found.")