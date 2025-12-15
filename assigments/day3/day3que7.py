
def factorial(n):
    if n == 0 or n == 1:  
        return 1
    else:
        return n * factorial(n - 1)



def power(base, exp):
    if exp == 0:         
        return 1
    else:
        return base * power(base, exp - 1)



num = 5
print("Factorial of", num, "=", factorial(num))

base = 2
exponent = 4
print(base, "power", exponent, "=", power(base, exponent))
