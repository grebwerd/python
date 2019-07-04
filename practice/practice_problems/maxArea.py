class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        leftIndex = 0
        rightIndex = len(height)-1
        maxArea = 0;

        while leftIndex < rightIndex:
            leftIndexValue = height[leftIndex]
            rightIndexValue = height[rightIndex]
          
            minHeight = min(leftIndexValue, rightIndexValue)
            tempArea = minHeight *(rightIndex - leftIndex)
          
            if maxArea < tempArea:
                maxArea = tempArea
            
            if leftIndexValue < rightIndexValue:
               
                leftIndex +=1
            else:
               
                rightIndex -= 1
        
        return maxArea