class Solution:
    def isPalindrome(self, s: str) -> bool:


        st=''

        def isValid(ch):
         if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z') or ('0' <= ch <= '9'):
          return True
         else:
          return False

          

        for i in range(len(s)):

            if isValid(s[i]):

                st+=s[i]


        l=0

        r=len(st)-1

        while(l<=r):

            if(st[l].lower()!=st[r].lower()):

                return False   
            l+=1
            r-=1     
        
        return True
