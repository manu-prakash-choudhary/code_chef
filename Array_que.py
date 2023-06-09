from typing import List
# Array
# Find Smallest Letter Greater Than Target

# You are given an array of characters letters that is sorted in non-decreasing order, 
# and a character target. There are at least two different characters in letters.
# Return the smallest character in letters that is lexicographically greater than target.
# If such a character does not exist, return the first character in letters.

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        min_greatest = float('inf')
        found = False
        for i in letters:
            if ord(i) < min_greatest and ord(i)>ord(target):
                found = i
                min_greatest = ord(i)
        if found:
            return found
        else: 
            return letters[0]

solObj = Solution()
print(solObj.nextGreatestLetter(["c","f","j"], target = "c"))