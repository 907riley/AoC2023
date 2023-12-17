from copy import deepcopy

class RockSlide():

    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.res = 0
        self.seen = []
        self.matrix = []
        self.transpose_matrix = []

    def parseFile(self):
        for line in self.file:
            self.matrix.append(line.strip())
        self.transpose_matrix = [[x for x in row] for row in self.matrix]
        # self.seen.append(self.matrix)
        # self.transpose_matrix = [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]
        # print(self.matrix)
        # print(self.transpose_matrix)
    
    # def runCycle(self, p):
    #     found = False
    #     i = 0
    #     while p > i and not found:
    #         transposed = [[self.transpose_matrix[j][i] for j in range(len(self.transpose_matrix))] for i in range(len(self.transpose_matrix[0]))]
    #         for q in range(4):
    #             if q == 0:
    #                 self.transpose_matrix = [[ x for x in row] for row in transposed]
    #             elif q == 1:
    #                 self.transposeMatrix()
    #             elif q == 2:
    #                 self.transposeMatrix()
    #                 for i in range(len(self.transpose_matrix)):
    #                     self.transpose_matrix[i] = self.transpose_matrix[i][::-1]
    #             elif q == 3:
    #                 self.transposeMatrix()
    #                 for i in range(len(self.transpose_matrix)):
    #                     self.transpose_matrix[i] = self.transpose_matrix[i][::-1]
    #             self.moveAllRoundRocks()
    #             # print(q, "after this many here with this")
    #             # for row in self.transpose_matrix:
    #             #     print(row)
    #         for k in range(len(self.transpose_matrix)):
    #             self.transpose_matrix[k] = self.transpose_matrix[k][::-1]
    #         self.transpose_matrix = self.transpose_matrix[::-1]

    #         if self.transpose_matrix in self.seen:
    #             loop_idx = self.seen.index(self.transpose_matrix)  # Find the first looped map
    #             loop_len = i + 1 - loop_idx  # Find the number of cycles between each loop
    #             print(f"found at {loop_idx} with len {loop_len}")  
    #             index = (p - loop_idx) % loop_len + loop_idx + 1
    #             print(index)
    #             found = True
    #             self.transpose_matrix = self.seen[index]
    #         if not found:
    #             # print(self.seen)
    #             self.seen.append(self.transpose_matrix)
    #             # print(self.seen)
    #         i += 1
    #     # print("out of here")

    
    # def transposeMatrix(self):
    #     self.transpose_matrix = [[self.transpose_matrix[j][i] for j in range(len(self.transpose_matrix))] for i in range(len(self.transpose_matrix[0]))]
    
    def runCycle(self):
        # Run the rotate and tilt four times for the full cycle
        for _ in range(4):
            self.rotate()

    def rotate(self):
        # Reverse all lines and return the columns to simulate a single rotation
        self.transpose_matrix = [''.join(line) for line in zip(*map(reversed, self.transpose_matrix))]
        self.moveAllRoundRocks()


    def moveAllRoundRocks(self):
        # self.prettyPrint(self.transpose_matrix)
        for i in range(len(self.transpose_matrix)):
            self.moveRoundRocks(i)
        # print()
        # self.prettyPrint(self.transpose_matrix)
        # print()


    def moveRoundRocks(self, q):
        line = self.transpose_matrix[q]
        line = ''.join(line).split("#")  # Group up all O and . between each #
        line_copy = deepcopy(line)
        for idx, section in enumerate(line_copy):
            if section != '':
                line[idx] = ''.join(sorted(section, reverse=True))  # Sort the O and . reversed to put the rocks on the left
        self.transpose_matrix[q] = '#'.join(line)  # Rejoin the line with #s in between
        # print(self.transpose_matrix[q])


    def computeAllLoads(self):
        self.prettyPrint(self.transpose_matrix)
        for i, val in enumerate(self.transpose_matrix):
            self.res += self.computeLoad(val)

    def computeLoad(self, row):
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
                # print(f"adding {len(row)-start-j}")
                res += len(row)-start-j
        # print(f"Total {res}")
        return res

    def prettyPrint(self, matrix):
        for row in matrix:
            print(''.join(row))

def main():
    riock = RockSlide("Day_14/small_input.txt")
    riock.parseFile()
    # riock.prettyPrint(riock.transpose_matrix)
    # riock.moveAllRoundRocks()
    counter = 0
    while True:
        riock.runCycle()
        if riock.transpose_matrix in riock.seen:  # If the cycle is already in the cycle list, you've found the loop
            loop_idx = riock.seen.index(riock.transpose_matrix)  # Find the first looped map
            loop_len = counter + 1 - loop_idx  # Find the number of cycles between each loop
            print(f"After {counter} cycles, we found a loop starting from cycle {loop_idx} for {loop_len} cycles")
            break
        riock.seen.append(riock.transpose_matrix)
        counter += 1
    print((1_000_000_000 - loop_idx) % loop_len + loop_idx)
    riock.transpose_matrix = riock.seen[(1_000_000_000 - loop_idx) % loop_len + loop_idx]
    print()
    # riock.prettyPrint(riock.transpose_matrix)
    riock.computeAllLoads()
    print(riock.res)

if __name__ == "__main__":
    main()