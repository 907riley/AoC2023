file = open("input.txt", 'r')
res = 0

nums = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

count = 0
while 1:
    line = file.readline()
    n = len(line)

    if n == 0:
        break
    
    ans = []
    # parse the whole input line now
    # spelled letters can only be length 3-5
    # so first check for input that cannot have any valid spelled letters
    # if n < 3:
    #     for i in range(n):
    #         if line[i] in "0123456789":
    #             ans.append(int(line[i]))
    # then check for spelled letters if the bounds allow
    # while also still looking at the individual chars
    # else:
    cur = ""
    for i in range(n):
        if line[i] in "0123456789":
            ans.append(int(line[i]))
        else:
            for j in range(3):
                if i < n-3+j:
                    cur = line[i:i+3+j]
                    if cur in nums:
                        ans.append(nums[cur])
    print(ans[0], ans[-1])
    res += ans[0] * 10 + ans[-1]

print(res)
