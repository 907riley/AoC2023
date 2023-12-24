from collections import deque

def floodFill(matrix, start) -> int:
    visited = set()
    queue = deque([start])
    while queue:
        i, j = queue.popleft()
        # print(queue, matrix, i, j)

        if matrix[i][j] == '#' or (i, j) in visited:
            continue

        for dir in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            queue.append((i+dir[0], j+dir[1]))
        visited.add((i, j))
    # print(visited)
    return len(visited)
    

# part 1 32116 to low
def main():
    filename = "Day_18/input.txt"
    print("**** PART 1 ANSWER ****")
    file = open(filename, 'r')
    instructions = []
    for line in file:
        instructions.append(line.strip().split(' '))
    # print(instructions)
    width_max, width_min = 0, 0
    height_max, height_min = 0, 0

    cur_width = 0
    cur_height = 0
    perimeter = 0
    for dir, amount, color in instructions:
        amount = int(amount)
        perimeter += amount
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
    # print(width_max, width_min, height_max, height_min)

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
            matrix[cur[1]][cur[0]] = '#'

    file_out = open('Day_18/out.txt', 'w')
    matrix_visual = [''.join([x if x == '#' else '.' for x in row] + ['\n']) for row in matrix]
    file_out.writelines(matrix_visual)
    
    res = 0
    # need to do a flood fill probably
    start = 0
    for i in range(1, len(matrix[0])):
        if matrix[1][i] == '' and matrix[1][i-1] != '':
            start = i
            break

    # print(f"start 1 {start}")

    res = floodFill(matrix, (1, start))
    # print(res)
    # for row in matrix:
    #     print(row)
    print(res + perimeter)



if __name__ == "__main__":
    main()
