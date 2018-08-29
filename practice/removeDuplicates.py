class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) is 0:
            return 0
        if len (nums) is 1:
            return 1

        retval = 1
        i = 0
        j = 1
        while j < len(nums):
            if(nums[i] != nums[j]):
                retval +=1
                i += 1
                nums[i] = nums[j]
            j += 1
        return retval