import dis

def myFunction(x):
    y = x + 1
    return y * x

dis.dis(myFunction)

# print(myFunction(5))
