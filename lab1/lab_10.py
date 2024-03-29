
#9. WAP program to sum all items in a list

input_str = input("Enter a list of numbers separated by SPACES: ")

myList = [int(x) for x in input_str.split()]


listSum = sum(myList)

# Print the sum
print("Sum of all items in the list:", listSum);

