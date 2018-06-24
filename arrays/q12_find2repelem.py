def find2repele(array,totalsize):
  dic={}
  for key in array:
    if key not in dic:
      dic[key]=1
    else:
      dic[key]=dic[key]+1
  #print (dic)
  result=[]
  for key,val in dic.items():
    if val==2:
      result.append(key)
  print ("\nThe two repeating elements in a given array:"," ".join(map(str,result)))

n=6
array=[4,1,6,3,1,7,5,5]
print ("\nGiven array:",array)
totalsize=n+2
find2repele(array,totalsize)
