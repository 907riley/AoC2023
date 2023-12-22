
def main():
    filename = "Day_18/small_input.txt"
    print("**** PART 1 ANSWER ****")
    file = open(filename, 'r')
    instructions = []
    for line in file:
        instructions.append(line.strip().split(' '))
    print(instructions)
    width_max, width_min = 0, 0
    height_max, height_min = 0, 0

    cur_width = 0
    cur_height = 0
    for dir, amount, color in instructions:
        amount = int(amount)
        if dir == 'U':
            cur_height -= amount
        elif dir == 'D':
            cur_height += amount
        elif dir == 'R':
            cur_width += amount
        elif dir == 'L':
            cur_width -= amount
        width_max = max(cur_width, width_max)
        width_min = min(cur_width, width_min)
        height_max = max(cur_height, height_max)
        height_min = min(cur_height, height_min)
    print(width_max, width_min, height_max, height_min)

    matrix = [['' for _ in range(width_max-width_min+1)] for _ in range(height_max-height_min+1)]
    cur = [abs(width_min), abs(height_min)]

    for dir, amount, color in instructions:
        for i in range(int(amount)):
            if dir == 'R':
                cur[0] += 1
            elif dir == 'L':
                cur[0] -= 1
            elif dir == 'U':
                cur[1] -= 1
            elif dir == 'D':
                cur[1] += 1
            # print(cur[0], cur[1])
            matrix[cur[1]][cur[0]] = color
    res = 0
    for row in matrix:
        i = 1
        print("new row")
        while i < len(row):
            if row[i-1] != '' and row[i] == '':
                while row[i] == '':
                    print(" . ", end='')
                    res += 1
                    i += 1
                res += 2
            # need to add all the non empty spaces for perim
            i += 1


    for row in matrix:
        print(row)
    print(res)



if __name__ == "__main__":
    main()
