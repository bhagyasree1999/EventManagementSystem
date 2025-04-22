import customtkinter as ctk
import tkinter as tk
import mysql.connector
from tkinter import messagebox
from PIL import Image
import subprocess

# App config
ctk.set_appearance_mode("light")
track_app = ctk.CTk()
track_app.geometry("1111x750")
track_app.title("Track Requests")
track_app.configure(fg_color="#7F5B6A")

# Top Frame
top_frame = ctk.CTkFrame(track_app, height=81, fg_color="#D9D9D9", corner_radius=0)
top_frame.pack(fill="x")
title_label = ctk.CTkLabel(top_frame, text="TRACK REQUESTS", font=("Arial", 22, "bold"), text_color="black")
title_label.place(relx=0.06, rely=0.5, anchor="w")

# Home button icon
def resize_image(size, image_url):
    image = Image.open(image_url)
    return ctk.CTkImage(light_image=image, size=size)

def go_home():
    subprocess.Popen(["python", "HomePage.py"])
    track_app.destroy()

# Go Back
def go_back():
    subprocess.Popen(["python", "CustomerDashboard.py"])
    track_app.destroy()

# Tooltip Label (appears below the door icon)
tooltip_label = ctk.CTkLabel(track_app, text="Logout", text_color="#000000", fg_color="#FFFFFF",
                             font=("Segoe UI", 10), corner_radius=4, width=60, height=20)
tooltip_label.place_forget()  # Hide initially

def show_tooltip(event):
    # Tooltip appears just below the door icon
    tooltip_label.place(x=1010, y=65)

def hide_tooltip(event):
    tooltip_label.place_forget()

home_icon = resize_image((55, 55), "icons/door.png")
home_label = ctk.CTkLabel(top_frame, text="", image=home_icon, fg_color="#D9D9D9", cursor="hand2")
home_label.place(x=1010, y=5)
home_label.bind("<Button-1>", lambda e: go_home())

# Back Icon
back_icon = resize_image((40, 40), "icons/backarrow.png")
back_label = ctk.CTkLabel(top_frame, text="", image=back_icon, fg_color="#D9D9D9", cursor="hand2")
back_label.place(x=20, y=20)
back_label.bind("<Button-1>", lambda e: go_back())

# Track Frame
track_frame = ctk.CTkFrame(track_app, fg_color="#F5F5F5", width=450, height=520, corner_radius=12)
track_frame.place(relx=0.5, rely=0.55, anchor="center")

# Fetch event status from database
def get_event_status(event_id):
    try:
        conn = mysql.connector.connect(
            host="141.209.241.57",
            user="tiruv1h",
            password="mypass",
            database="BIS698W1830_GRP1"
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT event_name, location, date, status FROM events WHERE id = %s", (event_id,))
        result = cursor.fetchone()
        conn.close()
        return result
    except Exception as e:
        messagebox.showerror("Database Error", str(e))
        return None

status_labels = []

def show_status():
    for lbl in status_labels:
        lbl.destroy()
    status_labels.clear()

    event_id = event_id_entry.get()
    data = get_event_status(event_id)
    if not data:
        return

    # Event Info Card
    card_frame = ctk.CTkFrame(track_frame, fg_color="white", width=400, corner_radius=8)
    card_frame.pack(pady=10)

    name = ctk.CTkLabel(card_frame, text=data['event_name'], font=("Arial", 18, "bold"), text_color="black")
    loc = ctk.CTkLabel(card_frame, text=f"\U0001F4CD {data['location']}", font=("Arial", 14), text_color="gray")
    date = ctk.CTkLabel(card_frame, text=f"\U0001F4C5 {data['date']}", font=("Arial", 14), text_color="gray")
    name.pack(pady=(10, 2))
    loc.pack()
    date.pack(pady=(0, 10))
    status_labels.extend([card_frame, name, loc, date])

    # Status
    steps = ["Booking Confirmed", "Planning in Process", "Vendors Booked", "Event Day"]
    current_status = data['status']
    status_index = steps.index(current_status) if current_status in steps else -1

    for i, step in enumerate(steps):
        icon = "\u2713" if i <= status_index else "\u25CB"
        color = "black" if i <= status_index else "#444444"
        lbl = ctk.CTkLabel(track_frame, text=f"{icon} {step}", font=("Arial", 15), text_color=color)
        lbl.pack(anchor="w", padx=50, pady=2)
        status_labels.append(lbl)

# Input for Event ID
event_id_label = ctk.CTkLabel(track_frame, text="Enter Event ID", font=("Arial", 14), text_color="black")
event_id_label.pack(pady=(25, 5))
event_id_entry = ctk.CTkEntry(track_frame, width=250, height=35)
event_id_entry.pack()

view_button = ctk.CTkButton(track_frame, text="Track Event", width=120, command=show_status)
view_button.pack(pady=(15, 10))

track_app.mainloop()
