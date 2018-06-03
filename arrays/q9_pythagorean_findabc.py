def findabc(list1,length):
  sqlist1=[i**2 for i in list1]
  print ("Squarelist of the above given array:",sqlist1)
  for i in range(0,length):
    for j in range(i+1,length):
      for k in range(j+1,length):
        a=sqlist1[i]
        b=sqlist1[j]
        c=sqlist1[k]
        if a==b+c or b==a+c or c==a+b:
          print ("\nThere is a Pythagorean triplet (%d,%d,%d)"%(a,b,c))
          return 1
  print ("\nThere is no Pythagorean triplet")
  return 0

list1=[3,1,4,6,5]
print ("\nGiven list:",list1)
length=len(list1)
if findabc(list1,length):
  print ("True")
else:
  print ("False")
