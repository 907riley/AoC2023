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

    mins = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    for val in game_split:
        counter_split = val.split(',')
        # print(counter_split)
        for count in counter_split:
            for color in colors:
                single_hand = count.split(' ')
                if color in single_hand[2]:
                    mins[color] = max(int(single_hand[1]), mins[color])
    product = 1
    for color in colors:
        product *= mins[color]
    res += product
print(res)

