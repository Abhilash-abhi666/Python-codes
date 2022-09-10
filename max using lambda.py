listof_num=[1,2,3,4,5,6]
n=len(listof_num)
mean=sum(listof_num)/n
#median
sortedlist=sorted(listof_num,reverse=True)

#Mode
dic={}
maxa={}
for i in sortedlist:
    dic[i]=sortedlist.count(i)
maxa=max(dic.values())
print(dic)
keymax=max(dic,key=lambda x:x[1])
print(keymax)

