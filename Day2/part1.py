file = open("input.txt", 'r')

res = 0
bounds = {
    'red': 12,
    'green': 13,
    'blue': 14
}

colors = ['red', 'blue', 'green']

for line in file:
    print(line)

    line_split = line.split(':')
    game_split = line_split[1].split(';')
    good = True

    for val in game_split:
        counter_split = val.split(',')
        # print(counter_split)
        for count in counter_split:
            for color in colors:
                single_hand = count.split(' ')
                if line_split[0].split(' ')[-1] == "56":
                    print(single_hand)
                if color in single_hand[2] and int(single_hand[1]) > bounds[color]:
                    print(f"Bad: {color} {count.split(' ')} > {bounds[color]}")
                    good = False
    if good:
        print(f"Good line adding {line_split[0].split(' ')[-1]}")
        res += int(line_split[0].split(' ')[-1])
        
print(res)

