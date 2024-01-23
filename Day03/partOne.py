def find_number(matrix):
    solution = 0
    global rows
    rows = len(matrix)
    global cols
    cols = len(matrix[0])

    i = 0

    while i < rows:
        j = 0
        while j < cols:
            if matrix[i][j].isnumeric():
                current_number = matrix[i][j]
                k = j +1
                while k < cols and matrix[i][k].isdigit():
                    current_number += matrix[i][k]
                    k += 1
                if is_part_number(matrix, i, j, current_number):
                    solution += int(current_number)
                j = k
            else:
                j += 1
        i += 1
    return solution


def is_part_number(matrix, i, j, current_number):
    for row in range(i - 1, i + 2):
        for col in range(j - 1, j + len(current_number) + 1):
            try:
                if matrix[row][col] != "." and not matrix[row][col].isnumeric():
                    return True
            except IndexError:
                continue
    return False


with open('input.txt', 'r') as f:
    lines = f.readlines()
    matrix = [line.strip() for line in lines]
    solution = find_number(matrix)
    print(solution)
