fibo = []
total = []
x, y = 1, 2

while x <= 4000000:
    fibo.append(x)
    fibo.append(y)
    x += y
    y += x

for i in fibo:
    if i % 2 == 0:
        total.append(i)

print(sum(total))

