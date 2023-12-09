"""
Intuition:
    Search each line for a *
    if found:
        try to look in all adjacent directions (including diagonal), checking that you won't go out of bounds, for a number
        if number is found:
                now look left until found the start of the num
                finally go right until end of num is found doing cur * 10 + new_num
            add number to a list of adjacernts
        if adjacents len == 2:
            res += product(adjacents)
    return res

"""
def getNum(res, dp, n, i, j):
    orig = j
    while dp[i][j-1] in "0123456789" and j > 0:
        # print(f"Moving over{dp[i][j-1]}")
        j -= 1
    
    cur = 0
    while j < n and dp[i][j] in "0123456789":
        cur = cur * 10 + int(dp[i][j])
        j += 1
    print(f"{cur}, ", end="")
    # print(f"Found num {cur} from {i} {orig}")
    return cur


def main():

    file = open('Day3\input.txt', 'r')

    # convert to a 2D matrix
    dp = []
    for line in file:
        temp = []
        for char in line:
            if char != "\n":
                temp.append(char)
        dp.append(temp)
    res = 0
    n = len(dp)
    m = len(dp[0])

    for i in range(n):
        print()
        for j, char in enumerate(dp[i]):
            adjacents = []
            if char == '*':
                # try to look for a num in all directions
                # Right
                if j < n-1:
                    if dp[i][j+1] in "0123456789":
                        adjacents.append(getNum(res, dp, n, i, j+1))
                # Bottom
                if i < n-1 and dp[i+1][j] in "0123456789":
                    # print("bottom")
                    # print(i, len(dp), j, len(dp[i+1]))
                    adjacents.append(getNum(res, dp, n, i+1, j))
                else:
                    # Bottom Left
                    if i < n-1 and j > 0 and dp[i+1][j-1] in "0123456789":
                        # print("bottom left")
                        adjacents.append(getNum(res, dp, n, i+1, j-1))
                    # Bottom Right
                    if i < n-1 and j < n-1 and dp[i+1][j+1] in "0123456789":
                        # print("bottom right")
                        adjacents.append(getNum(res, dp, n, i+1, j+1))

                # Up
                if i > 0 and dp[i-1][j] in "0123456789":
                    # print("up")
                    # print(i, len(dp), j, len(dp[i+1]))
                    adjacents.append(getNum(res, dp, n, i-1, j))
                else:
                    # Upper Left
                    if i > 0 and j > 0 and dp[i-1][j-1] in "0123456789":
                        # print("bottom left")
                        adjacents.append(getNum(res, dp, n, i-1, j-1))
                    # Upper Right
                    if i > 0 and j < n-1 and dp[i-1][j+1] in "0123456789":
                        # print("bottom right")
                        adjacents.append(getNum(res, dp, n, i-1, j+1))
                # Left
                if j > 0:
                    if dp[i][j-1] in "0123456789":
                        adjacents.append(getNum(res, dp, n, i, j-1))
            if len(adjacents) == 2:
                res += (adjacents[0] * adjacents[1])
    print(res)

if __name__ == "__main__":
    main()

