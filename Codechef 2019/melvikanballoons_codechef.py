tc=int(input())
for i in range(tc):
    a = input()
    e = list(a)
    c = e.count("a")
    d = e.count("b")
    print(e)
    if c > d:
        print(d)
    elif c==d:
        print(c or d)
    else:
        print(c)    