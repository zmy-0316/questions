"""
子集问题1
"""
class Solution:
    def combine(self, nums):
        result = []
        self.backtracking(nums,0, [], result)
        return result
    def backtracking(self, nums, startindex,  path, result):
        result.append(path[:])
        for i in range(startindex, len(nums)):
            path.append(nums[i])
            self.backtracking(nums, i + 1, path, result)
            path.pop()


solution = Solution()
print(solution.combine([1, 2, 3]))
