def max1s(bool2darr,nrow,mcol):
  resarr=[]
  for i in range(nrow):
    dic={}
    for j in range(mcol):
      if bool2darr[i][j]!=1:
        continue
      elif bool2darr[i][j] not in dic:
          key=bool2darr[i][j]
          dic[key]=1
      else:
        key=bool2darr[i][j]
        dic[key]=dic[key]+1
    val=dic.get(1)
    if val==None:
      continue
    resarr.append(val)
  if len(resarr)==0:
    print ("\nThere is no row(s) present with maximum number of 1s in a 2D row-wise sorted matrix.")
    exit(0)
  m=max(resarr)
  result=[i for i,j in enumerate(resarr) if j==m]
  print ("\nThe row(s) with maximum number of 1s in a 2D row-wise sorted matrix is(are):",(" ".join(map(str,result))))
  

bool2darr=[[0,0,0,1],[1,1,1,1],[0,1,1,1],[0,1,1,1],[1,1,1,1]]
#bool2darr=[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
nrow=len(bool2darr)
mcol=len(bool2darr[0])
print ("\nGiven 2D row-wise sorted matrix is:",bool2darr)
max1s(bool2darr,nrow,mcol)

bool2darr=[[0,0],[0,0]]
nrow=len(bool2darr)
mcol=len(bool2darr[0])
print ("\nGiven 2D row-wise sorted matrix is:",bool2darr)
max1s(bool2darr,nrow,mcol)

