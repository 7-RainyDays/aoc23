total_count = 0

number_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

keys = number_dict.keys()

def get_first_numeric (line):
    for i in range(0, len(line)):
        if line[i].isnumeric():
            match = line[i]
            return match
        for key in keys:
            if key in line[0:i+1]:
                return number_dict[key]

def get_last_numeric (line):
    for i in range(len(line)-1, -1, -1):
        if line[i].isnumeric():
            match = line[i]
            return match
        for key in keys:
            if key in line[i:len(line)]:
                return number_dict[key]

with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        first = get_first_numeric (line)
        last = get_last_numeric (line)
        total_count += int(first+last)
    print(total_count)

