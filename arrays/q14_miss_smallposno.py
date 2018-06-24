def smallmissno(array):
  posarr=[]
  for val in array:
    if val>0:
      posarr.append(val)
  print ("\nArray with positive numbers:",posarr)#0 is neither positive nor negative number
  mini=1
  while 1:
    if mini in array:
      mini=mini+1
    else:
      print ("\nThe least positive number missing in an array: %d"%mini)
      break

#array=[0,10,2,-10,-20]
#array=[2, 3, 7, 6, 8, -1, -10, 15]
array=[2, 3, -7, 6, 8, 1, -10, 15]
#array=[1, 1, 0, -1, -2]
#array=[-20,-10,-30]
#array=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print ("\nGiven array:",array)
smallmissno(array)
