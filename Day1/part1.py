
file = open("input.txt", 'r')
res = 0

count = 0
while 1:
    line = file.readline()
    n = len(line)

    if n == 0:
        break

    ans = [0, 0]
    for i in range(n):
        if line[i] in "0123456789":
            # print("found first", line[i])
            ans[0] = int(line[i])
            break
    
    for i in range(n-1, -1, -1):
        if line[i] in "0123456789":
            # print("found last", line[i])
            ans[1] = int(line[i])
            break
    # print()
    res += ans[0] * 10 + ans[1]
    # print(ans[0], ans[1], res)

print(res)
