def sort_pack(pack):
    return (card_values[pack[0]], card_values[pack[1]], card_values[pack[2]], card_values[pack[3]], card_values[pack[4]])

with open('input.txt', 'r') as f:
    score = 0
    card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    lines = f.readlines()
    d = {parts[0]: int(parts[1]) for line in lines for parts in [line.strip().split(" ")]}
    l = [hand.strip() for round in lines for hand in [round.split(" ")[0]]]

    Five_ok = [element for element in l if len(set(element)) == 1]
    Four_ok = [element for element in l if any(element.count(x) == 4 for x in element)]
    Full_house = [element for element in l if any(element.count(x) == 2 for x in element) and any(element.count(x) == 3 for x in element)]
    Three_ok = [element for element in l if any(element.count(x) == 3 and len(set(element)) == 3 for x in element) ]
    Two_pair = [element for element in l if len(set(element)) == 3 and any(element.count(x) == 2 for x in element)]
    One_pair = [element for element in l if len(set(element)) == 4]
    High_card = [element for element in l if len(set(element)) == 5]

    all_poker_hands = [Five_ok, Four_ok, Full_house, Three_ok, Two_pair, One_pair, High_card]
    sorted_hands = [sorted(poker_hand, key=sort_pack, reverse=True) for poker_hand in all_poker_hands]

    combined_list = []
    for poker_hand in sorted_hands:
        combined_list.extend(poker_hand)

    for i in range(len(combined_list)):
        score += d[combined_list[i]] * (len(combined_list)-i)

    print(score)