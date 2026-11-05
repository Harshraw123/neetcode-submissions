class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
           
           return False


        arr=[0]*26

        for i in range(len(s)):

          index1=ord(s[i])-97

          arr[index1]=arr[index1]+1


        for i in range(len(t)):

            index=ord(t[i])-97

            arr[index]=arr[index]-1


        for i in range(len(arr)):

            if arr[i]!=0:

                return False

        return True           



        