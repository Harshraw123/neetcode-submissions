class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:


        map={}

        for i , num in enumerate(numbers):

            find=target-num

            if find in map:

                return [map[find]+1,i+1]

            map[num]=i    





        