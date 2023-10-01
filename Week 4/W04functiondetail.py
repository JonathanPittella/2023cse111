# g is a global variable because it
# is defined outside of all functions.
g = 25

def main():
    # x is a local variable because
    # it is defined inside a function.
    x = 1

"""
Python Variable Scope
        Local
Where to Define: Inside a function 

Owner: The function where the variable is defined

Lifetime: Only as long as its containing function is executing

Where Usable: Only inside the function where it is defined

        Global
Where to Define: Outside all functions

Owner: The Python file where the variable is defined

Lifetime: As long as its containing program is executing

Where Usable: In all functions of the Python program
"""

#The variable nShapes is global because it is defined 
# outside of all functions. Because it is a global variable, 
# the code in the body of all functions may use the variable 
# nShapes. Within the square_area function, the parameter 
# named length and the variable named area both have local scope.


nShapes = 0

def square_area(length):
    area = length * length
    return area

def rectangle_area(width, length):
    area = width * length
    return area

import math

#add a parameter to the circle_area function 
# as shown at line 60 and pass the radius from 
# the main function to the circle_area function 
# as shown at line 57

def main():
    radius = float(input("Enter the radius of a circle: "))
    area = circle_area(radius)
    print(f"area: {area:.1f}")

def circle_area(radius):
    area = math.pi * radius * radius
    return area

main()


"""
Consider the program in example 5. Notice at line 19 
in the header for the arc_length function, that the 
parameter radius does not have a default value but 
the parameter degrees has a default value of 360. This 
means that when a programmer writes code to call the 
arc_length function, the programmer must pass a value 
for radius but is not required to pass a value for degrees. 
At line 8, the programmer wrote code to call the arc_length 
function and passed 4.7 for the radius parameter but did 
not pass a value for the degrees, so during that call to 
arc_length, the value of degrees will be the default value 
from line 19, which is 360. At line 13, the programmer wrote 
code to call the arc_length function again and passed two 
arguments: 4.7 and 270, so during that call to arc_length, 
the value of degrees will be 270.
"""
# Example 5

import math

def main():
    # Call the arc_length function with only one argument
    # even though the arc_length function has two parameters.
    len1 = arc_length(4.7)
    print(f"len1: {len1:.1f}")

    # Call the arc_length function again but
    # this time with two arguments.
    len2 = arc_length(4.7, 270)
    print(f"len2: {len2:.1f}")


# Define a function with two parameters. The
# second parameter has a default value of 360.
def arc_length(radius, degrees=360):
    """Compute and return the length of an arc of a circle."""
    circumference = 2 * math.pi * radius
    length = circumference * degrees / 360
    return length


main()


"""
Function Design
What are the properties of a good function?

There are many things to consider when writing 
a function, and many authors have written about 
design concepts that make functions easier to 
understand and less error prone. In future courses 
at BYU-Idaho, you will study some of these design 
concepts. For CSE 111, the following list contains 
a few properties that you should incorporate into 
your functions.

A good function is understandable by other programmers. 
One way to make a function understandable is to write a 
documentation string at the top of the function that 
describes the function, its parameters, and its return 
value. Another way to make a function understandable is 
to write comments in the body of the function as needed.

A good function performs a single task that the programmer 
can describe, and the function’s name matches its task.

A good function is relatively short, perhaps fewer than 
20 lines of code.
A good function has as few decision points (if 
statements and loops) as possible. Too many decision points 
in a function make a function error prone and difficult 
to test.

A good function is as reusable as possible. Functions that 
use parameters and return a result are more reusable than 
functions that get input from a user and print results to 
a terminal window.

As you read the sample code in CSE 111, observe how the 
sample functions fit these good properties, and as you 
write programs for CSE 111, do your best to write functions 
that have these good properties.

Summary
During this lesson, you are studying variable scope, default 
parameter values, and optional arguments. A variable that is 
defined (assigned a value) inside a function has local scope, 
and it can be used inside only the function where it is 
defined. Parameters always have local scope.

A parameter may have a default value like the parameter 
degrees in this function header:

def arc_length(radius, degrees=360):
    ⋮
When a function’s parameter has a default value, you can 
write a call to that function without passing an argument 
for the parameter like this:

length = arc_length(3.5)
In other words, the argument for a parameter that has a 
default value is optional.
"""