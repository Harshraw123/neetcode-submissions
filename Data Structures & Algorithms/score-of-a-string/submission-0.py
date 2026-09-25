class Solution:
    def scoreOfString(self, s: str) -> int:
        
 
        l=0
        r=1
        ans=0

        while l<len(s) and r<len(s):

            ans+=abs(ord(s[l])-ord(s[r]))

            l+=1
            r+=1

        return ans     
