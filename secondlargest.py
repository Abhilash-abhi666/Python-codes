
def second_largest(array):
     array=sorted(array1,reverse=True);
     present_element = array[0];
     for i in array:
          next_element=array[array.index(i)+1]
          if next_element<present_element:
             present_element=i;
             break
          else:
              present_element=i;
     
     
def second_largest_avd(arr):
    sorted_arr=sorted(arr,reverse=True)
    for i in range(len(sorted_arr)-1):
        if sorted_arr[i] != sorted_arr[i+1]:
            return sorted_arr[i+1]
    return -1



print(second_largest([26,26,2,3,20]))
print(second_largest_avd([26,26,2,3,20]))
