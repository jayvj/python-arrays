def missingno(list1,length,minno):
  totalsum=0
  for i in range(length+1):
    totalsum=totalsum+minno
    minno=minno+1
  #print (totalsum)
  sumlist=sum(list1)
  #print (sumlist)
  missnum=totalsum-sumlist
  return missnum

list1=[125,128,121,127,123,129,130,122,126]
#list1=[1,2,3,4]
minno=min(list1)
print ("\nGiven List: ",list1)
length=len(list1)
result=missingno(list1,length,minno)
print ("\nMissing number: %d"%result)
