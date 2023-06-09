from typing import List
# Array
# Find Smallest Letter Greater Than Target

# You are given an array of characters letters that is sorted in non-decreasing order, 
# and a character target. There are at least two different characters in letters.
# Return the smallest character in letters that is lexicographically greater than target.
# If such a character does not exist, return the first character in letters.

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1
        while right >= left:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return letters[left] if left < len(letters) else letters[0]
        

solObj = Solution()
print(solObj.nextGreatestLetter(["c","f","j"], target = "c"))