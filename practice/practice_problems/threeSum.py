class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        sumMap = self.sumPair(nums)
        sets = set()
        
        retval = []
        
        if len(nums) < 3 or nums is None:
            return []
        
        
        for index, value in enumerate(nums):
            if value in sumMap:
                lists = sumMap.get(value)
                for l in lists:
                    index1 = l[0]
                    index2 = l[1]
                    if (index is not index1) and (index is not index2):

                        if value < nums[index1]:
                            sets.add(tuple([value, nums[index1], nums[index2]]))
                        elif value < nums[index2]:
                             sets.add(tuple([nums[index1], value, nums[index2]]))
                        else:
                            sets.add(tuple([nums[index1], nums[index2], value]))


        
        retval.extend(list(sets))
        return retval
                



    def sumPair(self, nums):
        sumMap = {}
        for index, value in enumerate(nums):
            if index+1 < len(nums):
                for nextIndex in range (index+1, len(nums)):
                    summ = (nums[index]+nums[nextIndex]) * -1
                    if summ in sumMap.keys():
                        sumMap[summ].append([index, nextIndex])        
                    else:
                        sumMap[summ] = [[index, nextIndex]]
                    
        return sumMap