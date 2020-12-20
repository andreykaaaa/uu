allcards=int(input("введите размер колоды карт : "))
cards=[random.randint(0,100) for i in range(allcards)]
firstpart = []
secpart = []
mixing = []
def printList (oneList):
    for elem in oneList:
        print(elem, end=' ')
    print()

def mix (twoList):
    if len(twoList)%2==1:
        twoList.append(random.randint(0,100))
    for i in range(1,len(twoList)+1):
        if i ==len(twoList)/2:
            for j in range(0,i):
                firstpart.append(twoList[j])
            for k in range(i,len(twoList)):
                secpart.append(twoList[k])
            firstpart.reverse()
            secpart.reverse()
            twoList=[firstpart + secpart for c in range(1) for d in range(1)]
    print(twoList)
