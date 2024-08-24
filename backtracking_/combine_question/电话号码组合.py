"""
电话号码组合，输入一串数字字符串，输出电话号码所有可能的组合
1.是不同字符串间的组合问题，不需要startindex
2.需要index，记录遍历到输入字符串digits第几位了，递归终止条件：index = len(digits)
"""

class Solution:
    s = ""
    result = []
    letter = [ "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wsyz"]
    def combine(self, digits):
        if len(digits) == 0: return []
        self.backtracking(digits, 0)
        return self.result
    def backtracking(self, digits, index):
        if index == len(digits):
            self.result.append(self.s)
            return
        digit = int(digits[index])
        letters = self.letter[digit]
        for i in range(len(letters)):
            self.s += letters[i]
            self.backtracking(digits, index + 1)  #是index + 1，不是i + 1
            self.s = self.s[:-1]
solution = Solution()
print(solution.combine("23"))
