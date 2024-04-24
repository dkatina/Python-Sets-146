#Advnaced set methods

#used to compare 2 sets

#-- set1.issubset(set2) : returns True if all items from set1 can be found in set 2 else False

set1 ={1,2,3,4}
set2 = {1,2,3,4,5,6,7}

print(set1.issubset(set2)) #True

#-- set1.issuperset(set2) : returns True if set1 contains all items from set2 else False

set1 ={1,2,3,4}
set2 = {1,2,3,4,5,6,7}

print(set1.issuperset(set2)) #False

#-- set1.isdisjoint(set2) : Returns True if there no common items between the sets

set1 = {1,2,3,4}
set2 = {1,2,3,4,5,6,7}

print(set1.isdisjoint(set2))


fruit_set = {'apple', 'banana', 'pear'}
veg_set = {'carrots', 'potatos', 'broccoli'}

print(fruit_set.isdisjoint(veg_set))


#tuples : ()
#lists : []
#sets : {item}
#dictionaries : {key:value}