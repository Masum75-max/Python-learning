s = set()  #declaring an empty set
#set is unordered and unindexedd
s1={1,2,3,4,4,5}

print(s1)

s1.add(6)

print(s1)

s1.remove(3)

print(s1)


s1.discard(4) # removes 2 but if 2 is not present in set , then it wont give any error

print(s1)

s2 ={9,8,7,4,3}

s3= s1.union(s2)  # returns only the unique elements

print(s3)

s4=s1.intersection(s2)

print(s4) # returns only the common items

s5=s4.copy()

print(s5==s4)

s6={1,2}

print(s6.issubset(s1))

print(s1.issuperset(s6))
