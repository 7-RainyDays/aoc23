from functools import reduce

with open('input.txt', 'r') as f:
    lines = f.readlines()
    time = int(''.join([char for char in lines[0] if char.isnumeric()]))
    record = int(''.join([char for char in lines[1] if char.isnumeric()]))
    possibilities = [sum(1 for i in range(time) if i * (time - i) > record)]
    print(reduce(lambda x, y: x * y, possibilities))