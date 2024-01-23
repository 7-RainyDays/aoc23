import re
from functools import reduce

with open('input.txt', 'r') as f:
    lines = f.readlines()
    numeric_values = [[int(value) for value in re.findall(r'\b\d+\b', line)] for line in lines]
    grouped_values = list(zip(*numeric_values))
    possibilities = [sum(1 for i in range(time) if i * (time - i) > record) for time, record in grouped_values]
    print(reduce(lambda x, y: x * y, possibilities))