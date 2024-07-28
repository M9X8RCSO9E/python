guestlist = ['Ronald Reagan', 'Barrack Obama', 'Abraham Lincoln']

print(guestlist[2])

guestlist[2] = 'Bill Clinton'

print(guestlist)

print("we found a bigger table - more guests will join us!")

guestlist.insert(0, 'David Bowie')
guestlist.insert(2, 'Geddy Lee')
guestlist.insert(-1,'Robert Downey Jr')

print(guestlist)