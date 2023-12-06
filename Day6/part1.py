
class BoatRacer:

    def __init__(self, filename) -> None:
        self.file = open(filename, 'r')
        self.times = []
        self.records = []
        self.possible_wins = []
        self.res = 1
    
    def parseFile(self) -> None:
        self.times = [int(x) for x in self.file.readline().split(':')[1].strip().split(" ") if x.isdigit()]
        self.records = [int(x) for x in self.file.readline().split(':')[1].strip().split(" ") if x.isdigit()]
    
    def computePossibleWins(self) -> None:
        # iterate over all time/record pairs
        for i in range(len(self.times)):
            wins = 0
            for j in range(self.times[i]):
                holding_time = self.times[i]-j
                running_time = self.times[i]-holding_time
                if running_time*holding_time > self.records[i]:
                    wins += 1
            self.possible_wins.append(wins)
        for val in self.possible_wins:
            self.res *= val



def main():
    boat = BoatRacer("Day 6/input.txt")
    boat.parseFile()
    boat.computePossibleWins()
    print(boat.times)
    print(boat.records)
    print(boat.res)
    # expected result for small_input is 288
    # 4 * 8 * 9


if __name__ == "__main__":
    main()
