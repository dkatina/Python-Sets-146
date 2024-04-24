#Set Operations

#merge sets 'specifically'
set1 ={-1,0,1,2,3,4}
set2 = {1,2,3,4,5,6,7}




#-- set1.union(set2) : returns set of all items from set1 and set2
#does not effect original sets
new_set = set1.union(set2)
print(new_set)

#-- set1.intersection(set2) : return set of all the items set1 and set2 have in common

intersect = set1.intersection(set2)
print(intersect)

#-- set1.difference(set2) : return all the items only from set1 that are different
#from the items in set2

diff_set = set1.difference(set2)
print(diff_set)


#-- set.symetric_difference(set2) : returns a set of all the items from both sets
#that don't overlap (not in common)

sym_diff_set = set1.symmetric_difference(set2)
print(sym_diff_set)

sym_diff_set.add(10)
print(sym_diff_set)