# Que 1 :  Merge Strings Alternately
from itertools import zip_longest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # simplest approach suggestion str1 and then str2 if i%2 ==  merge from str1 else merge from str2
        
        return "".join(sum(zip_longest(word1, word2, fillvalue=""), ()))
    
solObj = Solution()
print(solObj.mergeAlternately(word1 = "ab", word2 = "pqrs"))


# Que 2 :  Reverse Vowels of a String