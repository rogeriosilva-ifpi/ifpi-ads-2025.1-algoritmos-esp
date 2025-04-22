def countdown(n):
  print(n)
  if n > 1:
    countdown(n - 1)
  


try:
  countdown(10001)
except RecursionError:
  print(1)