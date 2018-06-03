def twooddoccur(list1):
  dict1={}
  for key in list1:
    if key not in dict1:
      dict1[key]=1
    else:
      dict1[key]=dict1[key]+1
  print (dict1)
  result=[]
  for key,value in dict1.items():
    if value%2==0:
      continue
    else:
      result.append(key)
  return result

list1=[3,8,-4,0,3,-4,0,0,-4,8,8,8,-4,-4]
print ("\nGiven list: ",list1)
result=twooddoccur(list1)
print ("\nTwo numbers with odd occurrences in an unsorted array:"," ".join(map(str,result)))
