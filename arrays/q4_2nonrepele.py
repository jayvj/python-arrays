def twononrepele(list1):
  dict1={}
  for key in list1:
    if key not in dict1:
      dict1[key]=1
    else:
      dict1[key]=dict1[key]+1
  #print (dict1)
  nonreplist=[]
  for key,value in dict1.items():
    if value == 1:
      nonreplist.append(key)
  return nonreplist

list1=[3,4,2,7,3,2,6,7,3,7,3]
print ("\nGiven list: ",list1)
result=twononrepele(list1)
print ("\nTwo non-repeating elements in an array of repeating elements:"," ".join(map(str,result)))
