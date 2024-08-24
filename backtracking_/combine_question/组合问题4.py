"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。
说明： 所有数字（包括目标数）都是正整数。解集不能包含重复的组合。
区别于前一题：
本题candidates 中的每个数字在每个组合中只能使用一次。（startindex有调整）
本题数组candidates的元素是有重复的，而前一题是无重复元素的数组candidates（需要有去重操作
"""
class Solution:
    def combine(self, candidates, target):
        used = [False] * len(candidates)
        result = []
        candidates = sorted(candidates)
        self.backtracking(candidates, target, 0, 0, used, [], result)
        return result
    def backtracking(self, candidates, targets, cur_sum, startindex, used, path, result):
        if cur_sum == targets:
            result.append(path[:])
            return
        for i in range(startindex, len(candidates)):
            if i > startindex and candidates[i] == candidates[i - 1] and not used[i - 1]:
                continue
            if cur_sum + candidates[i] > targets:
                break
            path.append(candidates[i])
            cur_sum += candidates[i]
            used[i] = True
            self.backtracking(candidates, targets, cur_sum, i + 1, used, path, result)
            path.pop()
            cur_sum -= candidates[i]
            used[i] = False


solution = Solution()
print(solution.combine([10,1,2,7,6,1,5], 8))
