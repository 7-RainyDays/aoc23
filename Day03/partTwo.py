import numpy as np

def has_gear_ratio(matrix, i, j):
    part_numbers = []
    for row in range(i - 1, i + 2):
        current_number = 0
        try:
            if any(item.isdigit() for item in matrix[row][j - 1:j + 2]):
                #continue here ------------------------
                pass
            part_numbers.append(current_number)
        except IndexError:
            continue

    if len(part_numbers) == 2:
        return np.prod(part_numbers)
    return False


def find_gear(matrix):
    solution = 0
    global rows
    rows = len(matrix)
    global cols
    cols = len(matrix[0])

    i = 0

    while i < rows:
        j = 0
        while j < cols:
            if matrix[i][j] == '*':
                result = has_gear_ratio(matrix, i, j)
                if result:
                    solution += result
            j += 1
        i += 1
    return solution


with open('input.txt', 'r') as f:
    lines = f.readlines()
    matrix = [line.strip() for line in lines]
    solution = find_gear(matrix)
    print(solution)