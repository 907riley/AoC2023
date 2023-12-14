"""
Intuition

This is definetly a trickier problem it seems like, but I think a bit of recursion is what is needed
So for each line you have to find where to place the correct groupings
But you run into cases where one grouping can go in n places and then the next grouping can go in n-1 ...

So I think one way to do this is start with the first grouping,
find all the places where it can go
for each of these, find all the places where the next group can go, assuming you've places the previous, repeat
When there are no more groups to places, return the product of the nested possiblities for the first starting position

That way if you place the first and second, but the third cant go anywhere x * x1 * 0 will be 0 which is correct as all 
because that last one can't go anywhere. Also if a group can't be placed, there is no need to continue checking future positions

"""
import collections

class HotSpringRecords:

    def __init__(self, filename) -> None:
        self.file = open(filename, 'r')
        self.record_count_pairs = []
        self.res = 0

    def parseFile(self):
        for line in self.file:
            records, count_string = line.strip().split(" ")
            self.record_count_pairs.append([records, collections.deque(count_string.split(','))])
            # print(self.record_count_pairs)

    def computeAllPossibleLines(self):
        for i in range(len(self.record_count_pairs)):
            records, counts = self.record_count_pairs[i]
            # print(records, counts)
            testt = self.computePossibleLine(records, collections.deque([x for x in counts]))
            # print(testt, records, counts)
            self.res += testt
        # records, counts = self.record_count_pairs[5]
        # print(self.computePossibleLine(records, collections.deque([x for x in counts])))

    def computePossibleLine(self, records, counts):
        print(f"In recurse {records} {counts}")
        # if there is nothing left in counts
        # then we have covered all the groups so stop looking
        if not counts and '#' in records:
            return 0
        elif not counts:
            return 1
        # need to keep track of all the possibilites for a group
        start_total = 0
        cur_count = int(counts.popleft())
        # iterate over substrings
        for i in range(len(records)-cur_count+1):
            sub_check = records[0+i:i+cur_count]
            print(f"Checking substr {sub_check} for {records}")
            # check that all are ? or # and that we aren't braking a string of #
            # also if are any '#' then stop and we can only have this one
            if sub_check[0] == '#' and ('.'  in sub_check or (i+cur_count < len(records) and records[i+cur_count] == '#')):
                # start_total += self.computePossibleLine(records[i+cur_count+1:], collections.deque([x for x in counts]))
                print(f"Break {cur_count} child poss {start_total}")
                break
            elif sub_check[0] == '#' and ('.'  in sub_check or (i+cur_count >= len(records) or records[i+cur_count] != '#')):
                start_total += self.computePossibleLine(records[i+cur_count+1:], collections.deque([x for x in counts]))
                break
            elif '.' not in sub_check and (i+cur_count >= len(records) or records[i+cur_count] != '#'):
                val = self.computePossibleLine(records[i+cur_count+1:], collections.deque([x for x in counts]))
                # if val == 0:
                #     break
                start_total += val
                print(f"{cur_count} child poss {start_total}")
        return start_total


def main():
    broke_records = HotSpringRecords("Day 12/input.txt")
    broke_records.parseFile()
    broke_records.computeAllPossibleLines()
    print(broke_records.res)


if __name__ == "__main__":
    main()
