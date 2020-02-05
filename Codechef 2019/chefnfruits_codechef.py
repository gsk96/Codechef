tc = int(input())

for i in range(tc):

    a,o,c= input().split(" ")

    coins = int(c)

    apple = int(a)

    orange = int(o)

    while coins > 0:

        if apple > orange:

            coins -= 1

            apple -= 1

        elif apple == orange:

            coins -= 1
      
            apple -= 1

        else :

            coins -= 1

            orange -= 1

    result=abs(apple-orange)

print(result)