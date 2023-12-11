"""
Intuition

First parse the file into a matrix line by line
If a line has no # then put then add that index to empty_rows
Then go through and find the empty cols and add that index to the empty_cols

Once you have the complete matrix, go through and save the locations
of every galaxy into a list as (x, y)

While list:
    cur = list.pop()
    for val in list:
        find shortest dist to val
        res += shortest dist

Shortest dist formula is gonna be a math formula with coords that checks how many empty vals they cross
"""
import collections
import math

class GalaxyExpansion:

    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.matrix = []
        self.galaxies = []
        self.empty_rows = []
        self.empty_cols = []
        self.expansion_constant = 1000000
        self.res = 0

    def parseFile(self):
        for i, line in enumerate(self.file):
            line = [x for x in line.strip()]
            if '#' not in line:
                self.empty_rows.append(i)
            self.matrix.append([x for x in line])
        
        # find empty cols:
        for i in range(len(self.matrix[i])):
            empty = True
            for j in range(len(self.matrix)):
                if self.matrix[j][i] == '#':
                    empty = False
            if empty:
                self.empty_cols.append(i)

    def findGalaxies(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] == '#':
                    self.galaxies.append((i, j))
        # print(self.galaxies)
    """
    While list:
    cur = list.pop()
    for val in list:
        find shortest dist to val
        res += shortest dist
    """
    def computeMinDistances(self):
        queue = collections.deque(self.galaxies)
        # print(self.empty_rows, self.empty_cols)
        while queue:
            cur = queue.popleft()
            x1, y1 = cur
            for val in queue:
                x2, y2 = val
                x_empties = self.findEmptyVals(x1, x2, self.empty_rows)
                # print("x rows", x1, x2, x_empties)
                y_empties = self.findEmptyVals(y1, y2, self.empty_cols)
                # print("y cols", y1, y2, y_empties)
                self.res += abs(x1-x2) + abs(y1-y2) + (x_empties + y_empties) * (self.expansion_constant-1)
    

    def findEmptyVals(self, i, j, empty_vals):
        # always want j > i
        if i > j:
            i, j = j, i
        res = 0
        for val in empty_vals:
            if val < j and val > i:
                res += 1
        # print(i, j, empty_vals, res)
        return res
        


def main():
    galazzy = GalaxyExpansion("Day 11/input.txt")
    galazzy.parseFile()
    galazzy.findGalaxies()
    galazzy.computeMinDistances()
    print(galazzy.res)

if __name__ == "__main__":
    main()
