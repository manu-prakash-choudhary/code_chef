#  Que link -> https://leetcode.com/problems/implement-queue-using-stacks/
# Aim - use stack to create queue
# class MyQueue:

#     def __init__(self):
#         self.stack2 = []

#     def push(self, x: int) -> None:
#         self.stack2.append(x)

#     def pop(self) -> int:
#         stack1 = self.stack2.copy()
#         self.stack2 = []
#         while len(stack1)  > 1:
#             self.stack2.append(stack1.pop())
#         popped_item = stack1.pop()
#         stack1 = self.stack2.copy()
#         self.stack2 = []
#         while len(stack1) > 0:
#             self.stack2.append(stack1.pop())
#         return popped_item

#     def peek(self) -> int:
#         stack1 = self.stack2.copy()
#         while len(stack1) > 1:
#             stack1.pop()
#         return stack1.pop()

#     def empty(self) -> bool:
#         if len(self.stack2):
#             return False
#         else:
#             return True




# # Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(1)
# obj.push(2)

# print(obj.peek())
# print(obj.pop())
# print(obj.empty())

for _ in range(int(input())):
    n, k, q = map(int,input().split())
    s = input()
    queries = []
    for i in range(q):
        l, r = map(int, input().split())
        queries.append((l,r))
    print(queries)
    count = 0
    for temp in queries:
        L, R = temp[0], temp[1]
        string = s[L:R+1]
        for i in range(len(string)):
            # Now we well calculate all possible substrings of length i
            for j in range(len(string) - i):
                sub_string = string[j:]
                if len(sub_string) >= k:
                    ones = sub_string.count('1')
                    zeros = sub_string.count('0')
                    if not(ones > k or zeros > k):
                        count+=1
                else:
                    count += 1
        print(count)
        
