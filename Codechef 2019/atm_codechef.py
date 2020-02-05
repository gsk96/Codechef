a,b= input().split(" ")
amount = int(a)
balance = float(b)
bal=float(0)
if amount%5==0 and amount<=balance:
    bal = (balance - amount)- 0.5
    print("%.2f" % bal)
    #print(bal)
else:
    print("%.2f" % balance)

'''
l = input().split()
amount, balance = int(l[0]), float(l[1])
if amount % 5 == 0 and (amount + 0.5) <= balance:
	balance -= (amount + 0.5)
print("%.2f"%balance)
'''