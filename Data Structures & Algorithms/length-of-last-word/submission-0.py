class Solution:
    def lengthOfLastWord(self, s: str) -> int:

         r=len(s)-1

         count=0

         while(s[r]==' '):

            r-=1

         while(r>=0 and s[r]!=' '):

            r-=1
            count+=1   

         return count

        
        