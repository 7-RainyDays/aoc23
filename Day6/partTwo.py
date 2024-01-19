with open('input.txt', 'r') as f:
    lines = f.readlines()
    seeds = [int(num) for num in lines[0].split() if num.isdigit()]
    lines = [y.strip() for y in lines[1:] if any(c.isalnum() for c in str(y))]

    print(seeds)