class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 2:
            return [0, 1]
        numlist = nums.copy()
        for i, value in enumerate(numlist):
            numlists = numlist.copy()
            numlists.pop(i)
            if target - value in numlists:
                xs = nums.index(value)
                nums.pop(xs)
                xl = nums.index(int(target-value))
                return [xs, xl+1]


'''
nums = [-1,-2,-3,-4,-5]
target = -8
print(Solution().twoSum(nums, target))

nums = [2,7,11,15]
target = 9
print(Solution().twoSum(nums, target))

nums = [3,2,4]
target = 6
print(Solution().twoSum(nums, target))


nums = [3,3]
print(Solution().twoSum(nums, target))
'''