import csv
import tkinter as tk
from tkinter import Frame, Label, Button, Text, Scrollbar, simpledialog, filedialog, messagebox
from number_entry import IntEntry
from collections import Counter

# Declare csv_file_path as a global variable
csv_file_path = ""
categories_count = {}

def main():
    global csv_file_path, categories_count  # Declare as global variables
    root = tk.Tk()
    root.geometry("800x600")  # Set the width and height of the window
    frm_main = Frame(root)
    frm_main.master.title("Product Categories Counter")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Ask the user if they want to open the CSV file
    open_csv = messagebox.askyesno("Open CSV File", "Do you want to open the CSV file?")
    if open_csv:
        csv_file_path = filedialog.askopenfilename(title="Select CSV File", filetypes=[("CSV files", "*.csv")])
        if csv_file_path:
            categories_count = analyze_csv(csv_file_path)
            populate_main_window(frm_main)
        else:
            root.destroy()
    else:
        root.destroy()

    root.mainloop()


def populate_main_window(frm_main):
    global ent_age, result_text  # Declare ent_age and result_text as global
    lbl_csv_file = Label(frm_main, text=f"CSV File: {csv_file_path}")
    ent_age = IntEntry(frm_main, width=4)
    lbl_age_units = Label(frm_main, text="(Enter Category Number)")
    lbl_rates = Label(frm_main, text=":")
    lbl_slow = Label(frm_main, width=3)
    lbl_fast = Label(frm_main, width=3)
    lbl_rate_units = Label(frm_main, text="")
    btn_clear = Button(frm_main, text="Clear")

    result_text = Text(frm_main, height=10, width=40)
    result_text_scrollbar = Scrollbar(frm_main, command=result_text.yview)
    result_text.config(yscrollcommand=result_text_scrollbar.set)

    lbl_csv_file.grid(row=0, column=0, columnspan=4, padx=3, pady=3)
    ent_age.grid(row=1, column=0, padx=3, pady=3)
    lbl_age_units.grid(row=1, column=1, padx=0, pady=3)
    lbl_rates.grid(row=2, column=0, padx=(30, 3), pady=3)
    lbl_slow.grid(row=2, column=1, padx=3, pady=3)
    lbl_fast.grid(row=2, column=2, padx=3, pady=3)
    lbl_rate_units.grid(row=2, column=3, padx=0, pady=3)
    btn_clear.grid(row=3, column=0, padx=3, pady=3, columnspan=2, sticky="w")
    result_text.grid(row=4, column=0, columnspan=4, padx=3, pady=3, sticky="nsew")
    result_text_scrollbar.grid(row=4, column=4, pady=3, sticky="ns")

    ent_age.bind("<KeyRelease>", show_products)
    btn_clear.config(command=clear)

    result_text.delete("1.0", tk.END)
    for i, (category, count) in enumerate(categories_count.items(), start=1):
        result_text.insert(tk.END, f"{i}. {category}: {count} products\n")

def show_products(event=None):
    try:
        selected_category_number = ent_age.get()
        if 1 <= selected_category_number <= len(categories_count):
            selected_category = list(categories_count.keys())[selected_category_number - 1]
            products = get_products_for_category(csv_file_path, selected_category)
            result_text.delete("1.0", tk.END)  # Clear previous content
            result_text.insert(tk.END, f"Products in Category '{selected_category}':\n")
            for product in products:
                result_text.insert(tk.END, f"{product}\n")
        else:
            result_text.delete("1.0", tk.END)  # Clear previous content
            result_text.insert(tk.END, f"Invalid category number: {selected_category_number}\n")
    except ValueError:
        pass

def clear():
    global ent_age, result_text  # Add this line to declare ent_age as global
    ent_age.clear()
    result_text.delete("1.0", tk.END) 
    ent_age.focus()

    # Repopulate the original list of categories
    result_text.delete("1.0", tk.END) 
    for i, (category, count) in enumerate(categories_count.items(), start=1):
        result_text.insert(tk.END, f"{i}. {category}: {count} products\n")

def analyze_csv(csv_file_path):
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        first_word_column_index = 0
        categories_count = Counter(row[first_word_column_index].split()[0] for row in csv_reader)
    return categories_count

def get_products_for_category(csv_file_path, category):
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  
        first_word_column_index = 0
        products = [row[first_word_column_index] for row in csv_reader if row[first_word_column_index].split()[0] == category]

    return products

if __name__ == "__main__":
    main()
