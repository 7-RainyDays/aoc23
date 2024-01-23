total_count = 0


def extract_numerics(input_string):
    return ''.join(char for char in input_string if char.isdigit())


with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        numbers = extract_numerics(line)
        total_count += int(numbers[0] + numbers[-1])


print(total_count)
