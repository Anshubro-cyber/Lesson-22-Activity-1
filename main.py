n = int(input("Input your number:"))

digits = len(str(n))
resultNumber = 0

temp = n
while temp > 0:
    digit = temp % 10
    resultNumber += digit**digit
    temp //=10

if n == resultNumber:
    print(n,"is an Armstrong Number.")

else:
    print(n,"is not an Armstrong number.")
