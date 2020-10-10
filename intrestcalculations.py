# Intrest calculator

principal=int(input('enter starting value: '))
interest=float(input('enter interest rate: '))
years=int(input('how many years?: '))

for x in range(1,years+1):
    principal= (principal*((100+interest)/100))
    print(principal)