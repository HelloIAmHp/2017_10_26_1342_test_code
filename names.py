from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if 'q' == first:
        break
    else:
        last = input("Please give me a last name: ")
        formatted_name = get_formatted_name(first, last)
        print("hello, " + formatted_name + ".")
