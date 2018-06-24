def subarray(array,n):
  flag=0
  if 0 in array:
    pos=array.index(0)
    print ("\nOutput: true")
    print ("There is a subarray with zero sum from index %d to %d."%(pos,pos))
    exit(0)
  for i in range(0,n-1):
    sum1=array[i]
    for j in range(i+1,n):
      sum1=sum1+array[j]
      if sum1==0:
        print ("\nOutput: true")
        print ("There is a subarray with zero sum from index %d to %d."%(i,j))
        exit(0)
  if flag==0:
    print ("\nOutput: false")
    print ("There is no subarray with zero sum.")

array=[4, 2, -3, 1, 6]
#array=[4, 2, -3, 1, 6, 0, 0]
#array=[4, 2, 0, 1, 6]
#array=[-3, 2, 3, 1, 6]
print ("\nGiven array:",array)
n=len(array)
subarray(array,n)
