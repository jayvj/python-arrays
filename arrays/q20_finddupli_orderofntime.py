import collections
def finddupli(array):
  countarr=collections.Counter(array)
  #print (countarr)
  result=[i for i in countarr if countarr[i]>1]
  if len(result)==0:
    print ("\nThere is no Duplicates in O(n) time in the given array.")
    exit(0)
  print ("\nDuplicates in O(n) time in the given array:"," ".join(map(str,result)))


array=[1, 2, 3, 1, 3, 6, 6]
#array=[1,2,3,4]
print ("\nGiven array:",array)
finddupli(array)
