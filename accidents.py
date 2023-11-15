# Import the csv module so that it can be used
# to read from the accidents.csv file.
import csv

# Column numbers from the accidents.csv file.
YEAR_COLUMN = 0
FATALITIES_COLUMN = 1
INJURIES_COLUMN = 2
CRASHES_COLUMN = 3
FATAL_CRASHES_COLUMN = 4
DISTRACT_COLUMN = 5
PHONE_COLUMN = 6
SPEED_COLUMN = 7
DUI_COLUMN = 8
FATIGUE_COLUMN = 9

def main():
    try:
        # Prompt the user for a filename and open that text file.
        filename = input("Name of file that contains NHTSA data: ")
        with open(filename, "rt") as text_file:

            # Prompt the user for a percentage.
            perc_reduc = float(input("Percent reduction of texting while driving [0, 100]: "))

            if perc_reduc < 0:
                raise ValueError(f"{perc_reduc} is too low. Please enter a different number.")

            print()
            print(f"With a {perc_reduc}% reduction in using a cell",
                  "phone while driving, approximately the",
                  "following number of injuries and deaths",
                  "would have been prevented in the USA.", sep="\n")
            print()
            print("Year, Injuries, Deaths")

            # Use the csv module to create a reader
            # object that will read from the opened file.
            reader = csv.reader(text_file)

            # The first line of the CSV file contains column headings
            # and not a student's I-Number and name, so this statement
            # skips the first line of the CSV file.
            next(reader)

            # Process each row in the CSV file.
            for row in reader:
                year = row[YEAR_COLUMN]

                # Call the estimate_reduction function.
                injur, fatal = estimate_reduction(row, PHONE_COLUMN, perc_reduc)

                # Print the estimated reductions
                # in injuries and fatalities.
                print(year, injur, fatal, sep=", ")

    except FileNotFoundError as not_found_err:
        # This code will be executed if the user enters
        # the name of a file that doesn't exist.
        print()
        print(type(not_found_err).__name__, not_found_err, sep=": ")
        print(f"The file {filename} doesn't exist.")
        print("Run the program again and enter the" \
              " name of an existing file.")

    except ValueError as val_err:
        # This code will be executed if the user enters
        # an invalid integer for the line number.
        print()
        print(type(val_err).__name__, val_err, sep=": ")
        print("You entered an invalid integer for the line number.")
        print("Run the program again and enter an integer for" \
              " the line number.")

    except ValueError as val_error:
        print()
        print(type(val_error).__name__, val_error, sep=": ")
        if "percent reduction" in str(val_error).lower() and "negative" in str(val_error).lower():
            print(f"Error: Percent reduction cannot be negative. Please enter a non-negative number.")
        else:
            print("There was an error with the entered value.")
            print("Review the code and input values.")

    except IndexError as index_err:
        # This code will be executed if the user enters a valid
        # integer for the line number, but the integer is greater
        # than the number of lines in the file.
        print()
        print(type(index_err).__name__, index_err, sep=": ")
        if not filename:
            print("The filename is empty.")
        else:
            print(f"There was an index error with the file {filename}.")
            print("Review the code and file structure.")

    except Exception as excep:
        # This code will be executed if some
        # other type of exception occurs.
        print()
        print(type(excep).__name__, excep, sep=": ")

def estimate_reduction(row, behavior_key, perc_reduc):
    """Estimate and return the number of injuries and deaths that
    would not have occurred on U.S. roads and highways if drivers
    had reduced a dangerous behavior by a given percentage.

    Parameters
        row: a CSV row of data from the U.S. National Highway Traffic
            Safety Administration (NHTSA)
        behavior_key: heading from the CSV file for the dangerous
            behavior that drivers could reduce
        perc_reduc: percent that drivers could reduce a dangerous
            behavior
    Return: The number of injuries and deaths that may have been
        prevented
    """
    behavior = int(row[behavior_key])
    fatal_crashes = int(row[FATAL_CRASHES_COLUMN])
    ratio = perc_reduc / 100 * behavior / fatal_crashes

    fatalities = int(row[FATALITIES_COLUMN])
    injuries = int(row[INJURIES_COLUMN])

    reduc_fatal = int(round(fatalities * ratio, 0))
    reduc_injur = int(round(injuries * ratio, 0))
    return reduc_injur, reduc_fatal

# If this file was executed like this:
# > python accidents.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()