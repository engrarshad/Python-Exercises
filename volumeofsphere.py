# Volume of sphere = 4/3 *pi*r3

from math import *

def sphere_volume(radius):

    volume = 4.0 / 3.0 * pi * radius ** 3
    return volume

rad = float(input("Enter the radius of Sphere: "))
vol = sphere_volume(rad)
print(vol)
