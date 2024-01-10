solution = 0

def evaluate_cards(arr):
    # assign the amount of all cards related to the winning range
    for j in range(0, len(arr)+1):
        try:
            amount = arr[j][0]
            win = arr[j][1]
            for i in range(j+1, j+win+1):
                    arr[i][0] += amount
        except IndexError:
            continue
    return arr

with open('input.txt', 'r') as f:
    card_values = []

    lines = f.readlines()
    for line in lines:
        card = line.split(":")[1]
        card = card.split("|")

        card = [number.replace("  ", " ").strip() for number in card]

        winning_numbers = [number for number in card[0].split(" ")]
        elf_numbers = [number for number in card[1].split(" ")]

        #extract the winning value of each card
        card = [number for number in winning_numbers if number in elf_numbers]
        card_values.append(len(card))

    #translate the input to [[card_amount, winning_number] , ..]
    # [[1, 10], [1, 10], [1, 1], [1, 1], [1, 2], [1, 3], [1, 10]]

    arr = [list(a) for a in zip([1] * 196, card_values)]

    arr = evaluate_cards(arr)

    for a, b in arr:
        solution += a

    print(solution)