class Solution:
    def reverseWords(self, s: str):
        strn = ''
        lst = list()
        j = -1
        for i in range(len(s)):
            if s[i] == ' ':
                lst.append(strn)
                strn = ''
            else:
                strn += s[i]
        if strn:
            lst.append(strn)
        lst = lst[-1::-1]
        ans = ''
        for i in lst:
            if i :
                ans+=' '
                ans+=i
                
        return ans[1:]
                
        
print(Solution().reverseWords('  Hello World'))