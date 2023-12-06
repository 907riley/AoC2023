
class BoatRacer:

    def __init__(self, filename) -> None:
        self.file = open(filename, 'r')
        self.time = 0
        self.record = 0
        self.res = 0
    
    def parseFile(self) -> None:
        self.time = int("".join([x for x in self.file.readline().split(':')[1].strip().split(" ") if x.isdigit()]))
        self.record = int("".join([x for x in self.file.readline().split(':')[1].strip().split(" ") if x.isdigit()]))
    
    # optimized binary search implementation to find the point we start winning
    def computePossibleWins(self) -> None:
        left = 0
        right = self.time//2
        mid = 0

        while(left <= right):
            mid = (right+left) // 2
            holding_time = self.time-mid # 39,741,414
            running_time = self.time-holding_time # 5,085,567
            if running_time*holding_time > self.record: # 202,107,623,571,738
                right = mid -1
            else:
                left = mid + 1

        self.res = self.time - left*2 + 1




def main():
    boat = BoatRacer("Day 6/input.txt")
    # wrong 34655847
    # correct 34655848 lol
    boat.parseFile()
    boat.computePossibleWins()
    print(f"Boat time {boat.time}")
    print(f"Record to beat {boat.record}")
    print(f"Possible wins {boat.res}")
    # expected result for small_input is 71503


if __name__ == "__main__":
    main()
