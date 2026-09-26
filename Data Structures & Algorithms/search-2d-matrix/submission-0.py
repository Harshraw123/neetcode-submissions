class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        #peeche se start krte hai kyoki bda chayie hoga to neeche jaonga and bda chayie hoga to down jaonga
       
        endrow = 0
        endcol = len(matrix[0]) - 1


        while endrow<len(matrix) and endcol>=0:

            if matrix[endrow][endcol]==target:

                return True

            elif matrix[endrow][endcol]<target:

                endrow+=1


            else:

                endcol-=1



        return False            








     

        