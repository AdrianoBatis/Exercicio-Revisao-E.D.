import random
Lista1 = []
Lista2 = []
Lista3 = []

while len(Lista1) < 10:
    num = random.randint(1,20)
    if num not in Lista1:
        Lista1.append(num)
        Lista3.append(num)


while len(Lista2)  < 10:
    num = random.randint(1,20)
    if num not in Lista2:
        Lista2.append(num)
        Lista3.append(num)

Lista1.sort()        
Lista2.sort()
Lista3.sort()

print(Lista1)
print(Lista2)
print(Lista3)
