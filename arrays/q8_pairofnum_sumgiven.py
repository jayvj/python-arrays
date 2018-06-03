def pairofnum(list1,X):
  s=set()
  for val in list1:
    temp=X-val
    if (temp>=0) and (temp in s):
      print ("\nPair of numbers with given sum %d:(%d,%d)"%(X,val,temp))
    s.add(val)

X=16
list1=[4,5,15,2,6,12,1]
print ("\nGiven list: ",list1)
print ("Given sum is %d"%X)
pairofnum(list1,X)