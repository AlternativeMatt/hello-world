friends = {"Anne", "Bob", "Ralph"}
abroad = {"Anne", "Bob"}

local = {"Ralph"}
local_friends = friends.difference(abroad)
locla2=abroad.difference(friends)
friends2 = local.union(abroad)

print (local_friends, locla2,friends2)

art = {"Adam", "Jen", "Bob", "Charlie"}
science = {"Bob", "Anne", "Micky", "Jen"}

both = art.intersection(science)
print(both)

