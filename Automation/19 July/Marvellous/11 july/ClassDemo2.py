class Demo :
    def __init__(self):
        print("Inside the Constructor")
    def __del__(self):
        print("Inside the Destructor")
obj1 = Demo()
obj2 = Demo()

print("End of Application")