import sys
while True:
  s = input().split() # ⼀⾏⼀⾏读取
  a, b = int(s[0]), int(s[1])
  if not a or not b: # 遇到 0, 0 则中断
    break
  print(a + b)
