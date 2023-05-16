def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

print("Enter two numbers: ", end="")
nOne = int(input())
nTwo = int(input())
print("Enter the operation: ", end="")
op = int(input())
if op == 1:
    print(add(nOne,nTwo))
elif op == 2:
    print(sub(nOne,nTwo))
elif op == 3:
    print(mul(nOne,nTwo))
elif op == 4:
    print(div(nOne,nTwo))
else:
    print("Invalid option")
    
