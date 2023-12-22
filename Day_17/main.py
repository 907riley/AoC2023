"""
Got help from the subreddit for this one, I got a Djikstras implementation working on my own for the small_input
But I couldn't figure out what I was doing wrong for the actual input
"""

from collections import deque
import heapq

def main():
    filename = "Day_17/input.txt"
    print("********** PART 1 ANSWER **********")
    file = open(filename, 'r')
    board = {(i, j): int(c) for i, r in enumerate(file) for j, c in enumerate(r.strip())}

    def min_heat(start, end, least, most):
        # print(f"Starting with {start} end {end}, least {least}, most{most}")
        queue = [(0, *start, 0, 0)]
        seen = set()

        while queue:
            heat, x, y, px, py = heapq.heappop(queue)
            # print(f" {heat} {x} {px} {py}")
            if (x, y) == end: return heat
            if (x, y, px, py) in seen: continue
            seen.add((x, y, px, py))

            # look at turns
            for dx, dy in {(1, 0), (0, 1), (-1, 0), (0, -1)}-{(px, py), (-px, -py)}:
                a, b, h = x, y, heat
                # enter moves in direction
                for i in range(1, most+1):
                    a, b = a+dx, b+dy
                    if (a,b) in board:
                        h += board[a, b]
                        if i>= least:
                            heapq.heappush(queue, (h, a, b, dx, dy))
    print(min_heat((0, 0), max(board), 1, 3))
    print("********** PART 2 ANSWER **********")
    print(min_heat((0, 0), max(board), 4, 10))








if __name__ == "__main__":
    main()
