def factorial(a):
    if a<2:
        return 1
    else:
        return a*(factorial(a-1))

result = factorial(5)
print ('Factorial of 5 is: ',result)
