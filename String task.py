# The total number of occurrences of the string



s = input('enter main string:')
subs = input('enter sub string:')
n = len(s)
position = 0
count = 0
while True:
    i = s.find(subs,position,n)
    if i == -1:
        break
    else:
        print('found at index:',i)
        position = i+len(subs)
        count = count+1
print('The total number of occurrences:',count)
        