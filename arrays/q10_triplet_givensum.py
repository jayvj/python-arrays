def findtriplet(list1,length,sum1):
  for i in range(length):
    for j in range(i+1,length):
      for k in range(j+1,length):
        if list1[i]+list1[j]+list1[k]==sum1:
          print ("\nTriplet that sum to a given value %d: (%d,%d,%d)"%(sum1,list1[i],list1[j],list1[k]))
          return True
  print ("\nThere is no triplet that sum to a given value: %d"%sum1)
  return False

list1=[12,3,4,1,6,9]
sum1=24
print ("\nGiven array:",list1)
print ("\nGiven sum is %d"%sum1)
length=len(list1)
if findtriplet(list1,length,sum1):
  print ("True")
else:
  print ("False")
