
# Three different variables “num” are defined in separate namespaces and accessed accordingly.

# num = 30
# num = 20
# num = 10
def outer_function():
    num=20

    def inner_function():
        num= 30

        print('num=', num)

    inner_function()
    print('num=',num)


num=10

outer_function()
print('num=', num)


# ANother Program to acess global Namespace
print("The global variable are")

def outer_function():
    global num
    num = 20

    def inner_function():
        global num
        num = 30
        print('num =', num)

    inner_function()
    print('num =', num)


num = 10
outer_function()
print('num =', num)
