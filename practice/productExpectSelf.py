class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            print("Appending the value ", p, " in the first loop to output")
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            print("the value of output[i]:", output[i], " the value of p is ", p, " the value of i is", i)
            output[i] = output[i] * p
            print("The output value for index ", i, " is ", output[i])
            print("the value of nums[i]", nums[i])
            p = p * nums[i]
        return output
        