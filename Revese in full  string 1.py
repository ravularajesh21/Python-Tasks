# Write a program to reverse the given string

# Approach 1

s = input('enter any string:') 
r = reversed(s)
output = ''.join(r)
print(output)


# Approach 2

S = input('enter any string:')
i = len(S)-1
target = ''
while i>0:
    target = target+S[i]
    i = i-1
print(target)


# Approach 3

Str = input('enter any string:')
i = len(Str)-1
ouput = ''
for x in Str:
    output = output+Str[i]
    i = i-1
print(output)