with open('input.txt', 'r') as f:
    lines = f.readlines()
    seeds = [int(num) for num in lines[0].split() if num.isdigit()]
    lines = [y.strip() for y in lines[1:] if any(c.isalnum() for c in str(y))]

    maps = []
    current_group = []
    for line in lines:
        if not any(d.isnumeric() for d in line):
            if current_group:
                maps.append(current_group)
                current_group = []
        else:
            current_group.append(list(map(int, line.split())))

    if current_group:
        maps.append(current_group)

    for i in range(len(maps)):
        for k in range(len(seeds)):
            for j in range(len(maps[i])):
                source_r = maps[i][j][1]
                max_r = source_r + maps[i][j][2]
                if seeds[k] in range(source_r, max_r):
                    mapped = seeds[k] - source_r + maps[i][j][0]
                    seeds[k] = mapped
                    break

print(min(seeds))
