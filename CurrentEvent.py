import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import mysql.connector
from PIL import Image
import subprocess

# App setup
ctk.set_appearance_mode("light")
app = ctk.CTk()
app.geometry("1111x750")
app.title("Current Events")
app.configure(fg_color="#7F5B6A")

# Top frame
top_frame = ctk.CTkFrame(app, height=81, fg_color="#D9D9D9", corner_radius=0)
top_frame.pack(fill="x")
title_label = ctk.CTkLabel(top_frame, text="CURRENT EVENTS", font=("Arial", 22, "bold"), text_color="black")
title_label.place(relx=0.06, rely=0.5, anchor="w")

# Image resizer
def resize_image(size, path):
    img = Image.open(path)
    return ctk.CTkImage(light_image=img, size=size)

# Navigation
def go_back():
    subprocess.Popen(["python", "AdminDashboard.py"])
    app.destroy()

def go_home():
    subprocess.Popen(["python", "HomePage.py"])
    app.destroy()

# Icons
back_icon = resize_image((40, 40), "icons/backarrow.png")
back_label = ctk.CTkLabel(top_frame, text="", image=back_icon, fg_color="#D9D9D9", cursor="hand2")
back_label.place(x=20, y=20)
back_label.bind("<Button-1>", lambda e: go_back())

home_icon = resize_image((40, 40), "icons/door.png")
home_label = ctk.CTkLabel(top_frame, text="", image=home_icon, fg_color="#D9D9D9", cursor="hand2")
home_label.place(x=1050, y=20)
home_label.bind("<Button-1>", lambda e: go_home())

# Scrollable frame
content_frame = ctk.CTkScrollableFrame(app, fg_color="#EFEFEF", width=980, height=600, corner_radius=10)
content_frame.place(relx=0.5, rely=0.55, anchor="center")

# Table headers
headers = ["Event Name", "Date", "Time", "Location", "Duration", "Status", "Update", "Delete"]
for col, header in enumerate(headers):
    ctk.CTkLabel(content_frame, text=header, font=("Arial", 14, "bold"), text_color="black")\
        .grid(row=0, column=col, padx=8, pady=10)

# Update status in DB
def update_status(event_id, status_var):
    new_status = status_var.get()
    try:
        conn = mysql.connector.connect(
            host="141.209.241.57",
            user="tiruv1h",
            password="mypass",
            database="BIS698W1830_GRP1"
        )
        cursor = conn.cursor()
        cursor.execute("UPDATE events SET status = %s WHERE id = %s", (new_status, event_id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Status updated successfully!")
    except Exception as e:
        messagebox.showerror("Database Error", str(e))

# Delete event from DB
def delete_event(event_id):
    confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this event?")
    if confirm:
        try:
            conn = mysql.connector.connect(
                host="141.209.241.57",
                user="tiruv1h",
                password="mypass",
                database="BIS698W1830_GRP1"
            )
            cursor = conn.cursor()
            cursor.execute("DELETE FROM events WHERE id = %s", (event_id,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Deleted", "Event deleted successfully!")
            app.destroy()
            subprocess.Popen(["python", "CurrentEvent.py"])  # Reload the page
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

# Load and display events
def load_events():
    try:
        conn = mysql.connector.connect(
            host="141.209.241.57",
            user="tiruv1h",
            password="mypass",
            database="BIS698W1830_GRP1"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT id, event_name, date, time, location, duration, status FROM events ORDER BY date DESC")
        events = cursor.fetchall()
        conn.close()

        for i, event in enumerate(events, start=1):
            event_id, name, date, time, loc, dur, status = event

            ctk.CTkLabel(content_frame, text=name, font=("Arial", 12)).grid(row=i, column=0, padx=5, pady=5)
            ctk.CTkLabel(content_frame, text=str(date), font=("Arial", 12)).grid(row=i, column=1, padx=5, pady=5)
            ctk.CTkLabel(content_frame, text=time, font=("Arial", 12)).grid(row=i, column=2, padx=5, pady=5)
            ctk.CTkLabel(content_frame, text=loc, font=("Arial", 12)).grid(row=i, column=3, padx=5, pady=5)
            ctk.CTkLabel(content_frame, text=dur, font=("Arial", 12)).grid(row=i, column=4, padx=5, pady=5)

            status_var = tk.StringVar(value=status)
            status_menu = ctk.CTkComboBox(content_frame, variable=status_var, width=160, values=[
                "Planning in Process", "Booking Confirmed", "Vendors Booked", "Event Day"
            ])
            status_menu.grid(row=i, column=5, padx=5, pady=5)

            update_btn = ctk.CTkButton(content_frame, text="Update", width=80, height=30,
                                       command=lambda eid=event_id, var=status_var: update_status(eid, var))
            update_btn.grid(row=i, column=6, padx=5, pady=5)

            delete_btn = ctk.CTkButton(content_frame, text="Delete", width=80, height=30, fg_color="#c0392b",
                                       hover_color="#e74c3c", text_color="white",
                                       command=lambda eid=event_id: delete_event(eid))
            delete_btn.grid(row=i, column=7, padx=5, pady=5)

    except Exception as e:
        messagebox.showerror("Database Error", str(e))

load_events()
app.mainloop()
