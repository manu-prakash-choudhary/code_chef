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
''' Below is the general Solution of the problem and it works'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        initial = 0
        lpl = 1
        LPstring = s[0]
        while initial < len(s):
            
            j =  initial
            diff = (len(s) - initial)
            while j - initial <= diff//2:
                a = j+1
                j_initial_diff = j - initial
                limit = a + j_initial_diff + 1
                if s[initial:a] == s[a:limit][::-1]:
                    if (j_initial_diff + 1) * 2 > lpl:
                        lpl = (j_initial_diff + 1) * 2
                        LPstring = s[initial:limit]
                elif s[initial:a] == s[a-1:limit-1][::-1]:
                    if (j_initial_diff ) * 2 + 1> lpl:
                        lpl = (j_initial_diff ) * 2 + 1
                        LPstring = s[initial:limit-1]

                j+=1
            initial += 1
        return LPstring
solObj = Solution()
print(solObj.longestPalindrome(s = "aaabbbcdaadc"))
# print(solObj.longestPalindrome(s = "cbbd"))
# print(solObj.longestPalindrome(s = "babad"))






