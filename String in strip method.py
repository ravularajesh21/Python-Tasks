# Using strip method

city = input('enter city name:').strip()
if city ==  'Hyderabad':
    print('Hello Hyderabadi')
elif city == 'chennai':
    print('Hello Madrasi')
else:
    print('your entered city is invalid')
    
# find method

s = 'Learning python very is python very easy python'

print(s.rfind('python'))

s = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaa'
print(s.find('b'))

# Approach     

s = input('enter main string:')
subs = input('enter sub string:')
n = len(s)

count = 0

while True :
    i = s.find(subs,count,n)
    if i == -1:
        break
    else:
        print('found at index:',i)
        count = i+len(subs)
        count = count+1
print('The total number of occurrences:'.count)
