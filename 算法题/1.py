class Solution(object):
    def twoSum(self, nums, target):
        for i in range(1, len(nums)):
            tmp = nums[:i]
            num1 = target - nums[i]
            if num1 in tmp:
                j = tmp.index(num1)
                return [j, i]


test = Solution().twoSum([2, 7, 10, 17], 9)
print(test)
