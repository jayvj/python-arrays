def hashkeyfunc(hashtable,key):
  return key%len(hashtable)

def insert(hashtable,key,value):
  hashkey=hashkeyfunc(hashtable,key)
  hashtable[hashkey].append(value)

hashtable=[[] for i in range(10)]
print ("\n",hashtable)
insert(hashtable,23,'Minion')
insert(hashtable,10,'Agnes')
insert(hashtable,12,'Jackie')
insert(hashtable,43,'Uncle')
print ("\n",hashtable)
print ("\n")
