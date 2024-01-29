def sort_pack(pack):
    return (card_values[pack[0]], card_values[pack[1]], card_values[pack[2]], card_values[pack[3]], card_values[pack[4]])

with open('input.txt', 'r') as f:
    score = 0
    card_values = {'J': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'Q': 12, 'K': 13, 'A': 14}

    lines = f.readlines()
    d = {parts[0]: int(parts[1]) for line in lines for parts in [line.strip().split(" ")]}
    l = [hand.strip() for round in lines for hand in [round.split(" ")[0]]]

    Five_ok, Four_ok, Full_house, Three_ok, Two_pair, One_pair, High_card = [],[],[],[],[],[],[]

    for element in l:
        #search for five of a kind
        if len(set(element)) == 1:
            Five_ok.append(element)

        #search for four of a kind
        elif any(element.count(x) == 4 for x in element) and "J" not in element:
            Four_ok.append(element)
        elif (element.count('J') >= 1) and len(set(element)) == 2:
            Five_ok.append(element)

        #search for full house
        elif any(element.count(x) == 3 for x in element) and any(element.count(x) == 2 for x in element) and "J" in element:
            Five_ok.append(element)
        elif any(element.count(x) == 3 for x in element) and any(element.count(x) == 2 for x in element) and "J" not in element:
            Full_house.append(element)

        #search for three of a kind
        elif any(element.count(x) == 3 and len(set(element)) == 3 for x in element) and "J" not in element:
            Three_ok.append(element)
        elif any(element.count(x) == 3 and len(set(element)) == 3 for x in element) and "J" in element:
            Four_ok.append(element)

        #search for two pair
        elif len(set(element)) == 3 and any(element.count(x) == 2 for x in element):
            if "J" not in element:
                Two_pair.append(element)
            elif "J" in element:
                if element.count('J') == 2:
                    Four_ok.append(element)
                elif element.count('J') == 1:
                    Full_house.append(element)

        #search for one pair
        elif len(set(element)) == 4 and "J" not in element:
            One_pair.append(element)
        elif len(set(element)) == 4 and "J" in element:
            Three_ok.append(element)

        #search for high card
        elif len(set(element)) == 5:
            if "J" not in element:
                High_card.append(element)
            elif "J" in element:
                One_pair.append(element)
        else:
            print("could not assign:", element)

    Five_ok = sorted(Five_ok, key=sort_pack, reverse=True)
    Four_ok = sorted(Four_ok, key=sort_pack, reverse=True)
    Full_house = sorted(Full_house, key=sort_pack, reverse=True)
    Three_ok = sorted(Three_ok, key=sort_pack, reverse=True)
    Two_pair = sorted(Two_pair, key=sort_pack, reverse=True)
    One_pair = sorted(One_pair, key=sort_pack, reverse=True)
    High_card = sorted(High_card, key=sort_pack, reverse=True)

    combined_list = Five_ok + Four_ok + Full_house + Three_ok + Two_pair + One_pair + High_card


    for i in range(len(combined_list)):
        score += d[combined_list[i]] * (len(combined_list)-i)

    print(score)
