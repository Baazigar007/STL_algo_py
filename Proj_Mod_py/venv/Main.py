import random
from Algos import GetMaxCarIndex
from TrafficControlG import NormalTrafficG,CongestedTrafficG
#from FinalOutput import Reset
from turtle import Turtle, Screen
from OutputDemo3 import Base,Back,Pole,HeadText,Reset


#Assuming that 20 cars can cross the intersection in 30 seconds
NormVal=20
'''
Intersection1=input("Vehicles on intersection 1 :")
Intersection2=input("Vehicles on intersection 2 :")
Intersection3=input("Vehicles on intersection 3 :")
Intersection4=input("Vehicles on intersection 4 :")
'''
Intersection1=random.randrange(0,100)
Intersection2=random.randrange(0,100)
Intersection3=random.randrange(0,100)
Intersection4=random.randrange(0,100)

List=[Intersection1,Intersection2,Intersection3,Intersection4]
MaxIndex=int(GetMaxCarIndex(List))

for i in range(0,4):
    print ("\tIntersection ",i+1," - ",List[i]," Cars")
print("\n")
#print ("Most cars in ",Index," Side")

screen=Screen()
screen.setup(1000,1000)

Base()
Pole()
Back()
HeadText()
if List[MaxIndex]<=NormVal :
    #print ("Normal Flow of traffic ")
    NormalTrafficG(List)
else :
    #print ("Congested flow of traffic ")
    CongestedTrafficG(List)
Reset()
screen.mainloop()
