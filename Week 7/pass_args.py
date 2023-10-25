"""
Demonstrate that numbers are passed to a function by value
and lists are passed to a function by reference.
"""

def main():
    print("main()")
    x = 5
    lx = [7, -2]
    print(f"    Before calling modify_args(): x {x}  lx {lx}")

    # Pass one integer and one list
    # to the modify_args function.
    modify_args(x, lx)

    print(f"    After calling modify_args():  x {x}  lx {lx}")


def modify_args(n, alist):
    """Demonstrate that the computer passes a value
    for integers and passes a reference for lists.
    Parameters
        n: A number
        alist: A list
    Return: nothing
    """
    print("    modify_args(n, alist)")
    print(f"        Before changing n and alist: n {n}  alist {alist}")

    # Change the values of both parameters.
    n += 1
    alist.append(4)

    print(f"        After changing n and alist:  n {n}  alist {alist}")


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()

#How dos it works?
"""
Run the pass_args.py program on your computer. Examine the code and 
the output and answer the following three questions:
In main, there are two local variables named x and lx. At line 14, 
both of these local variables are passed to the modify_args function. 
After the call to modify_args finished, which of main’s two local 
variables did the modify_args function change?
x
lx
both of them
neither of them
Why is the modify_args function NOT able to change main’s local 
variable x?
Because x is a number and therefore passed to a function by value
Because x is a list and therefore passed to a function by reference
Why is the modify_args function able to change main’s local variable lx?
Because lx is a number and therefore passed to a function by value
Because lx is a list and therefore passed to a function by reference
Sample Run
"""
