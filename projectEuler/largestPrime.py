# factor search

num = int(input())

for i in range(2, num):
    for j in range(2, i):
        if i % j == 0:
            print(i, "equals", j, "*", i/j)
            break
    
    else:
        print(i, "is prime factor")