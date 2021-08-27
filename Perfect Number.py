

number = int(input('enter the number:'))
result = 0
for x in range(1,number):
    if (number%x) == 0:
        result = result+x
if result == number:
    print(number,'It is perfect number')
else:
    print('It is not perfect number')
    
    
# Approach 2

for number in range(10001):
    result = 0
    for x in range(1,number):
        if (number%x) == 0:
            result = result+x
    if result == number:
        print(number,'is perfect number')    
        