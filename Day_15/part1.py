def convertToValue(text):
    res = 0
    for char in text:
        res += ord(char)
        res *= 17
        res %= 256
    return res

def removeValue(cur_list, label):
    for i, val in enumerate(cur_list):
        if val[0] == label:
            cur_list = cur_list[:i] + cur_list[i+1:]
            break
    return cur_list

def addValue(cur_list, label, focal_length):
    new_val = (label, focal_length)
    added = False
    for i, val in enumerate(cur_list):
        if val[0] == new_val[0]:
            cur_list[i] = new_val
            added = True
            break
    if not added:
        cur_list.append(new_val)
    return cur_list


def main():
    cur_file = "Day_15/input.txt"
    print("************** PART 1 ANSWER **************")
    file = open(cur_file)
    values = file.readline().strip().split(',')
    res = 0
    for i in range(len(values)):
        res += convertToValue(values[i])
    print(res)

    print("************** PART 2 ANSWER **************")
    file = open(cur_file)
    values = file.readline().strip().split(',')
    hash_map = {x:[] for x in range(256)}
    res = 0

    for i in range(len(values)):
        val = values[i]
        # need to remove
        if '-' in val:
            label = val[:-1]
            cur_hash = convertToValue(label)
            hash_map[cur_hash] = removeValue(hash_map[cur_hash], label)
        # we can split on =
        else:
            label, focal_length = val.split('=')
            cur_hash = convertToValue(label)
            hash_map[cur_hash] = addValue(hash_map[cur_hash], label, focal_length)
            # print(cur_hash)
    
    # add up the results
    for key, val in hash_map.items():
        for i, inner_val in enumerate(val):
            # print(key + 1, i, inner_val[1])
            res += (key+1) * (i+1) * int(inner_val[1])
    # print(hash_map)
    print(res)

if __name__ == "__main__":
    main()