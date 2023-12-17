from copy import deepcopy


def parseFile(file):
    matrix = []
    for line in file:
        matrix.append(line.strip())
    return ["".join([matrix[j][i] for j in range(len(matrix))]) for i in range(len(matrix[0]))]
# def transposeMatrix(self):
#     self.transpose_matrix = [[self.transpose_matrix[j][i] for j in range(len(self.transpose_matrix))] for i in range(len(self.transpose_matrix[0]))]

def runCycle(matrix):
    # Run the rotate and tilt four times for the full cycle
    for _ in range(4):
        matrix = rotate(moveAllRoundRocks(matrix))
    return matrix

def rotate(matrix):
    # Reverse all lines and return the columns to simulate a single rotation
    return [''.join(line) for line in zip(*map(reversed, matrix))]


def moveAllRoundRocks(matrix):
    # self.prettyPrint(self.transpose_matrix)
    new_matrix = deepcopy(matrix)
    for i in range(len(matrix)):
        line = ''.join(matrix[i]).split("#")  # Group up all O and . between each #
        line_copy = deepcopy(line)
        for idx, section in enumerate(line_copy):
            if section != '':
                line[idx] = ''.join(sorted(section, reverse=True))  # Sort the O and . reversed to put the rocks on the left
        new_matrix[i] = '#'.join(line)  # Rejoin the line with #s in between
    return new_matrix

def load(matrix):
    # for row in matrix:
    #     print(row)
    return sum(sum(i * (c == "O") for i, c in enumerate(col[::-1], 1)) for col in matrix)


def computeAllLoads(matrix) -> int:
    # self.prettyPrint(self.transpose_matrix)
    res = 0
    for i, val in enumerate(matrix):
        res += computeLoad(val)
    return res

def computeLoad(row) -> int:
    start = 0
    count = 0
    res = 0
    # print(row)
    for i, val in enumerate(row):
        if val == '#':
            for j in range(count):
                # print(f"adding {len(row)-start-j}")
                res += len(row)-start-j
            start = i+1
            count = 0
        elif val == 'O':
            count += 1
    if count:
        for j in range(count):
            res += len(row)-start-j
    return res

def prettyPrint(matrix):
    for row in matrix:
        print(''.join(row))
    print()

def main():
    file = open("Day_14/input.txt", 'r')
    matrix = parseFile(file)
    # for row in matrix:
    #     print(row)
    # prettyPrint(matrix)
    map_list = [matrix]
    prettyPrint(runCycle(matrix))
    cycles = 1_000_000_000
    counter = 0
    while True:
        matrix = runCycle(matrix)
        # for row in matrix:
        #     print(row)
        if matrix in map_list:  # If the cycle is already in the cycle list, you've found the loop
            loop_idx = map_list.index(matrix)  # Find the first looped map
            loop_len = counter + 1 - loop_idx  # Find the number of cycles between each loop
            print(f"After {counter} cycles, we found a loop starting from cycle {loop_idx} for {loop_len} cycles")
            break
        map_list.append(matrix)
        counter += 1
    for row in map_list[(cycles - loop_idx) % loop_len + loop_idx]:
        print(row)
    print((cycles - loop_idx) % loop_len + loop_idx)
    print(load(map_list[(cycles - loop_idx) % loop_len + loop_idx]))
    # prettyPrint(runCycle(matrix))

if __name__ == "__main__":
    main()