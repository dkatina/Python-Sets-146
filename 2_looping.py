#Loop over sets the same way we loop over lists and tuples

aset = {'apple', 'orange', 'banana'}

for fruit in aset: #may see the items in random order due to the unordered nature of sets
    print(fruit)

#cant use a while loop to loop over sets, because sets dont have indices