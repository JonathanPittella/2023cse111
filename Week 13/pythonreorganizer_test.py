import unittest
import tkinter as tk
from unittest.mock import patch
from pythonreorganizer import analyze_csv, get_products_for_category, main, show_products, clear

class TestYourProgram(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()

    def tearDown(self):
        self.root.destroy()

    @patch('tkinter.filedialog.askopenfilename', return_value='path/to/your/test.csv')
    @patch('tkinter.messagebox.askyesno', return_value=True)
    def test_main(self, mock_askyesno, mock_askopenfilename):
        main()

    def test_analyze_csv(self):
        csv_file_path = 'path/to/your/test.csv'
        result = analyze_csv(csv_file_path)

    def test_get_products_for_category(self):
        csv_file_path = 'path/to/your/test.csv'
        category = 'some_category'
        result = get_products_for_category(csv_file_path, category)

def test_show_products(self):
    frm_main = tk.Frame(self.root)
    result_text = tk.Text(frm_main)
    csv_file_path = 'path/to/your/test.csv'
    categories_count = {'category1': 5, 'category2': 8}
    selected_category_number = 1
    show_products(frm_main, result_text, csv_file_path, categories_count, selected_category_number)

    def test_clear(self):
        frm_main = tk.Frame(self.root)
        ent_age = tk.Entry(frm_main)
        lbl_slow = tk.Label(frm_main, text='Some text')
        lbl_fast = tk.Label(frm_main, text='Some other text')
        result_text = tk.Text(frm_main)
        clear(ent_age, lbl_slow, lbl_fast, result_text)

if __name__ == '__main__':
    unittest.main()
