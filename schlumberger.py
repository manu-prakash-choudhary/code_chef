# take input n from user
# n = int(input())
#  take spaace separated list
# A = list(map(int, input().split()))
A = [[34,37,81], [2,5,4], [4,8,6]]

#  take input q from user
# q = int(input())
# B = list(map(int, input().split()))
B = [[3, 5], [5,8]]

num_map = dict()
monster_count = 0
for i in A:
    for j in range(i[0], i[1]+1):
        if j in num_map:
            num_map[j].append(i[2])
        else:
            num_map[j] = [i[2]]
        monster_count += 1

# print(num_map)
# sort the dictionary values list
for i in num_map:
    num_map[i].sort()

final_list = []
for i in B:
    strngth = i[1]
    position = i[0]
    if position in num_map:
        for j in num_map[position]:
            if j < strngth:
                monster_count -= 1
    # print(monster_count)
    final_list.append(monster_count)

print(final_list)