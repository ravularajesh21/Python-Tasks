## Convert string into uppercase without suing any predefined function

string=input('enter string:')
string2=''
for ch in string:
    if ch>='a' and ch<='z':
        ch=chr(ord(ch)-32)
        string2=string2+ch
    else:
        string2=string2+ch
print(string2)

## Convert string into lowercase without suing any predefined function

string=input('enter string:')
string2=''
for ch in string:
    if ch>='A' and ch<='Z':
        ch=chr(ord(ch)+32)
        string2=string2+ch
    else:
        string2=string2+ch
print(string2)
        