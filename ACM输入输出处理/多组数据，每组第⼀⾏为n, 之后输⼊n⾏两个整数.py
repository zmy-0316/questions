while 1:
  try:
    N = int(input())
    for i in range(N):
      l = list(map(int,input().split()))
      print(sum(l))
  except:
    break
