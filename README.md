## Please Read Before Using the App

This application was created as my **first capstone project** for the **Business and Data Analyst course at Purwadhika**.

The main purpose of this project is to practice **CRUD (Create, Read, Update, Delete)** functionality using Python.

This application may contain limitations or simplifications and may not fully reflect real-world workflows. However, it represents my best effort at this stage of learning.

## Technical Notes

- This application is built using **Python 3** as its sole programming language.
- All data in this app is **hardcoded** within the Python file.
- The data will **reset every time the application is restarted**.
- The application is **not connected to any database**.
- All data used in this project is **entirely fictional** and for learning purposes only.

## Project Overview
![Main Menu](Screenshots/Main%20Menu.png)

This program simulates a small library system that runs in the command line. Users can:

- View the list of books
- Add new book entries
- Update book details
- Soft delete books (move to trash)
- Restore or permanently delete from trash
- Borrow books with borrowing history

The app manages book status and stock automatically.

---

## Features

### 1) View Library Collection
![Menu 1](Screenshots/Menu%201.png)

This feature allows users to explore the library’s book collection through several viewing options. Users can display the complete list of books stored in the system, filter books based on specific categories, and view only available books with stock greater than zero. In addition, the application provides a search functionality that enables users to find books by entering keywords related to the book title or the author’s name, making it easier to locate specific items in the collection.

![Menu 1-1](Screenshots/Menu%201-1.png)


### 2) Add New Book
![Menu 2](Screenshots/Menu%202.png)

This feature allows users to add a new book into the library collection by entering the required book details. When a book is added, the application automatically generates a unique Book ID following the `BK-XXX-YYYY-AB12` format. The system also determines the book’s availability status based on its stock: books with stock greater than zero are marked as `TERSEDIA`, while books with zero stock are marked as `DIPINJAM`.

### 3) Update Book Data
![Menu 3](Screenshots/Menu%203.png)

This feature enables users to update existing book information by searching for a book using its title. Users can choose to update all book fields except the Book ID or update specific fields such as the title, author, publication year, category, or stock. After any update, the application automatically recalculates and updates the book’s status based on the current stock value.

### 4) Delete + Trash System
![Menu 4](Screenshots/Menu%204.png)

Instead of permanently deleting a book immediately, this application implements a soft delete mechanism through a Trash system. When a book is deleted, it is moved to the Trash list. From the Trash menu, users can view deleted books, restore a book back to the main library collection, or permanently remove a book from the system.

### 5) Borrow / Rent Books
![Menu 5](Screenshots/Menu%205.png)
![Menu 5-4](Screenshots/Menu%205-4.png)

This feature simulates a book borrowing process. Users can add books to a borrowing cart with a maximum limit of two books per transaction and remove books from the cart if needed. During checkout, the application records borrowing details, including the borrower’s name, the borrow date (set to the current date), and the due date (seven days after the borrow date). Once a transaction is completed, the system automatically updates the book stock and availability status and saves the borrowing history for record-keeping purposes.
