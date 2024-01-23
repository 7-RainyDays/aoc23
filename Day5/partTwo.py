with open('input.txt', 'r') as f:
    lines = f.readlines()
    seeds = [int(num) for num in lines[0].split() if num.isdigit()]
    lines = [y.strip() for y in lines[1:] if any(c.isalnum() for c in str(y))]

    paired = []

    for i in range(0, len(seeds), 2):
        paired.append([seeds[i], seeds[i+1]])


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
        evaluate_later = []
        for k in range(0, len(paired)):
            seed_start = paired[k][0]
            seed_max = paired[k][0] + paired[k][1]
            for j in range(len(maps[i])):
                source_r = maps[i][j][1]
                max_r = source_r + maps[i][j][2]

                if seed_start >= source_r and seed_max <= max_r:
                    mapped = seed_start - source_r + maps[i][j][0]
                    paired[k][0] = mapped
                    break

                elif any(x in range(source_r, max_r) for x in range(seed_start, seed_max)):
                    factor = abs(seed_start - source_r)
                    split_range_1 = (seed_start, factor)
                    split_range_2 = (seed_start + factor, paired[k][1] - factor)
                    print(split_range_1, split_range_2)

                    if split_range_1 in range(source_r, max_r):
                        split_range_1[0] = split_range_1[0] - source_r + maps[i][j][0]
                        break
                    else:
                        split_range_2[0] = split_range_2[0] - source_r + maps[i][j][0]
                        break


        seeds.extend(evaluate_later)

    print(paired)
