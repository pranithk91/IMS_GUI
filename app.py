import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
from datetime import datetime

# MySQL connection function
def connect_to_db():
    try:
        # Replace the credentials with your MySQL username and password
        connection = mysql.connector.connect(
        host="193.203.184.152",
        port='3306',
        user="u885517842_AdminUser",
        password="MdP@ssword!!1",
        database="u885517842_MedicalStore"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        messagebox.showerror("Database Error", f"Error while connecting to MySQL: {str(e)}")
        return None





# Insert data function

def insert_data(date, name, quantity, price, expiry_date, batch_number, invoice_number):
    connection = connect_to_db()
    if connection:
        try:
            cursor = connection.cursor()
            # Prepare the insert query
            query = """INSERT INTO your_table_name (date, MId, quantity, price, expiry_date, batch_number, invoice_number) 
                       VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            # Execute the query with user inputs
            cursor.execute(query, (date, name, quantity, price, expiry_date, batch_number, invoice_number))
            connection.commit()
            messagebox.showinfo("Success", "Data inserted successfully")
        except Error as e:
            messagebox.showerror("Error", f"Failed to insert data: {str(e)}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

# Submit button callback
def submit_data():
    # Fetch data from entry fields
    date = entry_date.get()
    name = entry_name.get()
    quantity = entry_quantity.get()
    price = entry_price.get()
    expiry_date = entry_expiry.get()
    batch_number = entry_batch.get()
    invoice_number = entry_invoice.get()
    
    # Validate input fields
    if not all([date, name, quantity, price, expiry_date, batch_number, invoice_number]):
        messagebox.showwarning("Input Error", "All fields must be filled out")
        return

    try:
        # Check date format for 'date' and 'expiry_date'
        datetime.strptime(date, '%Y-%m-%d')
        datetime.strptime(expiry_date, '%Y-%m-%d')
    except ValueError:
        messagebox.showerror("Date Error", "Invalid date format. Use YYYY-MM-DD")
        return

    # Insert data into database
    insert_data(date, name, quantity, price, expiry_date, batch_number, invoice_number)

# Tkinter setup
root = tk.Tk()
root.title("Data Collection Form")

# Define labels and entry fields
tk.Label(root, text="Date (YYYY-MM-DD)").grid(row=0, column=0)
entry_date = tk.Entry(root)
entry_date.grid(row=0, column=1)

tk.Label(root, text="Name").grid(row=1, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1)

tk.Label(root, text="Quantity").grid(row=2, column=0)
entry_quantity = tk.Entry(root)
entry_quantity.grid(row=2, column=1)

tk.Label(root, text="Price").grid(row=3, column=0)
entry_price = tk.Entry(root)
entry_price.grid(row=3, column=1)

tk.Label(root, text="Expiry Date (YYYY-MM-DD)").grid(row=4, column=0)
entry_expiry = tk.Entry(root)
entry_expiry.grid(row=4, column=1)

tk.Label(root, text="Batch Number").grid(row=5, column=0)
entry_batch = tk.Entry(root)
entry_batch.grid(row=5, column=1)

tk.Label(root, text="Invoice Number").grid(row=6, column=0)
entry_invoice = tk.Entry(root)
entry_invoice.grid(row=6, column=1)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_data)
submit_button.grid(row=7, columnspan=2)

# Start the Tkinter main loop
root.mainloop()
