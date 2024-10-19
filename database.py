import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
from datetime import datetime
import pandas as pd

months = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun", 
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

def connectToDB():
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
connectToDB()

def fetchMedicineNames():
    connection = connectToDB()
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

#fetch_medicine_names()

def fetchMagencyNames():
    connection = connectToDB()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT AId, MAgency FROM MAgencies")
        mAgencyData=pd.DataFrame(cursor.fetchall(), columns=['AId', 'MAgency'])
        cursor.execute("SELECT MAgency FROM MAgencies")
        names = [row[0] for row in cursor.fetchall()]
        cursor.close()
        connection.close()
        return names, mAgencyData
    return []




# Fetch data from invoices table for Invoice dropdown
def fetchInvoiceNumbers():
    connection = connectToDB()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT BillNo FROM DeliveryBills")
        invoices = [row[0] for row in cursor.fetchall()]
        cursor.close()
        connection.close()
        return invoices
    return []

# Function to insert data into the MySQL table
def insertBillItemsData(deliverydate, name, quantity, price, priceChange, batch_number, expiry_date, invoice_number, saleableStock):
    connection = connectToDB()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("Select MId from MedicineList where MName = '{}'".format(name))
            MId = cursor.fetchall()[0][0]
            if len(expiry_date) == 4:
                expDate = months[int(expiry_date[0])] + " 20" + expiry_date[2:] 
            elif len(expiry_date) == 5:
                expDate = months[int(expiry_date[:2])] + " 20" + expiry_date[3:]
            if saleableStock:
                cursor.execute("""
                    INSERT INTO StockDeliveries (DeliveryDate, MId, SaleableStock, NewMRP, PriceChange,BatchNumber,ExpiryDate, BillNo)
                                
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, (deliverydate, MId, quantity, price, priceChange, batch_number,   expDate,  invoice_number))
                connection.commit()
                print("Data inserted successfully!")
            else:
                cursor.execute("""
                    INSERT INTO StockDeliveries (DeliveryDate, MId, DeliveryStock, NewMRP, PriceChange,BatchNumber,ExpiryDate, BillNo)
                                
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, (deliverydate, MId, quantity, price, priceChange, batch_number,   expDate,  invoice_number))
                connection.commit()
                print("Data inserted successfully!")
        except mysql.connector.Error as err:
            print(f"Failed to insert data: {err}")
        finally:
            cursor.close()
            connection.close()


def insertDeliveryBillData(invDate, invNumber, mAgency, billAmount, discountInBill, discountPercent, billInFile, saleableStock=False):
    connection = connectToDB()
    if connection:
        cursor = connection.cursor()
        try:
            
            if saleableStock:
                print("This is saleable stock")
            else:
                cursor.execute("Select AId from MAgencies where MAgency = '{}'".format(mAgency))
                AId = cursor.fetchall()[0][0]
                cursor.execute("""
                        INSERT INTO DeliveryBills (BillDate, BillNo, MAgency, BillAmount, DiscountInBill, DiscountPercent, BillInFile)
                                    
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """, (invDate, invNumber, mAgency, billAmount, discountInBill, discountPercent, billInFile))
                connection.commit()
                print("Data inserted successfully!")
        except mysql.connector.Error as err:
            print(f"Failed to insert data: {err}")
        finally:
            cursor.close()
            connection.close()