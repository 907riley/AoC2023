# intuition (very similar to part 1) as the only part that changes is classifying typing
# create a hastable with keys as hand types and values as heaps with tuples (modified_hand, hand, bid)
# the modified hand is for the sake of sorting because A, K, Q, J, T are not ascii sorted already
# convert the symbols to the following to fix this. Created in the following for loop
#   A -> _
#   K -> ^
#   Q -> ]
#   J -> \
#   T -> [
#   J -> / (new lowest)
# for each hand in the input file
#   sort the hand as a copy
#   determine what type it is by the occurrences
#       CHANGE -> if there are jokers, append all jokers to the highest non joker occurence, now compute type
#   append the original hand and bet to the correct type hash
# multiplier = 1
# for each hand type in order from weakest to strongest:
#   while their are still values in the heap:
#       pop smallest
#       res += bid*multiplier
#       multiplier += 1
# return res

import heapq

class CamelCards:

    def __init__(self, file_name) -> None:
        self.res = 0
        self.types = ["High Card", "One Pair", "Two Pair", "Three of a Kind", "Full House", "Four of a Kind", "Five of a Kind"]
        self.type_hands = {}
        self.file = open(file_name, 'r')

        # init the dict
        for hand_type in self.types:
            self.type_hands[hand_type] = []
    
    def parseHands(self) -> None:
        for line in self.file:
            hand_counts = {}
            hand, bid = line.strip().split(" ")
            # create a dict for this hand of card -> count of card
            for char in hand:
                if char not in hand_counts:
                    hand_counts[char] = 0
                hand_counts[char] += 1
            joker_destination = ['', 0]
            # deal with jokers, don't change if all jokers
            if 'J' in hand_counts and hand_counts['J'] != 5:
                # find new max
                for key, val in hand_counts.items():
                    if key != 'J' and val > joker_destination[1]:
                        joker_destination = [key, val]
                # always just add jokers to our non joker highest occurrence card
                hand_counts[joker_destination[0]] += hand_counts['J']
                del hand_counts['J']
            # determine the hand type
            hand_type = self.determineType(hand_counts)
            # create our hand copy for easy heap sorting
            modified_hand = self.createModifiedCopy(hand)
            # push to type heap with modified hand first in tuple so it is what gets sorted on
            heapq.heappush(self.type_hands[hand_type], (modified_hand, hand, bid))

    # logic for determing hand type based on card counts
    def determineType(self, hand_counts):
        vals = [x[1] for x in hand_counts.items()]

        if 5 in vals:
            return "Five of a Kind"
        elif 4 in vals:
            return "Four of a Kind"
        elif 3 in vals:
            if 2 in vals:
                return "Full House"
            return "Three of a Kind"
        elif 2 in vals:
            count = 0
            for val in vals:
                if val == 2:
                    count += 1
            if count > 1:
                return "Two Pair"
            return "One Pair"
        return "High Card"

    # convert the symbols to the following to fix issue of sorting
    #   A -> _
    #   K -> ^
    #   Q -> ]
    #   J -> \
    #   T -> [
    #   J -> /
    # go look at an ASCII table to see why these values
    # they are in the correct order basically, didn't have to be these ones
    def createModifiedCopy(self, hand):
        modifier = {
            'A': '_',
            'K': '^',
            'Q': ']',
            'J': '\\',
            'T': '[',
            'J': '/'
            }
        new_hand = ""
        for char in hand:
            if char in modifier:
                new_hand += modifier[char]
            else:
                new_hand += char
        return new_hand
    
    # computes the answer
    # just goes through the hand types from weakest to strongest
    # popping out the heaps from weakest to strongest
    # keeping track of the number we have iterated through
    def computeRes(self) -> None:
        multiplier = 1
        # for each type weakest to strongest
        for hand_type in self.types:
            while len(self.type_hands[hand_type]) > 0:
                cur = heapq.heappop(self.type_hands[hand_type])
                self.res += multiplier * int(cur[2])
                multiplier += 1

def main():
    cards = CamelCards("Day 7/input.txt")
    cards.parseHands()
    cards.computeRes()
    print(cards.res)

if __name__ == "__main__":
    main()
