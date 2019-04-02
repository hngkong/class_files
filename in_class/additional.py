# Instantiate two objects of MyClass as myobj1 and myobj2

# Display the default value of the attribute myVar for both the objects
# Then change the value of the myobj1 attribute to "Passed" and myobj2 to "Failed"

# Then print the attribute myVar for both the objects

class MyClass():

    myVar = "Example"

    def myOps(self):
        # placeholder

def main():

    myobj1 = MyClass()
    myobj2 = MyClass()

    print(myobj1.myVar)
    print(myobj2.myVar)

    myobj1.myVar = "Passed"
    myobj2.myVar = "Failed"

    print(myobj1.myVar)
    print(myobj2.myVar)

main()