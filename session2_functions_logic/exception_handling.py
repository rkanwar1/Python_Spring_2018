
def factorial(n):
    if (n <= 1):
        return 1
    else:
        return n*factorial(n-1)

mstr = input("Enter a number: ")
m = int(mstr)
try:
    print('m! is',factorial(m),'.')
except:
    print('An error occurred.')

print("But the program continues!")
