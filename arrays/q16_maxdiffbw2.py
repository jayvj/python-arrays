def maxdiff(array):
  while len(array)!=1: 
    maxno=max(array)
    maxpos=array.index(maxno)
    if maxpos==0:
      array.remove(maxno)
      continue
    else:  
      minno=min(array)
      minpos=array.index(minno)
      diff=maxno-minno
      print ("\nMaximum difference between two elements such that larger element appears after the smaller number:%d and %d"%(maxno,minno))
      print ("\nMaximum difference  is %d"%diff)
      exit(0)
  print ("\nThere is no larger elements appears after the smaller number in the given array.")

array=[12,3,2,1,5,4]
#array=[12,11,10,1]
print ("\nGiven array:",array)
maxdiff(array)
