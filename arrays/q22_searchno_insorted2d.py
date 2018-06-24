def searchno(arr2d,n,x):
  i=0
  j=n-1
  while i<n and j>=0:
    if arr2d[i][j]==x:
      print ("\nFound at (%d,%d)"%(i,j))
      return 1
    if arr2d[i][j]>x:
      j=j-1
    else:
      i=i+1
  print ("\nElement not found")
  return 0


arr2d=[[10,20,30,40],[15,25,35,45],[27,29,37,48],[32,33,39,50]]
n=len(arr2d)
print ("\nGiven %d x %d row wise and column wise sorted matrix:"%(n,n))
print (arr2d)
x=29
#x=100
#x=50
print ("\nNumber to be searched in the above given matrix is %d"%x)
searchno(arr2d,n,x)
