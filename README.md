# Linear Search GUI Application
**Author:** Andrew Cunningham  
**Course:** CSC506 - Critical Thinking Assignment 1

---

## Project Overview
This application is a simple Python GUI tool that allows users to search through a local SQLite database of online sales using a **linear search algorithm**. The GUI is built with **Tkinter**, and results are displayed in a simple text-area.

---

## How It Works
- The user selects a category (e.g., product name, region) from a dropdown.
- A search term is entered in the text field.
- When the "Search" button is clicked, the application performs a **linear search**:
  - It retrieves **all rows** from the database.
  - It loops through each row **manually** in Python, comparing the target field to the search query.
  - Matching rows are displayed in the results box.

> The use of linear search satisfies the assignment requirement to implement a basic search algorithm without relying on SQL filtering.

---

## Technologies Used
- **Python 3**
- **Tkinter** for GUI
- **SQLite3** for local database access

---

## What I Learned

- **GUI Development:** How to create a clean, interactive interface using Tkinter widgets like `Entry`, `Button`, `Text`, and `OptionMenu`.
- **Database Integration:** How to connect to and query an SQLite database using Python’s built-in `sqlite3` module.
- **Linear Search Logic:** Implementing a manual linear search over a dataset, accessing fields by index, and ensuring case-insensitive comparisons.
- **Safe SQL Practices:** Avoiding SQL injection by using parameterized queries.
- **String Handling:** Cleaning input with `.strip()`, formatting output with `enumerate()` and `join()`, and aligning data for readability.

---

## Challenges Faced

- Handling text formatting in the results box so that rows were readable and neatly aligned.
- Managing communication between the GUI and backend logic while keeping the code modular.
- Realizing the difference between using SQL filtering and manual search logic — and adapting my approach to meet the assignment's expectations.

---

## How to Run
1. Install Python 3.
2. Make sure the SQLite database is located at `data/marketplace.db`.
3. Run the app:
   ```bash
   python main.py

---

## AI Disclosure

- All code written, including design, is my own.
- Chat GPT was utilized as a coach, and mentor. It helped me understand concepts and suggestions for writing and improving my code, as well as best practices.
- This README was AI-written, and was not submitted as part of the assignment.