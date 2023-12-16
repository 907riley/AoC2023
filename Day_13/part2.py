

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

        check_row = self.checkMatrix(matrix)
        if check_row != -1:
            return check_row * 100
        
        # now need to check cols
        transposition_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        return self.checkMatrix(transposition_matrix)

    def checkMatrix(self, matrix):

        for i in range(len(matrix)-1):
            if matrix[i] == matrix[i+1]:
                # now need to confirm, so go outwards
                top = i
                bot = i+1

                while matrix[top] == matrix[bot]:
                    top -= 1
                    bot += 1
                    if top < 0 or bot >= len(matrix):
                        return i+1
        return -1

def main():
    miro = MirrorMess("Day 13/input.txt")
    miro.parseFile()
    miro.computeAllMatrices()
    # print(miro.computeMatrix(4))
    print(miro.res)

if __name__ == "__main__":
    main()
