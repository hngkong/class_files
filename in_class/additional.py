# Instantiate two objects of MyClass as myobj1 and myobj2

# Display the default value of the attribute myVar for both the objects
# Then change the value of the myobj1 attribute to "Passed" and myobj2 to "Failed"

# Then print the attribute myVar for both the objects

class MyClass():

    # Initial variable setup
    myVar = "Example"

def main():

    # Instantiate two objects of the MyClass() type
    myobj1 = MyClass()
    myobj2 = MyClass()

    # Print the default values of myVar for both objects
    print("Attribute within myobj1:", myobj1.myVar)
    print("Attribute within myobj2:", myobj2.myVar)

    # Change the values of myVar for both objects
    myobj1.myVar = "Passed"
    myobj2.myVar = "Failed"

    # Print the values of myVar for both objects again
    print("Attribute within myobj1:", myobj1.myVar)
    print("Attribute within myobj2:", myobj2.myVar)

main()