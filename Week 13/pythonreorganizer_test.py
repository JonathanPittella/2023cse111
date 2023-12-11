import csv
import unittest
import tkinter as tk
from unittest.mock import patch
from collections import Counter  # Import Counter
from pythonreorganizer import analyze_csv, get_products_for_category, main, show_products, clear

class TestYourProgram(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()

    def tearDown(self):
        self.root.destroy()

    @patch('tkinter.filedialog.askopenfilename', return_value='')
    @patch('tkinter.messagebox.askyesno', return_value=True)
    @patch('tkinter.messagebox.showinfo')  
    @patch('tkinter.messagebox.showwarning')  
    def test_main(self, mock_showwarning, mock_showinfo, mock_askyesno, mock_askopenfilename):
        with patch.object(self.root, 'tk', return_value=self.root.tk):
            self.root.tk.call = self.root.tk.getOpenFile = lambda: 'Week 13/pythonreorganizer.py'
            main()
    
    def test_show_products(self):
        frm_main = tk.Frame(self.root)
        result_text = tk.Text(frm_main)
        csv_file_path = 'Week 13/pythonreorganizer.py'
        categories_count = {'category1': 5, 'category2': 8}
        selected_category_number = 1
        first_word_column_index = 1
        self.show_products(frm_main, result_text, csv_file_path, categories_count, selected_category_number, first_word_column_index)
        # Add meaningful assertions for testing

    def test_analyze_csv(self):
        csv_file_path = 'Week 13/pythonreorganizer.py'
        result = analyze_csv(csv_file_path)
        self.assertIsNotNone(result)  # Add a meaningful assertion

    def test_show_products(self):
        frm_main = tk.Frame(self.root)
        result_text = tk.Text(frm_main)
        csv_file_path = 'Week 13/pythonreorganizer.py'
        categories_count = {'category1': 5, 'category2': 8}
        selected_category_number = 1
        first_word_column_index = 0  # Replace with the correct index
        self.show_products(frm_main, result_text, csv_file_path, categories_count, selected_category_number, first_word_column_index)

    def clear(self, ent_age, result_text):
        ent_age.delete(0, tk.END)
        result_text.delete("1.0", tk.END)
        ent_age.focus()

    def show_products(self, frm_main, result_text, csv_file_path, categories_count, selected_category_number, first_word_column_index):
        try:
            selected_category_number = int(selected_category_number)
            if 1 <= selected_category_number <= len(categories_count):
                selected_category = list(categories_count.keys())[selected_category_number - 1]
                products = get_products_for_category(csv_file_path, selected_category, first_word_column_index)  # Pass first_word_column_index to get_products_for_category
                result_text.delete("1.0", tk.END)  # Clear previous content
                result_text.insert(tk.END, f"Products in Category '{selected_category}':\n")
                for product in products:
                    result_text.insert(tk.END, f"{product}\n")
            else:
                result_text.delete("1.0", tk.END)  # Clear previous content
                result_text.insert(tk.END, f"Invalid category number: {selected_category_number}\n")
        except ValueError:
            pass

    def test_analyze_csv(self):
        csv_file_path = 'Week 13/pythonreorganizer.py'
        result = analyze_csv(csv_file_path)
        self.assertIsNotNone(result)  # Add a meaningful assertion

    def test_get_products_for_category(self):
        csv_file_path = 'Week 13/pythonreorganizer.py'
        category = 'category1'
        first_word_column_index = 1  # Replace with the correct index
        result = get_products_for_category(csv_file_path, category, first_word_column_index)
        # Add meaningful assertions for testing

    def test_clear(self):
        ent_age = tk.Entry(self.root)
        result_text = tk.Text(self.root)
        self.clear(ent_age, result_text)
        # Add meaningful assertions for testing

    def test_show_products(self):
        frm_main = tk.Frame(self.root)
        result_text = tk.Text(frm_main)
        csv_file_path = 'Week 13/pythonreorganizer.py'
        categories_count = {'category1': 5, 'category2': 8}
        selected_category_number = 1
        first_word_column_index = 1  # Replace with the correct index
        self.show_products(frm_main, result_text, csv_file_path, categories_count, selected_category_number, first_word_column_index)

        # Add meaningful assertions to check the state of result_text after calling show_products
        expected_text = "Products in Category 'category1':\nproduct1\nproduct2\n"
        self.assertEqual(result_text.get("1.0", tk.END), expected_text)

    def analyze_csv(csv_file_path):
        with open(csv_file_path, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            first_word_column_index = 0
            categories_count = Counter(row[first_word_column_index].split()[0] for row in csv_reader if row and len(row) > first_word_column_index)

        return categories_count

if __name__ == '__main__':
    unittest.main()