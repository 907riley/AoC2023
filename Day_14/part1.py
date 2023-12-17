class RockSlide():

    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.res = 0
        self.matrix = []
        self.transpose_matrix = []

    def parseFile(self):
        for line in self.file:
            self.matrix.append(line.strip())

        self.transpose_matrix = [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]
        # print(self.matrix)
        # print(self.transpose_matrix)

    def computeAllLoads(self):
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

def main():
    riock = RockSlide("Day_14/input.txt")
    riock.parseFile()
    riock.computeAllLoads()
    print(riock.res)

if __name__ == "__main__":
    main()