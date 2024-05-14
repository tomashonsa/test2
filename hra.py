import random
p = []
k = 0

while k<=5:
     d = random.randint(0,5)
for x in range(d):
        p.append(random.randint(1,10))
        x = len(p)
        print(p)
        print(x)
        a=input("jaka je delka pole?")
        if a==p:
           print("správně")
           k+-1
        else:
           print("špatně")

    




