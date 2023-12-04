"""
Intuition:
    Need to know how many values match from the winning numbers and the numbers you have
    Assuming there are no duplicate winning numbers

Algorithm:
    Convert both lists to a set
    Do a set intersection
    res += 2 ** (len(intersection) - 1)
"""

class Scratchcard:

    def __init__(self, file_name):
        self.file_name = file_name
        self.score = 0

    def compute_score(self):
        file = open(self.file_name, 'r')

        for line in file:
            line = line.strip()
            numbers = line.split(':')
            winning_numbers, your_numbers = numbers[1].split('|')
            winning_numbers_set = set(x for x in winning_numbers.split(" ") if x != "")
            your_numbers_set = set(x for x in your_numbers.split(" ") if x != "")
            matching_set = winning_numbers_set & your_numbers_set
            # print(numbers[0], matching_set, f"adding {(2 ** (len(matching_set) - 1) if len(matching_set) > 0 else 0)}")
            self.score += (2 ** (len(matching_set) - 1) if len(matching_set) > 0 else 0)



def main():
    scorecard = Scratchcard("Day 4/input.txt")
    scorecard.compute_score()
    print(scorecard.score)


if __name__ == "__main__":
    main()
