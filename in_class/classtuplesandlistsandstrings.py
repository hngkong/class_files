# header
#

def main():
    user_string = input("Enter a string:")

    print("This is what I found out about the string:")

    if user_string.isalnum():
        print("Alphanumerical")
    if user_string.isalpha():
        print("Only letters")
    if user_string.isdigit():
        print("Only digits")
    if user_string.isspace():
        print("Only whitespace")
    if user_string.islower():
        print("All lowercase")
    if user_string.isupper():
        print("Alphanumerical")

main()