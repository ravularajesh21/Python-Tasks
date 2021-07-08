# To reverse internal content of each word

s = 'Learning python is very easy'
l = s.split()
l1 = []
for x in l:
    l1.append(x[::-1])
output = ' '.join(l1)
print(output)