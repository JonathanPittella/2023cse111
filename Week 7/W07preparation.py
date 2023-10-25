def main():
   # Create a list that contains five strings.
    color = ["yellow", "red", "green", "yellow", "blue"]

    # Call the built-in len function
    # and print the length of the list.
    lenght = len(color)
    print(f"Number of element:{lenght}")

    # Print the element that is stored
    # at index 2 in the colors list.
    print(color[2])

    # Change the element that is stored at
    # index 3 from "yellow" to "purple".

    color[3] = "purple"

    # Print the entire colors list.
    print(color)

# Call main to start this program.
if __name__ == "__main__":
    main()

print()

def main():
    # Create an empty list that will hold fabric names.
    fabrics = []

    # Add three elements at the end of the fabrics list.
    fabrics.append("velvet")
    fabrics.append("denim")
    fabrics.append("gingham")

    # Insert an element at the beginning of the fabrics list.
    fabrics.insert(0, "chiffon")
    print(fabrics)

    # Determine if gingham is in the fabrics list.
    if "gingham" in fabrics:
        print("gingham is in the list.")
    else: 
        print("gingham is NOT in the list.")

    # Get the index where velvet is stored in the fabrics list.
    i = fabrics.index("velvet")

    # Replace velvet with taffeta.
    fabrics[i] = "taffeta"

    # Remove the last element from the fabrics list.
    fabrics.pop()

    # Remove denim from the fabrics list.
    fabrics.remove("denim")

    # Get the length of the fabrics list and print it.
    n = len(fabrics)
    print(f"The fabrics list contains {n} elements.")
    print(fabrics)

# Call main to start this program.
if __name__ == "__main__":
    main()

print()

# Example 3

def main():
    # Create a list of color names.
    colors = ["red", "orange", "yellow", "green", "blue"]

    # Use a for loop to print each element in the list.
    for color in colors:
        print(color)


# Call main to start this program.
if __name__ == "__main__":
    main()

print()

# Example 4

def main():
    # Count from zero to nine by one.
    for i in range(10):
        print(i)
    print()

    # Count from five to nine by one.
    for i in range(5, 10):
        print(i)
    print()

    # Count from zero to eight by two.
    for i in range(0, 10, 2):
        print(i)
    print()

    # Count from 100 down to 70 by three.
    for i in range(100, 69, -3):
        print(i)


# Call main to start this program.
if __name__ == "__main__":
    main()

print()

# Example 5

def main():
    # Create a list of color names.
    colors = ["red", "orange", "yellow", "green", "blue"]

    # Use a for loop to print each element in the list.
    for color in colors:
        print(color)

    print()

    # Use a different for loop to
    # print each element in the list.
    for i in range(len(colors)):
        # Use the index i to retrieve
        # an element from the list.
        color = colors[i]

        print(color)


# Call main to start this program.
if __name__ == "__main__":
    main()

print()

# Example 6

def main():
    sum = 0

    # Get ten or fewer numbers from the user and
    # add them together.
    for i in range(10):
        number = float(input("Please enter a number: "))
        if number == 0:
            break
        sum += number

    # Print the sum of the numbers for the user to see.
    print(f"sum: {sum}")


# Call main to start this program.
if __name__ == "__main__":
    main()

print()

# Example 7

def main():
    list1 = ["red", "orange", "yellow", "green", "blue"]
    list2 = ["red", "orange", "green", "green", "blue"]

    index = compare_lists(list1, list2)
    if index == -1:
        print("The contents of list1 and list2 are equal")
    else:
        print(f"list1 and list2 differ at index {index}")


def compare_lists(list1, list2):
    """Compare the contents of two lists. If the contents
    of the two lists are not equal, return the index of
    the first difference. If the contents of the two lists
    are equal, return -1.

    Parameters
        list1: a list
        list2: another list
    Return: an index or -1
    """
    # Get the length of the shortest list.
    length1 = len(list1)
    length2 = len(list2)
    limit = min(length1, length2)

    # Begin at the first index (0) and repeat until the
    # computer finds two elements that are not equal or
    # until the computer reaches the end of the shortest
    # list, whichever comes first.
    i = 0
    while i < limit:
        # Retrieve one element from each list.
        element1 = list1[i]
        element2 = list2[i]

        # If the two elements are not
        # equal, quit the while loop.
        if element1 != element2:
            break

        # Add one to the index variable.
        i += 1

    # If the length of both lists are equal and the
    # computer verified that all elements are equal,
    # set i to -1 to indicate that the contents of
    # the two lists are equal.
    if length1 == length2 == i:
        i = -1

    return i


# Call main to start this program.
if __name__ == "__main__":
    main()

print()

# Example 8

def main():
    # These are the indexes of each
    # element in the inner lists.
    YEAR_PLANTED_INDEX = 0
    HEIGHT_INDEX = 1
    GIRTH_INDEX = 2
    FRUIT_AMOUNT_INDEX = 3

    # Create a compound list that stores inner lists.
    apple_tree_data = [
        # [year_planted, height, girth, fruit_amount]
        [2012, 2.7, 3.6, 70.5],
        [2012, 2.4, 3.7, 81.3],
        [2015, 2.3, 3.6, 62.7],
        [2016, 2.1, 2.7, 42.1]
    ]

    # Retrieve one inner list from the compound list.
    one_tree = apple_tree_data[2]

    # Retrieve one value from the inner list.
    height = one_tree[HEIGHT_INDEX]

    # Print the tree's height.
    print(f"height: {height}")


# Call main to start this program.
if __name__ == "__main__":
    main()

print()

# Example 9

def main():
    # These are the indexes of each
    # element in the inner lists.
    YEAR_PLANTED_INDEX = 0
    HEIGHT_INDEX = 1
    GIRTH_INDEX = 2
    FRUIT_AMOUNT_INDEX = 3

    # Create a compound list that stores inner lists.
    apple_tree_data = [
        # [year_planted, height, girth, fruit_amount]
        [2012, 2.7, 3.6, 70.5],
        [2012, 2.4, 3.7, 81.3],
        [2015, 2.3, 3.6, 62.7],
        [2016, 2.1, 2.7, 42.1]
    ]

    total_fruit_amount = 0

    # This loop will repeat once for each inner list
    # in the apple_tree_data compound list.
    for inner_list in apple_tree_data:

        # Retrieve the fruit amount from
        # the current inner list.
        fruit_amount = inner_list[FRUIT_AMOUNT_INDEX]

        # Print the fruit amount for the current tree.
        print(fruit_amount)

        # Add the current fruit amount to the total.
        total_fruit_amount += fruit_amount

    # Print the total fruit amount.
    print(f"Total fruit amount: {total_fruit_amount:.1f}")


# Call main to start this program.
if __name__ == "__main__":
    main()

print()

"""
The program in example 10 contains two integer variables named x and y. The program in example 10 does the following:

The statement at line 4 stores the value 17 into the variable x.
Line 328 copies the value that is in the variable x into the variable y.
Line 329 prints the values of x and y which are both 17.
Line 330 adds one to the value of x, making its value 18 instead of 17.
Line 331 prints the values of x and y again. The value of x was changed to 18. 
The value of y remained unchanged.
Why does line 330 (x += 1) change the value of x but not change the value 
of y? Because line 5 copies the value that was in x into y. In other 
words, x and y are two separate variables, each with its own value.
"""

# Example 10

def main():
    x = 17
    y = x
    print(f"Before changing x: x {x}  y {y}")
    x += 1
    print(f"After changing x:  x {x}  y {y}")

# Call main to start this program.
if __name__ == "__main__":
    main()

print()

"""
Example 11 shows a small Python program that contains two variables 
named lx and ly that each refer to a list. This program is similar 
to the previous program, but it has two lists instead of two integers. 
From the output of example 11, we see there is a big difference between 
the way a Python program assigns integers and the way it assigns lists. 
The program in example 11 does the following:

The statement at line 4 creates a list and stores a reference to that list 
in the variable lx.
Line 5 copies the reference in the variable lx into the variable ly. Line 
5 does not create a copy of the list but instead causes both the variables l
x and ly to refer to the same list.
Line 6 prints the values of lx and ly. Notice that their values are the 
same as we expect them to be because of line 5.
Line 7 appends the number 5 onto the list lx.
Line 8 prints the values of lx and ly again. Notice in the output that 
when lx and ly are printed the second time, it appears that the number 
5 was appended to both lists.
Why does it appear that appending the number 5 onto lx also appends 
the number 5 onto ly? Because lx and ly refer to the same list. There 
is really only one list with two references to that list. Because lx 
and ly refer to the same list, a change to the list through variable 
lx can be seen through variable ly.
"""
# Example 11

def main():
    lx = [7, -2]
    ly = lx
    print(f"Before changing lx: lx {lx}  ly {ly}")
    lx.append(5)
    print(f"After changing lx:  lx {lx}  ly {ly}")

# Call main to start this program.
if __name__ == "__main__":
    main()

print()

"""
The fact that the computer copies the value of some data types 
(boolean, integer, float) and copies the reference for other data 
types (list and other large data types) has important implications 
for passing arguments into functions. Consider the Python program 
in example 12 with two functions named main and modify_args. The 
program in example 12 does the following:

The statement at line 5 assigns the value 5 to a variable named x.
Line 6 assigns a list to a variable named lx.
Line 7 prints the values of x and lx before they are passed to the 
modify_args function.
Line 11 calls the modify_args function and passes x and lx to that 
function.
Within the modify_args function, line 28 changes the value of the 
parameter n by adding one to it, and line 29 changes the value of 
the parameter alist by appending the number 4 onto it.
Line 13 prints the values of x and lx after they were passed to the 
modify_args function. Notice in the output below that the value of 
x was not changed by the modify_args function. However, the value of 
lx was changed by the modify_args function.
"""

# Example 12

def main():
    print("main()")
    x = 5
    lx = [7, -2]
    print(f"Before calling modify_args(): x {x}  lx {lx}")

    # Pass one integer and one list
    # to the modify_args function.
    modify_args(x, lx)

    print(f"After calling modify_args():  x {x}  lx {lx}")


def modify_args(n, alist):
    """Demonstrate that the computer passes a value
    for integers and passes a reference for lists.
    Parameters
        n: A number
        alist: A list
    Return: nothing
    """
    print("   modify_args(n, alist)")
    print(f"   Before changing n and alist: n {n}  alist {alist}")

    # Change the values of both parameters.
    n += 1
    alist.append(4)

    print(f"   After changing n and alist:  n {n}  alist {alist}")


# Call main to start this program.
if __name__ == "__main__":
    main()