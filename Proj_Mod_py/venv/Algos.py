
def GetMaxCarIndex(List):
    IndexVal=0
    Max=List[0]
    for i in range(1,4) :
        if(Max<List[i]):
            IndexVal=i
            Max=List[i]
    return IndexVal

def GetMinCarIndex(List):
    IndexVal = 0
    Min = List[0]
    for i in range(1, 4):
        if (Min > List[i]):
            IndexVal = i
            Min = List[i]
    return IndexVal


