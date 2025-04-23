import customtkinter as ctk
import tkinter as tk
import mysql.connector
from mysql.connector import Error

#MySQL Connection & Data Fetch
def fetch_staff_allocation_data():

    try:
        connection = mysql.connector.connect(
            host="141.209.241.57",
            user="surak1m",
            password="mypass",
            database="BIS698W1830_GRP1"
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("""
                SELECT name, event_role, DATE_FORMAT(event_date, '%b %e'), location 
                FROM staff_allocation 
                ORDER BY event_date ASC 
                LIMIT 8
            """)
            return cursor.fetchall()
    except Error as e:
        print("Database error:", e)
        return []
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

#Screen
app = ctk.CTk(fg_color="#7F5B6A")
app.title("Staff Dashboard")
app.geometry("1111x750")
app.resizable(False, False)

#Frame 1- Header
header_frame = ctk.CTkFrame(app, width=1111, height=81, fg_color="#D9D9D9", corner_radius=0)
header_frame.place(x=0, y=0)

header_label = ctk.CTkLabel(header_frame, text="Staff Allocation", text_color="#000000", font=('Arial', 40, 'bold'))
header_label.place(x=30, y=15)

#Table Headers
table_frame = ctk.CTkFrame(app, width=1111, height=60, fg_color="#805060", corner_radius=5)
table_frame.place(x=0, y=81)

headers = ["Name", "Event Role", "Date", "Location"]
x_positions = [110, 370, 650, 840]

for i, text in enumerate(headers):
    label = ctk.CTkLabel(table_frame, text=text, text_color="#000000", font=("Arial", 18, "bold"))
    label.place(x=x_positions[i], y=15)

#Table Data Rows
data = fetch_staff_allocation_data()
row_y_start = 150
row_height = 70

for index, (name, role, date, location) in enumerate(data):
    row_y = row_y_start + index * row_height

    row_frame = ctk.CTkFrame(app, width=1000, height=60, fg_color="#D3CCD3", corner_radius=5)
    row_frame.place(x=55, y=row_y)

    # Each column in the row
    ctk.CTkLabel(row_frame, text=name, text_color="#000000", font=("Arial", 16)).place(x=30, y=15)
    ctk.CTkLabel(row_frame, text=role.upper(), text_color="#000000", font=("Arial", 16)).place(x=260, y=15)
    ctk.CTkLabel(row_frame, text=date.upper(), text_color="#000000", font=("Arial", 16)).place(x=580, y=15)
    ctk.CTkLabel(row_frame, text=location.upper(), text_color="#000000", font=("Arial", 16)).place(x=800, y=15)


app.mainloop()