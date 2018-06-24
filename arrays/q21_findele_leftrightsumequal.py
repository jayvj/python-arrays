def partitionelem(array,n):
  if n<3:
    print ("\nInsufficient input to find an element in the given array such that sum of left array is equal to sum of right array")
    exit(0)
  i=1
  flag=0
  while i<n-1:
    partition=array[i]
    leftarr=[]
    rightarr=[]
    leftsum=0
    rightsum=0
    for j in range(0,i):
      leftarr.append(array[j])
      leftsum=leftsum+array[j]
    for k in range(i+1,n):
      rightarr.append(array[k])
      rightsum=rightsum+array[k]
    if leftsum==rightsum:
      print ("\nAn element in array such that sum of left array is equal to sum of right array:%d"%partition)
      print ("\nSubarrays are:",(leftarr,rightarr))
      exit(0)
    i=i+1
  if flag==0:
    print ("\nThere is no element in array such that sum of left array is equal to sum of right array.")


array=[1,4,2,5]
#array=[2,3,4,1,4,5]
#array=[1,2,3,4]
print ("\nGiven array:",array)
n=len(array)
partitionelem(array,n)
