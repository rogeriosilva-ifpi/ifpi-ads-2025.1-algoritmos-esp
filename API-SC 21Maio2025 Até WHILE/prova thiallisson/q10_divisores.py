def teste(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count

a = int(input())
b = int(input())

if b > a + 10:
    for num in range(a,b + 1):
        print(f"{num}, {teste(num)}")
else:
        print("erro")