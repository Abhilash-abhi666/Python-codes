listof_num=[1,1,3,3,4,5,6]
n=len(listof_num)
mean=sum(listof_num)/n
#median
sortedlist=sorted(listof_num,reverse=True)
median=0
if (n%2 !=0):
    median=sortedlist[int(n/2)]
else:
    median=(sortedlist[int(n/2)]+sortedlist[int((n-1)/2)])/2
print('Value of mean is ' + str(mean))
print('value of median is ' + str(median))
#Mode
dic={}
maxa={}
for i in sortedlist:
    dic[i]=sortedlist.count(i)
    print(dic)
maxa=max(dic.values())
if maxa==1:
    print ("no Mode exists")
else:
    for i,j in dic.items():
        if j>1:
            print ('value of mode is ' + str(i) + '  ' + str(j))

