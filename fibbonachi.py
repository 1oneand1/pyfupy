#funciton to find the fibonacci number
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    #recursive case - formula 'F(n) = F(n-1) + F(n-2)'
n = int(input("Enter a positive integer:"))

#the fibonacci sequence~
print("The fibonacci sequence up to the", n, "th term is:")
for i in range(n):
    print(fibonacci(i), end=" ")
