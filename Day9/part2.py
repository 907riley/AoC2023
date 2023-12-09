
class OasisHistory:
    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.histories = []
        self.extrapolated_values = {}
        self.res = 0

    def parseFile(self):
        for line in self.file:
            self.histories.append([int(x) for x in line.strip().split(' ')])
    
    def computeHistories(self):
        for i in range(len(self.histories)):
            new_values = []
            new_values.append(self.histories[i])
            flag = False

            cur_row = self.histories[i]
            while not flag:
                flag = True
                new_row = []
                for j in range(1, len(cur_row)):
                    diff = cur_row[j] - cur_row[j-1]

                    new_row.append(diff)
                    if diff != 0:
                        flag = False
                cur_row = new_row
                new_values.append(new_row)
            # print(new_values)
            self.extrapolated_values[i] = new_values
    
    def extrapolateHistories(self):
        for i in range(len(self.histories)):
            history_list = self.extrapolated_values[i]
            cur_res = 0
            for j in range(len(history_list)-2, -1, -1):
                cur_res = history_list[j][0] - cur_res
            self.res += cur_res


def main():
    oasis = OasisHistory("Day9/input.txt")
    oasis.parseFile()
    oasis.computeHistories()
    oasis.extrapolateHistories()
    print(oasis.res)

if __name__ == "__main__":
    main()