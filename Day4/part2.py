"""
Intuition:
    Need to know how many values match from the winning numbers and the numbers you have
    Assuming there are no duplicate winning numbers

Algorithm:
    Convert both lists to a set
    Do a set intersection
    get n = len(matching)
    update dict values for next n with cur value in dict
    update score with cur value in dict
"""

class Scratchcard:

    def __init__(self, file_name):
        self.file_name = file_name
        # this isn't good, but this is a one time thing
        self.scores = {index: 1 for index in range(1, 215)}
        self.score = 0

    def compute_scores(self):
        file = open(self.file_name, 'r')

        i = 1
        for line in file:
            line = line.strip()
            numbers = line.split(':')
            winning_numbers, your_numbers = numbers[1].split('|')
            winning_numbers_set = set(x for x in winning_numbers.split(" ") if x != "")
            your_numbers_set = set(x for x in your_numbers.split(" ") if x != "")
            matching_set = winning_numbers_set & your_numbers_set

            # print(numbers[0], matching_set, f"adding {(2 ** (len(matching_set) - 1) if len(matching_set) > 0 else 0)}")
            n = len(matching_set)
            for j in range(1, n+1):
                if i+j in self.scores:
                    self.scores[i+j] += self.scores[i]
            self.score += self.scores[i]
            i += 1



def main():
    scorecard = Scratchcard("Day 4/input.txt")
    scorecard.compute_scores()
    print(scorecard.score)


if __name__ == "__main__":
    main()
