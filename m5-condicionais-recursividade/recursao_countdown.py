def countdown(n):
  if n == 0:
    return
  
  print(n)
  countdown(n - 1)
  


try:
  countdown(10001)
except RecursionError:
  print(1)