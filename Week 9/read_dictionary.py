import csv

def read_dictionary(filename):
    student_data = {}
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader) 
        for row in reader:
            inumber, name = row
            student_data[inumber] = name
    return student_data

def main():
    filename = 'Week 9/students.csv'
    student_data = read_dictionary(filename)
    
    inumber = input("Enter I-Number: ")
    
    if inumber in student_data:
        student_name = student_data[inumber]
        print(f"Student name: {student_name}")
    else:
        print("No such student")

if __name__ == "__main__":
    main()
