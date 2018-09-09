class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """



    def sumPair(self, nums):
        sums = set()
        print("The length of nums is ",len(nums))
        for index, value in enumerate(nums):
            print("The index is ", index)
            if index+1 < len(nums):
                for nextIndex in range (index+1, len(nums)):
                    print("the nextIndex is", nextIndex)
                    sums.add(nums[index]+nextIndex)
