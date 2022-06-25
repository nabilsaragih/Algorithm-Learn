# givenStr = str(input())
# n = list(givenStr)

# my_Dict = {i:n.count(i) for i in n}
# my_DictValues = list(my_Dict.values())
# highestValue = max(my_DictValues)

# print(highestValue)

a = list(input())

count = 0
ma = 0

for i in range(len(a)-1):

    if a[i] == a[i+1]:
        count += 1
        if ma <= count:
            ma = count
    elif a[i] != a[i+1]:
        count = 0



print(ma+1)