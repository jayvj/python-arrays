def find3ijk(array,n):
  result=[]
  for i in range(0,n-2):
    for j in range(i+1,n-1):
      for k in range(j+1,n):
        if array[i]<array[j] and array[j]<array[k]:
          temp=[]
          temp.append(array[i])
          temp.append(array[j])
          temp.append(array[k])
          result.append(temp)
  if len(result)==0:
    print ("\nNo such triplet")
  if len(result)>0:
    print ("\nThe 3 elements such that a[i] < a[j] < a[k] and i < j < k: %d, %d, %d"%(result[0][0],result[0][1],result[0][2]))
  #print (result)

#array=[3,1,4,2]
#array=[4,3,2,1]
array=[12, 11, 10, 5, 6, 2, 30]
#array=[1,2,3,4]
print ("\nGiven array:",array)
n=len(array)
find3ijk(array,n)
