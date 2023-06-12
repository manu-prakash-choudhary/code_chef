import sys

# Que 1 :  Merge Strings Alternately
from itertools import zip_longest

class Solution1:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # simplest approach suggestion str1 and then str2 if i%2 ==  merge from str1 else merge from str2
        
        return "".join(sum(zip_longest(word1, word2, fillvalue=""), ()))
    
solObj = Solution1()
print(sys._getframe(0).f_lineno, 'Que 1', solObj.mergeAlternately(word1 = "ab", word2 = "pqrs"))


# Que 2 :  Reverse Vowels of a String
class Solution2:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        s = list(s)
        left, right = 0, len(s)-1

        while right > left:
            leftS = s[left].lower()
            rightS = s[right].lower()
            if leftS not in vowels:
                left += 1
                continue
            if rightS not in vowels:
                right -= 1
                continue
            s[left], s[right] = s[right], s[left]
            left, right = left+1, right-1
        return ''.join(s)
solObj = Solution2()
print(sys._getframe(0).f_lineno, 'Que 2', solObj.reverseVowels(s = "leetcode"))




