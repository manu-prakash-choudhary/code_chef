# find string with no continous occurence of a letter
# if there is remove the two chars
# repeat the proces untill none left
# class Solution:
#     def removeDuplicates(self, s: str) -> str:
#         if len(s) > 2:
#             len_s = len(s) // 2
#             left_s = s[:len_s]
#             right_s = s[len_s:]
#             l = self.removeDuplicates(left_s)
#             r = self.removeDuplicates(right_s)
#             if l and r:
#                 l_int = len(l)-1
#                 r_int = 0
#                 while l_int >= 0 and r_int<len(r):
#                     if l[l_int] == r[r_int]:
#                         l_int-=1
#                         r_int+=1
#                     else:
#                         break
#                 if l_int < 0:
#                     if r_int > len(r):
#                         return ""
#                     return r[r_int:]
#                 else:
#                     if r_int > len(r):
#                         return l[:l_int+1]
#                     return l[:l_int+1] + r[r_int:]
#             return l + r

#         if len(s) > 1:
#             if s[0] == s[1]:
#                 return ""
#         return s


class Solution:
    def removeDuplicates(self, nums):
        i=0
        temp  = nums[0]
        c = 0
        while True:
            if nums[i] == temp and c:
                break
            c=1
            j = nums[i]
            while j in nums:
                nums.remove(j)
            nums.append(j)
        return nums
print(Solution().removeDuplicates([1,1,2]))

# this new line
