tc=int(input())
for i in range(tc):
    n = input()
    d = list(n)
    sum = 0
    for i in d:
        sum = sum + int(i)
    print(sum)