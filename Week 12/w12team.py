import math
import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry

def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Area of a circle")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()

def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create a label that displays "Radius:"
    lbl_radius = Label(frm_main, text="Radius:")

    # Create an integer entry box where the user will enter the radius.
    ent_radius = IntEntry(frm_main, width=4, lower_bound=1, upper_bound=100)

    # Create a label that displays "units"
    lbl_radius_units = Label(frm_main, text="units")

    # Create a label that will display the result.
    lbl_area = Label(frm_main, width=10)

    # Create the Clear button.
    btn_clear = Button(frm_main, text="Clear")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_radius.grid(      row=0, column=0, padx=3, pady=3)
    ent_radius.grid(      row=0, column=1, padx=3, pady=3)
    lbl_radius_units.grid(row=0, column=2, padx=0, pady=3)

    lbl_area.grid(      row=1, column=0, columnspan=3, padx=3, pady=3)

    btn_clear.grid(row=2, column=0, padx=3, pady=3, columnspan=3, sticky="w")

    # This function will be called each time the user releases a key.
    def calculate(event):
        """Compute and display the area of a circle."""
        try:
            radius = ent_radius.get()
            if radius:
                area = math.pi * (float(radius) ** 2)
                lbl_area.config(text=f"Area: {area:.2f}")
            else:
                lbl_area.config(text="")
        except ValueError:
            # When the user enters non-numeric values, clear the result label.
            lbl_area.config(text="")

    # This function will be called each time the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_radius.clear()
        lbl_area.config(text="")
        ent_radius.focus()

    # Bind the calculate function to the radius entry box so
    # that the computer will call the calculate function
    # when the user changes the text in the entry box.
    ent_radius.bind("<KeyRelease>", calculate)

    # Bind the clear function to the clear button so
    # that the computer will call the clear function
    # when the user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the radius entry box.
    ent_radius.focus()

# If this file is executed like this:
# > python circle_area.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
