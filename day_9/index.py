
setA =set()
length=len(setA)
setB=set()

while length < 5:
    item=input('enter an item to be added ')
    itemB=input('enter item in setB')
    setA.add(item)
    setB.add(itemB)
    print(setA,setB)
    intersect =setA & setB
    if intersect:
        print('elements common in a and b are:',intersect)
    else:
        print('oops no common elements')


