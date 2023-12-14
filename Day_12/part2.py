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

We're gonna attempt this without changing our math lol

That did not work. I know there is some combinatorics thing here but I don't know how to implement

Guess and Check method?
Get the positions that have questions for each line, find the number of ones you need to convert, create a guess for 
each possible arrangement, check it

2 hours later....

That was even worse then my recursive implementation!
I did just realize that we are repeating a lot of calculations when, so I think this is a DP problem
I'm gong to try to implement some memoization, so if we've already computed the possible configurations of
a group count starting at a certain record index, we can just grab it
"""
import collections
import itertools

class HotSpringRecords:

    def __init__(self, filename) -> None:
        self.file = open(filename, 'r')
        self.record_count_pairs = []
        self.res = 0

    def parseFile(self):
        for line in self.file:
            records, count_string = line.strip().split(" ")
            self.record_count_pairs.append([records, collections.deque([int(x) for x in count_string.split(',')])])
            # print(self.record_count_pairs)
    
    def uncoilRecords(self):
        for i in range(len(self.record_count_pairs)):
            # print(self.record_count_pairs[i])
            new_record = ""
            for _ in range(4):
                new_record += self.record_count_pairs[i][0] + '?'
            new_record += self.record_count_pairs[i][0]

            self.record_count_pairs[i] = [new_record, self.record_count_pairs[i][1]*5]
            # print(self.record_count_pairs[i])


    def computeAllPossibleLines(self):
        for i in range(len(self.record_count_pairs)):
            records, counts = self.record_count_pairs[i]
            # print(records, counts)
            dp = [[-1 for _ in records] for _ in counts]
            # print(dp)
            testt = self.computePossibleLine(records, 0, counts, 0, dp)
            # print(testt, records, counts)
            self.res += testt
        # records, counts = self.record_count_pairs[5]
        # print(self.computePossibleLine(records, collections.deque([x for x in counts])))

    def computePossibleLine(self, records, records_index, counts, counts_index, dp):
        print(f"In recurse {records} {counts}")
        print(dp)
        # if there is nothing left in counts
        # then we have covered all the groups so stop looking
        cur_records = records[records_index:]
        if counts_index >= len(counts) and '#' in cur_records:
            return 0
        elif counts_index >= len(counts):
            return 1
        # need to keep track of all the possibilites for a group
        start_total = 0
        cur_count = counts[counts_index]
        # iterate over substrings
        for i in range(len(cur_records)-cur_count+1):
            sub_check = cur_records[i:i+cur_count]
            print(f"Checking substr {sub_check} for {records}")
            # check that all are ? or # and that we aren't braking a string of #
            # also if are any '#' then stop and we can only have this one
            if sub_check[0] == '#' and ('.'  in sub_check or (i+cur_count < len(cur_records) and cur_records[i+cur_count] == '#')):
                # start_total += self.computePossibleLine(records[i+cur_count+1:], collections.deque([x for x in counts]))
                print(f"Break {cur_count} child poss {start_total}")
                break
            elif sub_check[0] == '#' and ('.'  in sub_check or (i+cur_count >= len(cur_records) or cur_records[i+cur_count] != '#')):
                if dp[counts_index][records_index] == -1:
                    dp[counts_index][records_index] = self.computePossibleLine(records, records_index+i+cur_count+1, counts, counts_index+1, dp)
                start_total += dp[counts_index][records_index]
                break
            elif '.' not in sub_check and (i+cur_count >= len(cur_records) or cur_records[i+cur_count] != '#'):
                if dp[counts_index][records_index] == -1:
                    dp[counts_index][records_index] = self.computePossibleLine(records, records_index+i+cur_count+1, counts, counts_index+1, dp)
                start_total += dp[counts_index][records_index]
        print(dp)
        return start_total

    # def computePossibleLine(self, records, counts) -> int:
    #     # print(records, counts)
    #     occupied_positions = sum([1 for x in records if x == '#'])
    #     missing_positions = []
    #     for i, val in enumerate(records):
    #         if val == '?':
    #             missing_positions.append(i)
    #     positions_to_fill = sum(counts) - occupied_positions
    #     # print(f"how many missing {positions_to_fill} from {counts} {records}")
    #     valid_count = 0
    #     for val in itertools.combinations(missing_positions, positions_to_fill):
    #         records_copy = records
    #         for index in val:
    #             records_copy = records_copy[0:index] + '#' + records_copy[index+1:]
    #             # print(records_copy)
    #         if self.checkValid(records_copy.replace('?', '.'), counts):
    #             valid_count += 1
    #     # print(positions_to_fill)
    #     return valid_count
    
    # # want to check if the groupings of '#' lens match the counts
    # # ###..##..#...### 3 2 1 3
    # # 3, 2, 1, 3 == 3 2 1 3
    # def checkValid(self, records, counts):
    #     records_groupings = [x for x in records.split('.') if x != '']
    #     # print(records_groupings)
    #     records_groupings_lens = [len(x) for x in records_groupings]
    #     # print(f"Checking {records} with {records_groupings}")
        
    #     if len(records_groupings_lens) != len(counts):
    #         return False

    #     for i in range(len(records_groupings_lens)):
    #         if records_groupings_lens[i] != counts[i]:
    #             return False
    #     # print(f"Found valid string {records} {counts}")
    #     return True


def main():
    broke_records = HotSpringRecords("Day 12/test_input.txt")
    broke_records.parseFile()
    # broke_records.uncoilRecords()
    broke_records.computeAllPossibleLines()
    print(broke_records.res)


if __name__ == "__main__":
    main()
