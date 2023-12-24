import collections

class PipeTraversal:

    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.start = []
        self.matrix = []
        self.n = 0
        self.m = 0
        self.res = 0

    def parseFile(self):
        for i, line in enumerate(self.file):
            new_row = []
            for j, char in enumerate(line.strip()):
                new_row.append(char)
                if char == "S":
                    self.start = (i, j)
            self.matrix.append(new_row)
        self.n = len(self.matrix)
        self.m = len(self.matrix[0])
        self.areas = []
        self.all_visited_pipes = set()
        # print(self.matrix, self.start)
    
    """
    | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    . is ground; there is no pipe in this tile.
    S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

    UP
        |
        7
        F
    RIGHT
        -
        J
        7
    DOWN
        |
        L
        J
    LEFT
        -
        L
        F
    """
    def traversePipes(self):
        vert_moves = 0
        horiz_moves = 0
        visited = set()
        queue = collections.deque([(self.start, 0)])

        while queue:
            cur = queue.popleft()
            i, j, cur_steps = cur[0][0], cur[0][1], cur[1]
            # print(self.matrix[i][j], cur)
            cur_char = self.matrix[i][j]

            # if cur_steps > self.res:
            #     self.res = cur_steps

            # Look up
            if i-1 >= 0 and (cur_char == 'S' or cur_char == '|' or cur_char == 'J' or cur_char == 'L') and (i-1, j) not in visited:
                check_up = self.matrix[i-1][j]
                if check_up == '|' or check_up == '7' or check_up == 'F':
                    print(f"pos vert {i, j} {cur_char}")
                    vert_moves += 1
                    queue.append(((i-1, j), cur_steps+1))

            # look right
            if j+1 < self.m and (i, j+1) not in visited and (cur_char == 'S' or cur_char == '-' or cur_char == 'L' or cur_char == 'F'):
                check_right = self.matrix[i][j+1]
                if check_right == '-' or check_right == 'J' or check_right == '7':
                    print(f"pos horiz {i, j} {cur_char}")
                    horiz_moves += 1
                    queue.append(((i, j+1), cur_steps+1))

            # look down
            if i+1 < self.n and (i+1, j) not in visited and (cur_char == 'S' or cur_char == '|' or cur_char == '7' or cur_char == 'F'):
                check_down = self.matrix[i+1][j]
                if check_down == '|' or check_down == 'L' or check_down == 'J':
                    print(f"neg vert{i, j} {cur_char}")
                    vert_moves -= 1
                    queue.append(((i+1, j), cur_steps+1))

            # look left
            if j-1 >= 0 and (i, j-1) not in visited and (cur_char == 'S' or cur_char == '-' or cur_char == 'J' or cur_char == '7'):
                check_left = self.matrix[i][j-1]
                if check_left == '-' or check_left == 'L' or check_left == 'F':
                    horiz_moves -= 1
                    print(f"neg horiz {i, j} {cur_char}")
                    queue.append(((i, j-1), cur_steps+1))

            # self.matrix[i][j] = '$'
            visited.add((i, j))
        self.all_visited_pipes = visited
        # for row in self.matrix:
            # print(row)
        # print(abs(vert_moves), abs(horiz_moves))

    def findSurrounded(self):
        for y, row in enumerate(self.matrix):
            for x, char in enumerate(row):
                if (y,x) in self.all_visited_pipes:
                    continue
                    
                crosses = 0
                x2,y2 = x,y

                while x2 < len(self.matrix[0]) and y2 < len(self.matrix):
                    c2 = self.matrix[y2][x2]
                    if (y2, x2) in self.all_visited_pipes and c2 != "L" and c2 != "7":
                        crosses += 1
                    x2 += 1
                    y2 += 1


                if crosses % 2 == 1:
                    self.res += 1




        

def main():
    pipes = PipeTraversal('Day10/input.txt')
    pipes.parseFile()
    pipes.traversePipes()
    pipes.findSurrounded()
    print(pipes.res)


if __name__ == "__main__":
    main()