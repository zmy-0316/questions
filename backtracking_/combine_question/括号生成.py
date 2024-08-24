"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合
可以生出左树枝条件：左括号剩余数量严格大于0；
可以生出右树枝条件：右括号剩余数量严格大于左树枝剩余数量；
"""
class Solution:
    result = []
    def solution(self, n):
        self.trackbacking("", n, n)
        return self.result
    def trackbacking(self, cur_str, left, right):
        if left == 0 and right == 0:
            self.result.append(cur_str)
            return
        if left > right: return
        if left > 0:
            self.trackbacking(cur_str + "(", left - 1, right)
        if right > 0:
            self.trackbacking(cur_str + ")", left, right - 1)

solution = Solution()
print(solution.solution(3))
