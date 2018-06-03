def oddnotimes(numlist):
  dict1={}
  for key in numlist:
    if key not in dict1:
      dict1[key]=1
    else:
      dict1[key]=dict1[key]+1
  result=[]
  for key,val in dict1.items():
    if val%2 == 0:
      continue
    else:
      result.append(key)
  return result

print ("\nEnter numbers:")
numlist=[int(x) for x in input().split()]
result=oddnotimes(numlist)
print ("\nNumber Occurring Odd Number of Times:")
print (" ".join(map(str,result)))
