# count substring in a string with atmost k 0s and k 1s
for _ in range(int(input())):
    n, k, q = map(int, input().split())
    strng = input()
    queries = []
    for i in range(q):
        l, r = map(int, input().split())
        queries.append((l - 1, r))
    # print(queries)
    for temp in queries:
        count = 0
        L, R = temp[0], temp[1]
        string = strng[L:R]
        for i in range(len(string)):
            # Now we will calculate all possible substrings of length i if i  greater than k
            if (i+1 <= k):
                count += len(string)-i
            else:
                for j in range(len(string)-i):
                    sub_string = string[j:i+j+1]
                    ones = sub_string.count('1')
                    zeros = sub_string.count('0')
                    if not (ones > k or zeros > k):
                        count += 1
        print(count)

        