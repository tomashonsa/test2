import random
p = []
d = random.randint(0,5)
for x in range(d):
    p.append(random.randint(0,10))
print(p)
y = len(p)
print(y)
a = input("jaká je délka pole?")
a = int(a)

if a==y:
      print("správně")
else:
      print("špatně")


