n = 3 # global variable
def func1():
    global n
    print(n)
    n = 4 # local variable
    print(n)

func1()
print(n)