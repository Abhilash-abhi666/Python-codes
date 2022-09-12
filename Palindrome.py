i_string="ana"
r_string=reversed(i_string)
length=len(i_string)
count=0
for i,j in zip(i_string,r_string):
    if i!=j:
        print('Not palindrome')
        break
    elif i==j and count!=length-1:
            count += 1
    else:
            print('palindrome')
            
            
def pal(string): # AVD
    left = 0
    right = len(string)-1
    
    while left<right:
        if string[left] != string[right]:
            return False
    return True


