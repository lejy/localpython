nums = list(map(int,input().split()))
target = int(input(""))

found = False
for i in nums:
    for j in nums:
        if (i+j) == target:
            print(i,j)
            found = True
            break
    if found:
        break