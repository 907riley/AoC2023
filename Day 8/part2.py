"""
intuition

Put all the different parent -> (left, right) relationships
into a hastable with parent as the key.
While doing this get the start nodes (any nodes ending in Z)

Put the path instructions (LRLRLRRRR...) into a queue that you always pop then push

To find res, traverse the paths starting at all the start nodes, using the directions, keeping track of steps
Stop once every cur value ends in Z

Turns out my implementation lends itself nicely to part 2

I was wrong lol, this is inefficient. I think each path should just be a loop once it reaches the end.
Lets try finding all the lengths of each path, then find the LCM of all the paths. That should give us 
their intersection
"""
from collections import deque
import math


class CamelTraversal:

    def __init__(self, filename) -> None:
        self.file = open(filename, 'r')
        # dict
        self.paths = {}
        # queue
        self.directions = []
        # starting nodes
        self.starting_nodes = []
        # lengths of each path
        self.path_lengths = []
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
            if key_raw.strip()[-1] == 'A':
                self.starting_nodes.append(key_raw.strip())
        
        # setup path lengths
        for _ in self.starting_nodes:
            self.path_lengths.append(0)
        # print(self.directions)
        # print(self.paths)
    
    def traversePath(self) -> None:
        end = False
        cur_nodes = self.starting_nodes

        while not end:
            self.res += 1
            # print(self.res, cur_nodes)
            end = True
            new_nodes = []
            # deal with queue and get direction
            direction = self.directions.popleft()
            self.directions.append(direction)

            # now go through all the current nodes
            for i, starting_node in enumerate(cur_nodes):
                # a negative one in the list means we've already finished that path
                # didn't want to deal with weird indices so I did this instead lol
                if starting_node == -1:
                    new_nodes.append(-1)
                    continue
                # get the possible paths
                cur_children = self.paths[starting_node]

                next = None
                if direction == 'L':
                    next = cur_children[0]
                else:
                    next = cur_children[1]

                if next[-1] == 'Z':
                    self.path_lengths[i] = self.res
                    new_nodes.append(-1)
                else:
                    new_nodes.append(next)
                    end = False

            cur_nodes = new_nodes
    
    def computeMinSteps(self) -> None:
        res = self.path_lengths[0]
        print(self.starting_nodes)
        print(self.path_lengths)
        for i in range(1, len(self.path_lengths)):
            res = (self.path_lengths[i] * res) // (math.gcd(self.path_lengths[i], res))
        self.res = int(res)


def main():
    traverse = CamelTraversal("Day 8/input.txt")
    traverse.parseInput()
    traverse.traversePath()
    traverse.computeMinSteps()
    print(f"Steps required: {traverse.res}")

if __name__ == "__main__":
    main()
