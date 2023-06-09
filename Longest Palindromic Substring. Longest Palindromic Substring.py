# Longest Palindromic Substring

# Given a string s, return the longest 
# palindromic substring in s.

'''--->  My First Approach :
                  maintain a pointer of each index covered  lets say initial = 0
                  maintain longest_palindrome_len variable lpl = 0
                  now traverse the string from initial to the half of the left string + 1
                  lets say we traverse using varible j=initial to j = {(len(string) - initial) // 2} + 1
                  now compare if string[initial:j] == string[j+1:j+(j-initial)]
                  if yes then check if j-initial is greater than lpl if yes then update lpl and continue else continue
                  '''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        initial = 0
        lpl = 1
        j = initial
        while initial < len(s)//2+1:
            diff = (len(s) - initial) //2 + 1
            while j < diff:
                if s[initial:j] == s[j+1:j+(j-initial)]:
                    if (j-initial) * 2 > lpl:
                        lpl = (j-initial) * 2
                j+=1
            initial += 1
        return lpl
solObj = Solution()
print(solObj.longestPalindrome(s = "babad"))






