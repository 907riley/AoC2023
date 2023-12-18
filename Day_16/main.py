"""
Intuition

Seems like a maze traversal problem where you right from the upper left until
    you hit a char that is not a '.', change direction accordingly
    you try to go out of bounds, stop traversing there

Because of the splitters, we need to be able to handle traversing multiple paths at once,
so I a DFS aglorithm would be best. This also gives us the added benefit of being able to end a path
early because if we come to a path that has been visited before AND we are heading the same direction,
we can stop traversing there

Directions are
    l left j--
    r right j++
    u up i--
    d down i++
"""

def parseFileIntoMatrix(file):
    matrix = []
    for line in file:
        matrix.append(line.strip())
    return matrix

def getNextMoves(i, j, direction, matrix):
    cur_symbol = matrix[i][j]

    # 90 degree turn
    if cur_symbol == '\\':
        # go left
        if direction == 'u':
            return [(i, j-1, 'l')]
        # go right
        elif direction == 'd':
            return [(i, j+1, 'r')]
        # go down
        elif direction == 'r':
            return [(i+1, j, 'd')]
        # go up
        elif direction == 'l':
            return [(i-1, j, 'u')]
    # 90 degree turn
    elif cur_symbol == '/':
        # go right
        if direction == 'u':
            return [(i, j+1, 'r')]
        # go left
        elif direction == 'd':
            return [(i, j-1, 'l')]
        # go up
        elif direction == 'r':
            return [(i-1, j, 'u')]
        # go down
        elif direction == 'l':
            return [(i+1, j, 'd')]
    # nothing or split both 90
    elif cur_symbol == '|':
        # go up
        if direction == 'u':
            return [(i-1, j, 'u')]
        # go down
        elif direction == 'd':
            return [(i+1, j, 'd')]
        # go up AND go down
        elif direction == 'r':
            return [(i+1, j, 'd'), (i-1, j, 'u')]
        # go up AND go down
        elif direction == 'l':
            return [(i+1, j, 'd'), (i-1, j, 'u')]
    # nothing or split both 90
    elif cur_symbol == '-':
        # go right AND go left
        if direction == 'u':
            return [(i, j-1, 'l'), (i, j+1, 'r')]
        # go right AND go left
        elif direction == 'd':
            return [(i, j-1, 'l'), (i, j+1, 'r')]
        # go right
        elif direction == 'r':
            return [(i, j+1, 'r')]
        # go left
        elif direction == 'l':
            return [(i, j-1, 'l')]
    # just continue on
    elif cur_symbol == '.':
        # go left
        if direction == 'l':
            return [(i, j-1, 'l')]
        # go right
        elif direction == 'r':
            return [(i, j+1, 'r')]
        # go down
        elif direction == 'd':
            return [(i+1, j, 'd')]
        # go up
        elif direction == 'u':
            return [(i-1, j, 'u')]
    return [-1]

def main():
    filename = "Day_16/input.txt"
    print("**************** PART 1 ANSWER ****************")
    file = open(filename, 'r')
    matrix = parseFileIntoMatrix(file)
    visited = [[0 for _ in range(len(row))] for row in matrix]

    stack = [(0, 0, 'r')]

    while stack:
        i, j, direction = stack.pop()

        # kill this path
        if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or visited[i][j] == direction:
            continue

        cur_symbol = matrix[i][j]
        visited[i][j] = direction

        # get the next moves onto the stack
        for val in getNextMoves(i, j, direction, matrix):
            if val == -1: print("ERROR")
            stack.append(val)
    # compute the answer by checking the visited indices that are filled
    res = 0
    for row in visited:
        for char in row:
            if char != 0:
                res += 1
    print(res)

    print("**************** PART 2 ANSWER ****************")
    file = open(filename, 'r')
    matrix = parseFileIntoMatrix(file)
    res_max = float("-inf")

    n = len(matrix)
    m = len(matrix[0])
    starting_vals = []
    # add top row
    for val in [(0, j, 'd') for j in range(m)]:
        starting_vals.append(val) 
    # add bottom row
    for val in [(n-1, j, 'u') for j in range(m)]:
        starting_vals.append(val) 
    # add left col
    for val in [(i, 0, 'r') for i in range(n)]:
        starting_vals.append(val) 
    # add right col
    for val in [(i, m-1, 'l') for i in range(n)]:
        starting_vals.append(val) 

    for starting_val in starting_vals:
        visited = [[0 for _ in range(len(row))] for row in matrix]

        stack = [starting_val]

        while stack:
            i, j, direction = stack.pop()

            # kill this path
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or visited[i][j] == direction:
                continue

            cur_symbol = matrix[i][j]
            visited[i][j] = direction

            # get the next moves onto the stack
            for val in getNextMoves(i, j, direction, matrix):
                if val == -1: print("ERROR")
                stack.append(val)
        # compute the answer by checking the visited indices that are filled
        res = 0
        for row in visited:
            for char in row:
                if char != 0:
                    res += 1
        if res > res_max:
            res_max = res
    print(res_max)





if __name__ == "__main__":
    main()
