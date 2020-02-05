sum_tri = 180
tc=int(input())
for i in range(tc):
    a,b,c=input().split(" ")
    #b=int(input())
    #c=int(input())
    sum = int(a)+int(b)+int(c)
    if sum_tri == sum:
        print("YES")
    else:
        print("NO")     
