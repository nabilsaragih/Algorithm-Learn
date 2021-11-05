n = int(input())
number = []

def weirdAlgorithm(n):
    number.append(int(n))
    while n != 1:
        if n % 2 == 0:
            n /= 2
            number.append(int(n))
        else:
            n = n * 3 + 1
            number.append(int(n))

weirdAlgorithm(n)
stringInts = [str(int) for int in number]
strOfInts = " ".join(stringInts)

print(strOfInts)
