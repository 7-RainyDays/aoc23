from functools import reduce
import operator

solution = 0

def parse_input(line):
    parsed_line = line.split(":")
    games = parsed_line[1]
    parsed_games = [game.strip() for game in games.split(";")]
    return (parsed_games)

def find_greatest_amount(game):
    return {color: int(amount) for draw in game.split(',') for amount, color in (draw.strip().split(" "),)}

with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        games = parse_input(line)
        minimum = {'green': 1, 'red': 1, 'blue': 1}
        for game in games:
            greatest = find_greatest_amount(game)
            for key in greatest.keys():
                if minimum[key] < greatest[key]:
                    minimum[key] = greatest[key]
        val = minimum.values()
        solution+= (reduce(operator.mul,val, 1))

print(solution)

70950