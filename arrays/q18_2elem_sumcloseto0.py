import sys
def minsum(array,n):
  if n<2:
    print ("\nInsufficient input to find sum which is closest to zero")
    exit(0)
  no1=array[0]
  no2=array[1]
  minsum=sys.maxsize
  for i in range(0,n-1):
    for j in range(i+1,n):
      sum1=array[i]+array[j]
      if abs(sum1)<abs(minsum):
        minsum=sum1
        no1=array[i]
        no2=array[j]
  print ("\nThe two elements whose sum is closest to zero are %d and %d"%(no1,no2))
  print ("The sum which is closest to zero is %d"%minsum)


array=[1, 60, -10, 70, -80, 85]
#array=[4]
#array=[]
#array=[5,2,-5]
print ("\nGiven array:",array)
n=len(array)
minsum(array,n)
