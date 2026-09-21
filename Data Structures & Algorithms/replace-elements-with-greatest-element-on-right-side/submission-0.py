class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        

        rightMax=[0]*len(arr)

        currentMax=arr[-1]


        rightMax[-1]=-1

        for i in reversed(range(len(rightMax) - 1)):

            rightMax[i]=max(currentMax,arr[i+1])

            currentMax=max(currentMax,arr[i])

         

        return rightMax



