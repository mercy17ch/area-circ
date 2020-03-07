"""
import math

print("")
print("area of circle")
#function for area of circle
def AreaCircle(r):# r is the argument
    a=r**2*math.pi
    return a
print(AreaCircle(5))
print(AreaCircle(10))
print('')
print("perimeterofrecttangle")
#perimeterofrectangle

"""

def Perimeterofrectangle(l,w):
    perimeter=2*(l+w)
    return perimeter

#user input l,w
l=float(input("enter the length="))
w=float(input("enter the width="))

print("perimeterofrectangle=",Perimeterofrectangle(l,w))

print("")
print("VOLUME OF CUBOID")
def VolumeCuboid(l,w,h):
    v=l*w*h
    return v

l=float(input("enter the length="))
w=float(input("enter the width="))
h=float(input("enter the height="))

print("volume of the cuboid=",VolumeCuboid(l,w,h))