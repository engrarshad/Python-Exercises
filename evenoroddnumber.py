# Check even or odd numbers
n = int(input("Enter the number : "))
def oddeven(n):
    if (n%2==0):
        return "This is even!"
    else:
        return "This is odd!"
print(oddeven(n))