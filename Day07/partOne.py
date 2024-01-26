import re

def apply_value(keys):
    print("entering")
    return

with open('input.txt', 'r') as f:
    lines = f.readlines()
    d = {parts[0]: parts[1] for line in lines for parts in [line.strip().split(" ")]}
    #'{key: value for key, value in zip(keys, values)}

    sorted(dict(d.keys(), key=apply_value))
    print(d)