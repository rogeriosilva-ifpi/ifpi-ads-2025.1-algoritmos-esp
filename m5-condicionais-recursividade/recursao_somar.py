def somar(n):
  if n == 1:
    return 1
  
  return n + somar(n - 1)



print(somar(1))
print(somar(3))
print(somar(10))
print(somar(5))