

class MirrorMess:

    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.matrices = []
        self.res = 0
    
    def parseFile(self):
        new_matrix = []
        for line in self.file:
            if line == '\n':
                self.matrices.append(new_matrix)
                new_matrix = []
            else:
                new_matrix.append(line.strip())
        self.matrices.append(new_matrix)
        
        # for matrix in self.matrices:
        #     for line in matrix:
        #         print(line)
        #     print()
    
    def computeAllMatrices(self):
        for i in range(len(self.matrices)):
            self.res += self.computeMatrix(i)
    
    """
    First look for a mirror on the rows
    """
    def computeMatrix(self, index):
        
        matrix = self.matrices[index]

        # print(f"checking rows")
        check_row = self.checkMatrix(matrix)
        if check_row != -1:
            return check_row * 100
        
        # print(f"checking cols")
        # now need to check cols
        transposition_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        return self.checkMatrix(transposition_matrix)

    def checkMatrix(self, matrix):
        for i in range(len(matrix)-1):
            misses_allowed = 1
            inner_matching, inner_misses = self.rowChecker(matrix[i], matrix[i+1])
            misses_allowed -= inner_misses
            if inner_matching:
                # print(f"found a match with {misses_allowed} left, with {matrix[i]} and {matrix[i+1]}")
                # now need to confirm, so go outwards
                top = i
                bot = i+1

                while inner_matching and misses_allowed >= 0:
                    top -= 1
                    bot += 1
                    if misses_allowed == 0 and (top < 0 or bot >= len(matrix)):
                        # print("one off match found")
                        return i+1
                    elif top < 0 or bot >= len(matrix):
                        # print("not a good match")
                        break
                    inner_matching, inner_misses = self.rowChecker(matrix[top], matrix[bot])
                    misses_allowed -= inner_misses
        return -1

    def rowChecker(self, row1, row2):
        miss_alligned = 0
        for i in range(len(row1)):
            if row1[i] != row2[i]:
                miss_alligned += 1

        # print(row1, row2, miss_alligned)
        if miss_alligned > 1:
            return [False, -1]
        return [True, miss_alligned]


def main():
    miro = MirrorMess("Day_13/input.txt")
    miro.parseFile()
    miro.computeAllMatrices()
    # print(miro.computeMatrix(4))
    print(miro.res)

if __name__ == "__main__":
    main()
