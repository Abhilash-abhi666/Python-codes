i=0; a=-1
def recu(i):
    global input_string,l,a
    a = a + 1
    print(a)
    print(i)
    if i>1:
       if input_string[i]!=input_string[a]:
           return 0
    else:
        return 1
    return 1*recu(i-1)

def pal(string):  # AVD
    if len(string)<=1:
        return True
    return (string[0]==string[-1]) and pal(string[1:-1])

input_string="madam"
l=len(input_string)-1
flag=recu(l)
if flag==1:
    print('palindrome')
else:
    print('not palindrome')
