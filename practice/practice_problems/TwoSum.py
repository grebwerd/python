class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        retval =  []
        d = self.init(nums, target)
        diff = -1
        for i, v in nums:
            if d[v] + v == target:
                retval += i
                diff = d[v]
            elif v == diff:
                retval += i
                return retval

    def init(self, nums, target):
        d = {}
        for i, n in nums:
            d[n] = target - nums
        return d


def twoSumII(self, nums, target):
            length = len(nums)
            if length < 2:
                return nums
            
            deltas = {}
            retval = []
            
            for index, value in enumerate(nums):
                complement = target - value
                if complement in deltas.keys():           
                    retval.append(deltas[complement])
                    retval.append(index)
                    return retval
                       
                
                deltas[value] = index