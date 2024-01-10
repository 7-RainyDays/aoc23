import re

possible = {'green': 13, 'blue': 14, 'red': 12}
solution = 0

def parse_input(line):
    parsed_line = line.split(":")
    title = parsed_line[0]
    games = parsed_line[1]

    parsed_games = [game.strip() for game in games.split(";")]

    match = re.search(r'\d+', title)
    game_id = int(match.group())
    return (game_id, parsed_games)

def validate_game(game):
    result = {color: int(amount) for draw in game.split(',') for amount, color in (draw.strip().split(" "),)}
    return all(result[key] <= possible[key] for key in result)

with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        valid = True
        game_id, games = parse_input(line)
        for game in games:
            valid = validate_game(game)
            if not valid:
                break
        if valid:
            solution += game_id

print(solution)

