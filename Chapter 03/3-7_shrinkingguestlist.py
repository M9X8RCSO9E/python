guestlist = ['Ronald Reagan', 'Barrack Obama', 'Abraham Lincoln']

print(guestlist[2])

guestlist[2] = 'Bill Clinton'

print(guestlist)

print("we found a bigger table - more guests will join us!")

guestlist.insert(0, 'David Bowie')
guestlist.insert(2, 'Geddy Lee')
guestlist.insert(-1,'Robert Downey Jr')

print(guestlist)

print("Oh no! The bigger table isn't available.  I can only invite two folks.")

leave = guestlist.pop(0)
print(f"sorry we didn't have room {leave.title()}")
print(guestlist)

leave = guestlist.pop(0)
print(f"sorry we didn't have room {leave.title()}")
print(guestlist)

leave = guestlist.pop(0)
print(f"sorry we didn't have room {leave.title()}")
print(guestlist)

leave = guestlist.pop(0)
print(f"sorry we didn't have room {leave.title()}")
print(guestlist)

print(f"You guys are good to go {guestlist}")

del guestlist[1]
del guestlist[0]
print (f"No more guests. {guestlist}")