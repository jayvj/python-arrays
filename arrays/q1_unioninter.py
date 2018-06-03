def ui(arr1,arr2,m,n):
  i,j=0,0
  unionarr=[]
  interarr=[]
  while i<m and j<n:
    if arr1[i]<arr2[j]:
      unionarr.append(arr1[i])
      i=i+1
    elif arr1[i]>arr2[j]:
      unionarr.append(arr2[j])
      j=j+1
    else:
      unionarr.append(arr2[j])
      interarr.append(arr2[j])
      i=i+1
      j=j+1
  while i<m:
    unionarr.append(arr1[i])
    i=i+1
  while j<n:
    unionarr.append(arr2[j])
    j=j+1
  print ("\nUnion: ",unionarr)
  print ("Intersection: ",interarr)
  print ("\n")

print ("\nEnter array1 values:")
arr1=[int(x) for x in input().split()]
print ("Enter array2 values:")
arr2=[int(x) for x in input().split()]
print ("\nArray1: ",arr1)
print ("Array2: ",arr2)
m=len(arr1)
n=len(arr2)
ui(arr1,arr2,m,n)
