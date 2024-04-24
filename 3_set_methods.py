#Set methods

#Membership checks on sets : check to see if item in set, return True or False
#One of the primary reasons we use sets, because this happens instantaneously

my_set = {'superman', 'batman', 'wonder woman', 'the flash'}

print('superman' in my_set) #True


#-- set.add(item) : add items to a set
#If you try to add a duplicate item, it simply gets ignored
my_set.add('green lantern')
print(my_set)

my_set.add('superman') #nothing happens
print(my_set)

#-- set.update(iterable) : will add all the items of that iterable (set, tuple, string, list, dict)
#to my set

marvel = ['iron man', 'thor', 'loki', 'dr. strange']
my_set.update(marvel)
print(my_set)

movies = {'Avenger': 'Endgame', 'Far From Home': 'Spider-Man', 'Dark Knight': 'Batman'}
my_set.update(movies.keys()) # .keys(), .values() , .items() adds kvps as a tuple
print(my_set)

#-- set.remove(item) : removes an item from the set, will throw an KeyError if the
#item does not exist in the set

my_set.remove('loki')
print(my_set)

#my_set.remove('Thanos') #throws KeyError


#-- set.discard(item) : removes an item from the set, without throwing an error
#if the item doesn't exist

my_set.discard('green lantern')
print(my_set)

my_set.discard('Thanos') #nothing happens

#-- set.pop() : removes a random item from the set and returns it
#cant specify items, will throw a TypeError if you pass in an arg

rand = my_set.pop()
print(rand)
print(my_set)

#-- set.clear() : removes all items

my_set.clear()
print(my_set)
