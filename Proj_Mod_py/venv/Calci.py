import math

def Mean(List):
    Sum=0
    for i in range(0,4):
        Sum=Sum+List[i]
    return Sum/4

def Variance(List):
    Sum=0
    MeanVal=Mean(List)
    for i in range(0,4):
        Sum=Sum+pow(List[i]-MeanVal,2)
    return Sum/4

def STDev(List):
    return math.sqrt(Variance(List))

def Interval(List):
    VarianceVal=Variance(List)
    if VarianceVal<200:
        return 40
    elif VarianceVal<400:
        return 60
    elif VarianceVal<900:
        return 75
    else:
        return 90
