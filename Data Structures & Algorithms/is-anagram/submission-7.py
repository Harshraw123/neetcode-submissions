class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if(len(s)!=len(t)):

            return False
        


        arr1=[0]*26

        if len(s) != len(t):
            return false
        
        
        for i in range(len(s)):

          char=s[i]

          index1=ord(char) - ord('a')

          arr1[index1]=arr1[index1] + 1

          index2=ord(t[i]) - ord('a')

          arr1[index2]=arr1[index2] - 1


        for i in range(len(arr1)):

            if arr1[i]>0:

                return False  

        return True 

        