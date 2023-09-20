from time import sleep
name = input("What is your name?")
for i in range(3, 0, -1):
    print(i, flush=True)
    sleep(0.9)
print(f"Welcome to CSE 111 {name}!")

from time import sleep
name = input("Hello! what is your name?")
for i in range(3, 0, -1):
    #i is just the value used to assign the function
    print(i, flush=True)
    #flush=True is used to print number by number.
    sleep(0.9)    
print(f"Welcome to CSE 111,{name}")