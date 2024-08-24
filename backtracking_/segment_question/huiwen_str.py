"""
分割回文子串
"""

class Solution:
    def combine(self, s):
        result = []
        self.backtracking(s, 0, [], result)
        return result
    def backtracking(self, s, startindex, path, result):
        if startindex == len(s):
            result.append(path[:])
            return
        for i in range(startindex, len(s)):
            if s[startindex: i + 1] == s[startindex: i + 1][::-1]:
                path.append(s[startindex: i + 1])
                self.backtracking(s, i + 1, path, result)
                path.pop()



solution = Solution()
print(solution.combine("aab"))
