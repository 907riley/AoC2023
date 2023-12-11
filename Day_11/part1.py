"""
Intuition

First parse the file into a matrix line by line
If a line has no # then put that line in twice
Then parse the matrix col by col looking for empty cols to dup

Once you have the complete matrix, go through and save the locations
of every galaxy into a list as (x, y)

While list:
    cur = list.pop()
    for val in list:
        find shortest dist to val
        res += shortest dist

Shortest dist formula is gonna be a math formula with coords
"""
import collections
import math

class GalaxyExpansion:

    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.matrix = []
        self.galaxies = []
        self.res = 0

    def parseFile(self):
        for line in self.file:
            line = [x for x in line.strip()]
            if '#' not in line:
                self.matrix.append([x for x in line])
            self.matrix.append([x for x in line])
        

        for i in range(len(self.matrix[0])-1, -1, -1):
            empty = True
            for j in range(len(self.matrix)):
                if self.matrix[j][i] == '#':
                    empty = False
            if empty:
                for j in range(len(self.matrix)):
                    self.matrix[j].insert(i+1, '.')
            # for row in self.matrix:
            #     print(row)
    
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
        
        while queue:
            cur = queue.popleft()
            x1, y1 = cur
            for val in queue:
                x2, y2 = val
                self.res += abs(x1-x2) + abs(y1-y2)


def main():
    galazzy = GalaxyExpansion("Day 11/input.txt")
    galazzy.parseFile()
    galazzy.findGalaxies()
    galazzy.computeMinDistances()
    print(galazzy.res)

if __name__ == "__main__":
    main()
