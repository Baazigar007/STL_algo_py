from Colors import bcolors
import time
from Algos import GetMaxCarIndex
from Calci import Interval
from turtle import Turtle,Screen
from OutputDemo3 import Base,Back,Pole,Red,Yellow,Green



def NormalTrafficG(List):
    Gtime=30
    for i in range(0,4):
        if(List[i]>0):
            Green(i+1,List[i],List[i],Gtime)
            for j in range (0,4):
                if(j==i) :
                    continue
                else:
                    Red(j+1)
        time.sleep(Gtime/10)
        Yellow(i+1)
        time.sleep(2)

#NormalTraffic([0,32,12,32])

def CongestedTrafficG(List):
    #Gtime=30
    #MinIndex=GetMinCarIndex(List)
    for i in range(0,4):
        if(List[i]<=10) and (List[i]>0):
            Gtime=int(List[i]*3/2)*2
            Green(i+1,List[i],List[i],Gtime)
            for j in range(0, 4):
                if (j == i):
                    continue
                else:
                    Red(j+1)
            time.sleep(Gtime / 10)
            Yellow(i+1)
            time.sleep(2)
            Red(i+1)
            List[i]=0


    MaxIndex=GetMaxCarIndex(List)
    while(List[MaxIndex]>0):
        for i in range(0, 4):
            if (List[i] <= 5) and (List[i] > 0):
                Gtime = int(List[i] * 3 / 2) * 2
                Green(i + 1, List[i], List[i], Gtime)
                for j in range(0, 4):
                    if (j == i):
                        continue
                    else:
                        Red(j + 1)
                time.sleep(Gtime / 10)
                Yellow(i + 1)
                time.sleep(2)
                Red(i + 1)
                List[i] = 0
        Gtime=Interval(List)
        PassableCars=min(List[MaxIndex],round((Gtime*2)/3))
        Green(MaxIndex+1,List[MaxIndex],PassableCars,Gtime)
        for j in range(0, 4):
            if (j == MaxIndex):
                continue
            else:
                Red(j+1)
        time.sleep(Gtime / 10)
        Yellow(MaxIndex+1)
        time.sleep(2)
        List[MaxIndex]=List[MaxIndex]-PassableCars
        MaxIndex=GetMaxCarIndex(List)

    time.sleep(1)
