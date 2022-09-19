array1=[26,26,2,3,20];
array=sorted(array1,reverse=True);
present_element = array[0];
for i in array:
     next_element=array[array.index(i)+1]
     if next_element<present_element:
        present_element=i;
        break
     else:
         present_element=i;
print(present_element);



