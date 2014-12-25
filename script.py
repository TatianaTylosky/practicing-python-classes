import cat_adoption

#made the pet store
ihazcatz = cat_adoption.Pet_store ("IHazCatz", 3000)

#made new cats
fluffy = cat_adoption.Cat("Fluffy", "orange", 20)
poofykins = cat_adoption.Cat("Poofykins", "white", 15)

ihazcatz.cats.append(fluffy)
ihazcatz.cats.append(poofykins)

#ihazcatz.cats.fluffy = cats.Cat("Fluffy", "white", 20)

print "Name: " + ihazcatz.cats[0].name
print "Color: " + ihazcatz.cats[0].color
print "Weight: " + str(ihazcatz.cats[0].weight)

print ihazcatz.cats
