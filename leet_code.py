# class Solution:
#     def removeStones(self, stones) -> int:
#         if len(stones) == 1:
#             return 1
#         connections = []
#         res = 0
#         num_conn = 0
#         for i in range(len(stones)):
#             has_connection = False
#             for j in range(len(stones)):
#                 if i != j:
#                     if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
#                         has_connection = True
#                         distinct_conn = True
#                         for k in connections:
#                             for l in k:
#                                 if l[0] == stones[j][0] or l[1] == stones[j][1]:
#                                     distinct_conn = False
#                                     k.append([stones[0],stones[1]])
#                                     break
#                         if distinct_conn:
#                             num_conn += 1
#                             connections.append([[stones[j][0], stones[j][1]]])
#             if not has_connection:
#                 res += 1
#         print(connections)
#         if num_conn:
#             return  len(stones) - (res + num_conn)
#         return len(stones) - res

# # [[[3, 1], [[3, 2], [3, 1]], [[3, 2], [3, 1]], [[3, 2], [3, 1]], [[3, 2], [3, 1]]], [[0, 2], [[3, 2], [3, 1]], [[3, 2], [3, 1]]], [[4, 0], [[3, 2], [3, 1]]]]
# # print(Solution().removeStones( [[3,2],[3,1],[4,4],[1,1],[0,2],[4,0]]))
# print(Solution().removeStones( [[3,2],[3,1],[4,4],[1,1],[0,2],[4,0]]))

# class Solution:
#     def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
#         if ax1 >= bx2 or ax2 <= bx1 or ay1 >= by2 or ay2 <= by1:
#             total_area = (ax2 - ax1) * ((ay2 - ay1)) + (bx2 - bx1) * (ay2 - ay1)
#             return total_area
#         # now find overlapping


# print(Solution().computeArea(ax1=-3, ay1=0, ax2=3, ay2=4, bx1=0, by1=-1, bx2=9, by2=2))
# class Solution:
#     def isUgly(self, n: int) -> bool:
#         if n <= 0:
#             return False
#         set1 = {2, 3, 5}
#         prime_factors = set()
#         if n % 2 == 0:
#             prime_factors.add(2)
#             while n % 2 == 0:
#                 n = n / 2
#         for i in range(3, int(n**0.5) + 1,2):
#             if n % i == 0:
#                 while n % i == 0:
#                     n = n / i
#                 prime_factors.add(i)
#         if n > 2:
#             prime_factors.add(n)
#         if (prime_factors - set1):
#             return False
#         return True

# print(Solution().isUgly(14))
# end of line

# add subtract expression evaluation problem
# s = "-(-1+(4+5+2)-3+(-4))+(6+8)"
# s = s.replace(" ","")
# a = s.split("(")
# print(s)
# print(a)
# res_final = 0
# for i in range(len(a)):
#     if a[i]:
#         b = a[i].split(")")
#         print('b->',b)
#         # res = 0
#         for j in range(len(b)):
#             if b[j] and len(b[j])>1:
#                 if len(b[j])% 2 == 1:
#                     if b[j][0] == '+' or b[j][0] == '-':
#                         continue
#                     eve = True
#                     num = []
#                     operations = []

#                     for k in b[j] :
#                         if eve :
#                             int(k)
#                             num.append(int(k))
#                             eve = False
#                         else:
#                             eve = True
#                             if k =='+':
#                                 operations.append('+')
#                             else:
#                                 operations.append('-')
#                     res = num[0]
#                     for l in range(len(operations)):
#                         if operations[l] == '+':
#                             res += num[l+1]
#                             b[j] = str(res)
#                             print(res)
#                         else:
#                             res -= num[l+1]
#                             b[j] = str(res)
#                             print(res,'in negative')
#                 else:
#                     pass
#             if len(b[j]) > 2:
#                 eve = True
#                 num = []
#                 operations = []
#                 for k in b[j][3:]:
#                     if eve :
#                         int(k)
#                         num.append(int(k))
#                         eve = False
#                     else:
#                         eve = True
#                         if k =='+':
#                             operations.append('+')
#                         else:
#                             operations.append('-')
#                 res = num[0]
#                 for l in range(len(operations)):
#                     if operations[l] == '+':
#                         res += num[l+1]
#                         b[j] = str(res)
#                         print(res)
#                     else:
#                         res -= num[l+1]
#                         b[j] = str(res)
#                         print(res,'in negative')
#                     # if not len(operations):
#                     #     b[j] = b[j][:3] + b[3:]
#                 # b[j] = str(int(b[j]) - 2*int(b[j][1]))
#                 # b[j] = '-' + b[j]
#                 if b[j][2] == '+':
#                     b[j] = str(-int(b[j][1]) + int(b[j][3]))
#                 else:
#                     b[j] = str(-int(b[j][1]) - int(b[j][3]))
#                 print("expected -1 ->",b[j])

#             else:
#                 pass
#         print('final b ->',b)
#         a[i] = ''.join(b)
#         # for k in range(len(b)):
#         #     b = ''.join(b)


# print('final a', a)
# nums = []
# operations = []
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         if a[i][j] == '+' or a[i][j] == '-':
#             operations.append(a[i][j])
#         elif a[i][j] != '' and a[i][j] != ')':
#             nums.append(a[i][j])
# print('value of nums ->',nums)
# print('value of operations ->',operations)

# exception possible list
#  -(-3 + 2)
# ['-', '-3+2']
# it ends here

class Solution:
    def uniqueOccurrences(self, arr: list) -> bool:
        item_set = set()
        count_set = set()

        for i in arr:
            if i not in item_set:
                item_set.add(i)
                count = 0
                for j in arr:
                    if j==i:
                        count+=1
                if count not in count_set:
                    count_set.add(count)
                else:
                    return False
        
        return True
            


print(Solution().uniqueOccurrences(arr = [1,2,2,2,1,1,3]))