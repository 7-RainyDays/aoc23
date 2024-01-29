def sort_pack(pack):
    return (card_values[pack[0]], card_values[pack[1]], card_values[pack[2]], card_values[pack[3]], card_values[pack[4]])

with open('input.txt', 'r') as f:
    score = 0
    card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    lines = f.readlines()
    d = {parts[0]: int(parts[1]) for line in lines for parts in [line.strip().split(" ")]}
    l = [hand.strip() for round in lines for hand in [round.split(" ")[0]]]

    Five_ok = [element for element in l if len(set(element)) == 1]
    Five_ok = sorted(Five_ok, key=sort_pack, reverse=True)

    Four_ok = [element for element in l if any(element.count(x) == 4 for x in element)]
    Four_ok = sorted(Four_ok, key=sort_pack, reverse=True)

    Full_house = [element for element in l if any(element.count(x) == 2 for x in element) and any(element.count(x) == 3 for x in element)]
    Full_house = sorted(Full_house, key=sort_pack, reverse=True)

    Three_ok = [element for element in l if any(element.count(x) == 3 and len(set(element)) == 3 for x in element) ]
    Three_ok = sorted(Three_ok, key=sort_pack, reverse=True)

    Two_pair = [element for element in l if len(set(element)) == 3 and any(element.count(x) == 2 for x in element)]
    Two_pair = sorted(Two_pair, key=sort_pack, reverse=True)

    One_pair = [element for element in l if len(set(element)) == 4]
    One_pair = sorted(One_pair, key=sort_pack, reverse=True)

    High_card = [element for element in l if len(set(element)) == 5]
    High_card = sorted(High_card, key=sort_pack, reverse=True)

    combined_list = Five_ok + Four_ok + Full_house + Three_ok + Two_pair + One_pair + High_card

    for i in range(len(combined_list)):
        score += d[combined_list[i]] * (len(combined_list)-i)

    print(score)
