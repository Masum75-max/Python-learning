

# set of data of any type

friends=["apple","orange",5,345.06,"akash","rohan"]

print(friends[0])
#  list is mutable


print(friends[0:4])

friends.append("masum") # adds an element at the last

print(friends)

friends.pop()  # pops out the last element

print(friends)


# friends.clear()     #  clears all the elements 

print(friends)

li_of_numbers= [1,3,2,4,5]

li_of_numbers.sort()
print(li_of_numbers)

li_of_numbers.reverse()
print(li_of_numbers)

no_of_one=li_of_numbers.count(1)

print(no_of_one)

print(li_of_numbers.index(3))

li_of_numbers.insert(2,10)

print(li_of_numbers)

print(li_of_numbers.pop(2))  ## pops out and returns the vaalue at index 2

print(li_of_numbers)

li_of_numbers.remove(5)  # will only remove the vaalue not the value at index

print(li_of_numbers)
print(len(li_of_numbers))

print(max(li_of_numbers))
print(min(li_of_numbers))


third = li_of_numbers + friends

print(third)


