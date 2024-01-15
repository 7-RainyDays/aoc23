with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [y.strip() for y in lines if any(c.isdigit() for c in str(y))]

    seeds = [int(num) for num in lines[0].split() if num.isdigit()]

    maps = [[int(y) for y in m.split(" ")] for m in lines[1:]]


    for i in range(len(maps)):
        source_r = maps[i][1]
        max_r = source_r + maps[i][2]
        result = []

        for x in seeds:

            if x in range(source_r, max_r):
                mapped = x - source_r + maps[i][0]
            else:
                mapped = x
            result.append(mapped)
        print(result)


        #seeds = [x if x not in range(source_r, max_r) else (x - source_r + maps[i][0]) for x in seeds]



#maps [['50', '98', '2'], ['52', '50', '48'],
#check if seed number is in range(second_col, second_col + third_col)
#true: new_number = seed_number + (second_col - corresponding_range)
#false: pass to next line