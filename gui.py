# Andrew Cunningham
# CSC506 Critical Thinking Assignment 1

# Practice making a simple tkinter gui to support linear search

import tkinter as tk

class gui:
    def __init__(self, root, on_submit_callback, categories):
        self.root = root
        self.root.title("Online Sales Search Tool")
        self.root.iconbitmap("icons/favicon.ico")
        self.on_submit_callback = on_submit_callback

        # Dropdown
        self.categories = categories

        self.initialize_fields()

    def initialize_fields(self):
        '''Initializes a GUI with a dropdown menu for the database's fields,
            A query field, and contains room for the results'''
        # font and entry width
        global_font = ("Arial", 12)

        # label
        top_label = tk.Label(self.root, text = "Simple linear search: select category, input search query", font = global_font)
        top_label.pack(pady=15, padx=15)

        # dropdown
        self.selected_category = tk.StringVar()
        self.selected_category.set(self.categories[0])

        dropdown_menu = tk.OptionMenu(self.root, self.selected_category, *self.categories)
        dropdown_menu.config(font=global_font)
        dropdown_menu.pack(padx=15, pady=15)

        # query
        self.query_entry = tk.Entry(self.root, font=global_font)
        self.query_entry.pack(padx=15,pady=15)

        # submit button
        self.submit_button = tk.Button(self.root, text="Search", command=self.handle_submit)
        self.submit_button.pack(padx=15,pady=15)

        # results
        self.results_box = tk.Text(self.root, height=50, width=130, font=("Courier", 10), wrap="none")
        self.results_box.pack(padx=15,pady=15)



    def handle_submit(self):
        '''utlizes the call-back function to return the inputs to the calling class'''
        category = self.selected_category.get()
        query = self.query_entry.get().strip()
        self.on_submit_callback(category, query)

    def update_results(self, results):
        '''displays results in the output field'''
        self.results_box.delete("1.0", tk.END)
        
        if not results:
            self.results_box.insert(tk.END, "No results found =[\n")
            return
        
        for index, row in enumerate(results, start=1):
            line = f"{index}\t" + "\t".join(str(item) for item in row) + "\n"
            self.results_box.insert(tk.END, line)