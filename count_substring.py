# count substring in a string with atmost k 0s and k 1s
for _ in range(int(input())):
    n, k, q = map(int, input().split())
    strng = input()
    queries = []
    for i in range(q):
        l, r = map(int, input().split())
        queries.append((l - 1, r))
    print(queries)
        