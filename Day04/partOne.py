def evaluate_card(winning_numbers, elf_numbers):
    counter = 0
    for number in winning_numbers:
        if number in elf_numbers:
            if counter == 0:
                counter = 1
            else:
                counter = counter*2
    return counter


with open('input.txt', 'r') as f:
    solution = 0
    lines = f.readlines()
    for line in lines:
        card = line.split(":")[1]
        card = card.split("|")

        card = [number.replace("  ", " ").strip() for number in card]

        winning_numbers = [number for number in card[0].split(" ")]
        elf_numbers = [number for number in card[1].split(" ")]

        win = evaluate_card(winning_numbers, elf_numbers)
        solution += win

    print(solution)