# Example 1

def main():
    # Create a dictionary with student IDs as
    # the keys and student names as the values.
    students_dict = {
        "42-039-4736": "Clint Huish",
        "61-315-0160": "Amelia Davis",
        "10-450-1203": "Ana Soares",
        "75-421-2310": "Abdul Ali",
        "07-103-5621": "Amelia Davis"
    }

    # Add an item to the dictionary.
    #dictionary_name[key] = value
    students_dict["81-298-9238"] = "Sama Patel"

    # Remove an item from the dictionary.
    students_dict.pop("61-315-0160")

    # Get the number of items in the dictionary.
    length = len(students_dict)
    print(f"length: {length}")

    # Print the entire dictionary.
    print(students_dict)
    print()

    # Get a student ID from the user.
    id = input("Enter a student ID: ")

    # Check if the student ID is in the dictionary.
    if id in students_dict:

        # Find the student ID in the dictionary and
        # retrieve the corresponding student name.
        name = students_dict[id]

        # Print the student's name.
        print(name)

    else:
        print("No such student")


# Call main to start this program.
if __name__ == "__main__":
    main()


# Example 2

def main():
    # Create a dictionary with student IDs as the keys
    # and student data stored in a list as the values.
    students_dict = {
        # student_ID: [given_name, surname, email_address, credits]
        "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
        "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
        "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
        "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
        "07-103-5621": ["Amelia", "Davis" "dav19008@byui.edu", 0]
    }


#Bad Exemplo!!!!!!!!!!!!:
# Example 3

def main():
    # Create a dictionary with student IDs as the keys
    # and student data stored in a list as the values.
    students_dict = {
        # student_ID: [given_name, surname, email_address, credits]
        "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
        "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
        "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
        "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
        "07-103-5621": ["Amelia", "Davis" "dav19008@byui.edu", 0]
    }

    # Get a student ID from the user.
    id = input("Enter a student ID: ")

    # This is a difficult and slow way to find an item in a
    # dictionary. Don't write code like this to find an item
    # in a dictionary!

    # For each item in the dictionary, check if
    # its key is the same as the variable id.
    student = None
    for key, value in students_dict.items(): # Bad example!
        if key == id:                        # Don't use a loop
            student = value                  # like this to find an
            break                            # item in a dictionary.    


#Good exemplo
# Example 4

def main():
    # Create a dictionary with student IDs as the keys
    # and student data stored in a list as the values.
    students_dict = {
        # student_ID: [given_name, surname, email_address, credits]
        "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
        "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
        "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
        "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
        "07-103-5621": ["Amelia", "Davis" "dav19008@byui.edu", 0]
    }

    # These are the indexes of the elements in the value lists.
    GIVEN_NAME_INDEX = 0
    SURNAME_INDEX = 1
    EMAIL_INDEX = 2
    CREDITS_INDEX = 3

    # Get a student ID from the user.
    id = input("Enter a student ID: ")

    # Check if the student ID is in the dictionary.
    if id in students_dict:

        # Find the student ID in the dictionary and
        # retrieve the corresponding value, which is a list.
        value = students_dict[id]

        # Retrieve the student's given name (first name) and
        # surname (last name or family name) from the list.
        given_name = value[GIVEN_NAME_INDEX]
        surname = value[SURNAME_INDEX]

        # Print the student's name.
        print(f"{given_name} {surname}")

    else:
        print("No such student")


# Call main to start this program.
if __name__ == "__main__":
    main()


# Example 6

def main():
    # Create a dictionary with student IDs as the keys
    # and student data stored in a list as the values.
    students_dict = {
        "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
        "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
        "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
        "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
        "07-103-5621": ["Amelia", "Davis", "dav19008@byui.edu", 0],
        "81-298-9238": ["Sama", "Patel", "pat21004@byui.edu", 8]
    }

    # These are the indexes of the elements in the value lists.
    GIVEN_NAME_INDEX = 0
    SURNAME_INDEX = 1
    EMAIL_INDEX = 2
    CREDITS_INDEX = 3

    total = 0

    # For each item in the list add the number
    # of credits that the student has earned.
    for key, value in students_dict.items():

        # Retrieve the number of credits from the value list.
        credits = value[CREDITS_INDEX]

        # Add the number of credits to the total.
        total += credits

    print(f"Total credits earned by all students: {total}")


# Call main to start this program.
if __name__ == "__main__":
    main()


#Difference between lists and dictionary 
    # Create a list of cities.


    cities_list = ["Delhi", "Lagos", "Dallas"]

    # Create a dictionary of people.
    people_dict = {
        "P203": "Ignacio Torres",
        "P445": "Whitney Nelson",
        "P128": "Yasmin Li"
    }

    # Add two cities to the cities list.
    cities_list.insert(1, "Paris")
    cities_list.append("Tokyo")

    # Add two people to the people dictionary.
    people_dict["P205"] = "Liam Myers"
    people_dict["P317"] = "Davina Patel"

    if "Paris" in cities_list:
        print("Paris is in the list of cities.")

    if "P203" in people_dict:
        print("P203 is in the dictionary of people.")

    # Find Dallas in the cities list.
    index = cities_list.index("Dallas")

    # Find person P128 in the people dictionary.
    person_name = people_dict["P128"]

    # Retrieve the element stored at
    # index 2 in the cities list.
    city_name = cities_list[2]

    # Find person P128 in the people dictionary
    # and retrieve the corresponding value.
    person_name = people_dict["P128"]

    # Change the city name at index 2 to London.
    cities_list[2] = "London"

    # Change the name of person P205 to Finn Meyers.
    people_dict["P205"] = "Finn Myers"

    # Process all the elements in the cities list.
    for city_name in cities_list:
        print(city_name)

    # Process all the items in the people dictionary.
    for person_key, person_name in people_dict.items():
        print(person_name)

    # Remove the element at index 3
    # from the cities list.
    cities_list.pop(3)

    # Remove the key "P203" and its
    # value from the people dictionary.
    people_dict.pop("P203")

    # Call the draw_chart function and pass
    # the citites list to that function.
    draw_chart(cities_list)

    # Call the hire_people function and pass
    # the people dictionary to that function.
    hire_people(people_dict)

# Example 7

def main():
    # Create a list that contains five student numbers.
    numbers_list = ["42-039-4736", "61-315-0160",
            "10-450-1203", "75-421-2310", "07-103-5621"]

    # Create a list that contains five student names.
    names_list = ["Clint Huish", "Amelia Davis",
            "Ana Soares", "Abdul Ali", "Amelia Davis"]

    # Convert the numbers and names lists into a dictionary.
    student_dict = dict(zip(numbers_list, names_list))

    # Print the entire student dictionary.
    print("Dictionary:", student_dict)
    print()

    # Convert the student dictionary into
    # two lists named keys and values.
    keys = list(student_dict.keys())
    values = list(student_dict.values())

    # Print both lists.
    print("Keys:", keys)
    print()
    print("Values:", values)


# Call main to start this program.
if __name__ == "__main__":
    main()

"""
Lists	                                Dictionaries
Similar	A list can                      A dictionary can store 
store many elements.                    many items.
                        Different:
List:
Each element in a list does
not have to be unique.	

Lists were designed for efficiently storing elements. Lists use 
less memory than dictionaries. However, finding an element in a 
list is relatively slow.

A programmer uses square brackets ([ and ]) to create a list.

Dictionary:
Each item in a dictionary is a key value pair. Each key must be 
unique within a dictionary. Each value does not have to be unique.

Dictionaries were designed for quickly finding items. Finding an 
item in a dictionary is fast. However, dictionaries use more memory 
than lists.

A programmer uses curly braces ({ and }) to create a dictionary.

Same:	
Lists are mutable, which means a program can add and remove 
elements after a list is created.

Dictionaries are mutable, which means a program can add and 
remove items after a dictionary is created.

A programmer calls the insert and append methods to add an 
element to a list.

A programmer uses square brackets ([ and ]) to add an item to 
a dictionary.

Similar:
To cause the computer to check whether an element is in a list, 
a programmer uses the in keyword.

To cause the computer to check whether a key is in a dictionary, 
a programmer uses the in keyword.

Different:	
A programmer uses the index method to find an element in a list.

A programmer uses square brackets ([ and ]) and a key to find an 
item in a list.

Similar:	
A programmer uses square brackets ([ and ]) and an index to 
retrieve an element from a list.

A programmer uses square brackets ([ and ]) and a key to retrieve 
a value from a dictionary.

A programmer uses square brackets ([ and ]) and an index to replace 
an element in a list.

A programmer uses square brackets ([ and ]) and a key to replace a 
value in a dictionary.

Similar:	
A programmer can use a for loop to process all the elements in a 
list.

A programmer can use a for loop to process all the items in a 
dictionary.

Same:	
A programmer uses the pop method to remove an element from a list.

A programmer uses the pop method to remove an item from a dictionary.

Lists are passed by reference into a function.

Dictionaries are passed by reference into a function.

"""


"""
Converting between Lists and Dictionaries
It is possible to convert two lists into a dictionary by 
using the built-in zip and dict functions. The contents 
of the first list will become the keys in the dictionary, 
and the contents of the second list will become the values. 
This implies that the two lists must have the same length, 
and the elements in the first list must be unique because 
keys in a dictionary must be unique.

It is also possible to convert a dictionary into two lists by 
using the keys and values methods and the built-in list function. 
The following code example starts with two lists, converts them 
into a dictionary, and then converts the dictionary into two lists.
"""