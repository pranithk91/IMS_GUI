import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
from datetime import datetime
import pandas as pd

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


def fetch_medicine_names():
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT *  FROM MedicineList")
        cols = ['MId',	'MName','MCompany',	'CurrentStock',	'MType', 'MRP',	'PTR',	
                'GST',	'HSN',	'Offer1',	'Offer2','Weight',	'Composition',	'Alternative']
        medicineData = pd.DataFrame(cursor.fetchall(), columns=cols)
        
        cursor.execute("SELECT MName  FROM MedicineList")  
        names = [row[0] for row in cursor.fetchall()]
        
        cursor.close()
        connection.close()
        return medicineData, names
    return []

fetch_medicine_names()

def fetch_magency_names():
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT AId, MAgency FROM MAgencies")
        mAgencyData=pd.DataFrame(cursor.fetchall(), columns=['AId', 'MAgency'])
        cursor.execute("SELECT MAgency FROM MAgencies")
        names = [row[0] for row in cursor.fetchall()]
        cursor.close()
        connection.close()
        return names#, mAgencyData
    return []




# Fetch data from invoices table for Invoice dropdown
def fetch_invoice_numbers():
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT BillNo FROM DeliveryBills")
        invoices = [row[0] for row in cursor.fetchall()]
        cursor.close()
        connection.close()
        return invoices
    return []

# Function to insert data into the MySQL table
def insert_data(deliverydate, name, quantity, price, batch_number, expiry_date, invoice_number):
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("Select MId from MedicineList where MName = '{}'".format(name))
            MId = cursor.fetchall()[0][0]
            cursor.execute("""
                INSERT INTO StockDeliveries (DeliveryDate, MId, DeliveryStock, price, batch_number,expiry_date, invoice_number)
                           	
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (deliverydate, MId, quantity, price,batch_number,  expiry_date,  invoice_number))
            connection.commit()
            print("Data inserted successfully!")
        except mysql.connector.Error as err:
            print(f"Failed to insert data: {err}")
        finally:
            cursor.close()
            connection.close()
