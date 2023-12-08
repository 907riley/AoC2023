"""
intuition

Put all the different parent -> (left, right) relationships
into a hastable with parent as the key

Put the path instructions (LRLRLRRRR...) into a queue that you always pop then push

To find res, traverse the paths starting at AAA, using the directions, keeping track of steps
Stop once you've reached ZZZ

I'm a little scared that I'm not implementing like a true adjacency list but I think this
is okay since each parent only has two children. I fear part 2...
"""
from collections import deque


class CamelTraversal:

    def __init__(self, filename) -> None:
        self.file = open(filename, 'r')
        # dict
        self.paths = {}
        # queue
        self.directions = []
        self.res = 0

    def parseInput(self) -> None:
        self.directions = deque([char for char in self.file.readline().strip()])
        # get rid of newline
        self.file.readline()
        # parse all the paths in the file
        for line in self.file:
            key_raw, children_raw = line.strip().split('=')
            children = children_raw.strip().strip('()').split(',')
            self.paths[key_raw.strip()] = (children[0], children[1].strip())
        # print(self.directions)
        # print(self.paths)
    
    def traversePath(self) -> None:
        start = "AAA"
        end = "ZZZ"

        cur = start
        while cur != "ZZZ":
            # get the possible paths
            cur_children = self.paths[cur]

            # deal with queue and get direction
            direction = self.directions.popleft()
            self.directions.append(direction)

            if direction == 'L':
                cur = cur_children[0]
            else:
                cur = cur_children[1]
            self.res += 1


def main():
    traverse = CamelTraversal("Day 8/input.txt")
    traverse.parseInput()
    traverse.traversePath()
    print(traverse.res)

if __name__ == "__main__":
    main()
