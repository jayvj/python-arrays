def hashpairsum(list1,X,n,hashtable):
  k=0
  for i in range(0,n):
    for j in range(i+1,n):
      sum1=list1[i]+list1[j]
      hashtable[k].append(sum1)
      hashtable[k].append(i)
      hashtable[k].append(j)
      k=k+1
  #print (hashtable)
  res=[]
  for i in range(0,k):
    currsum=hashtable[i][0]
    remainsum=X-currsum
    for j in range(i+1,k):
      if remainsum==hashtable[j][0] and (hashtable[i][1]!=hashtable[j][1] and hashtable[i][1]!=hashtable[j][2] and hashtable[i][2]!=hashtable[j][1] and hashtable[i][2]!=hashtable[j][2]):
        val1=hashtable[i][1]
        val2=hashtable[i][2]
        val3=hashtable[j][1]
        val4=hashtable[j][2]
        #print ("(%d,%d,%d,%d)"%(val1,val2,val3,val4))
        if (list1[val1] in res) and (list1[val2] in res) and (list1[val3] in res) and (list1[val4] in res):
          continue
        else: 
          print ("\nFour elements that sum to a given value %d:(%d,%d,%d,%d)"%(X,list1[val1],list1[val2],list1[val3],list1[val4]))
          res.append(list1[val1])
          res.append(list1[val2])
          res.append(list1[val3])
          res.append(list1[val4])


list1=[3,2,1,18,4,14,6,5,7]
#list1=[10, 20, 30, 40, 1, 2]
#X=91
X=14
print ("\nGiven array:",list1)
print ("Given sum is %d"%X)
n=len(list1)
hashtablesize=n*(n-1)//2
hashtable=[[] for i in range(hashtablesize)]
hashpairsum(list1,X,n,hashtable)
