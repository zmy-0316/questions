"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。
注意：还是需要用到startindex，只是更新不加一；
剪枝：剪枝操作前提必须排序才可以剪枝，和尾target，如果当前sum已经大于target，后续所有元素就没必要在遍历了，直接结束。

"""
class Solution:
    #result = []
    def combine(self, candidates, target):
        candidates = sorted(candidates)
        result = []
        self.backtracking(candidates, target, 0, 0, [], result)
        return result


    def backtracking(self, candidates, targets, cur_sum, startindex, path, result):
        if cur_sum == targets:
            result.append(path[:])
            return
        for i in range(startindex, len(candidates)):
            if cur_sum + candidates[i] > targets:
                break
            path.append(candidates[i])
            cur_sum += candidates[i]
            self.backtracking(candidates, targets, cur_sum, startindex, path, result)
            path.pop()
            cur_sum -= candidates[i]

solution = Solution()
print(solution.combine([2, 3, 6, 7], 7))
