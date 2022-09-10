def countwithoutSC (sen):
    b=0
    for i in range(len(sentence)):
        a = ord(sentence[i])
        if ((a>64 and a<91) or (a>97 and a<123) or (a>47 and a<56)):
            b+=1
    return b

def noofwords(sen):
    p=1
    for i in sen:
       if (i==' '):
          p+=1
    return p

sentence="So, R u ok?"
m=countwithoutSC(sentence)
n=noofwords(sentence)
x=m/n
print(m,n,x)

