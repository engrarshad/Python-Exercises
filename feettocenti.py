# A Python program to convert height (in feet and inches) to centimeters

height1 = float(input("please height in feet:"))
height2 = float(input("please height in inches:"))
def convert(x, y):
    return (x*30.48)+(y*2.54)
print("Its height is equal to: ",round(convert(height1,height2)), " in centimeters")