#Sets are a collection datatype in python, that can be immutable/mutable, unordered, unindexable, and all
#items within a set must be unique and 


#Characteristics:
#-- Unordered : Items in sets have no order and there for cannot be indexed into
#-- Mutable : You can change how many items a set has, and remove said items
#-- All elements in a set need to be unique, converting a list into a set will remove
#all duplicate items from the set
#-- All elements inside the set must be immutable

#Why bother:
#-- ensures elements are unique
#-- instantaneous membership checks
#-- straight forward comparison operations


#Creating Sets

pop_set = {'one', ('this','that','other'), 'three'} #sets use curly braces, itmes separated by commas
print(pop_set)
print(type(pop_set))

empty_set = set()   #define empty sets with the set() constructor since {} is a dict
print(type(empty_set))


alist = ['item', 'item', 'stuff', 'thing', 'oddity']
set_list = set(alist)
alist = list(set_list) #the items will 'float' around since they don't have a specified order
print(alist)

atuple = ('item', 'item', 'stuff', 'thing', 'oddity')
set_tup = set(atuple)
atuple = tuple(set_tup)
print(atuple)




