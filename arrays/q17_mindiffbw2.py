def mindiff(array,n):
  if n<2:
    print ("\nInsufficient input to find minimum difference")
    exit(0)
  maxno=array[1]
  minno=array[0]
  mindiff=maxno-minno
  for i in range(1,n-1):
    if  (array[i+1]-array[i])<mindiff:
      maxno=array[i+1]
      minno=array[i]
      mindiff=array[i+1]-array[i]
  print ("\nThe two numbers such that their difference is minimum are %d and %d"%(maxno,minno))
  print ("The difference is %d"%mindiff)

#array=[]
#array=[1]
array=[1, 5, 3, 19, 18, 25]
#array=[30, 5, 20, 9]
#array=[1, 19, -4, 31, 38, 25, 100]
print ("\nGiven array:",array)
array.sort()
print ("Sorted array:",array)
n=len(array)
mindiff(array,n)
