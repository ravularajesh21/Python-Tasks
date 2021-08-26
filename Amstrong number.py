# Aprroach 1

x = int(input('enter number:'))
i = x
result = 0
n = len(str(x))
while x!=0:
    digit = x%10
    result = result+digit**n
    x = x//10
    
if i == result:
    print('It is amstring number is',i)
else:
    print('It is not amstrong number')
    
# Aprroach 2

for x in range(10001):
    i = x
    result = 0
    n = len(str(x))
    while (x!=0):
        digit = x%10
        result = result+digit**n
        x = x//10
    if i == result:
        print(i)    