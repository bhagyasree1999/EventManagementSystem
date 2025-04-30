import customtkinter as ctk
import tkinter as tk
from tkcalendar import Calendar
from tkinter import messagebox
import mysql.connector
from PIL import Image
import subprocess
from datetime import datetime

# App config
ctk.set_appearance_mode("light")
modify_app = ctk.CTk()
modify_app.geometry("750x600")
modify_app.title("Modify Event Details")
modify_app.configure(fg_color="#7F5B6A")

# Top Frame
top_frame = ctk.CTkFrame(modify_app, height=81, fg_color="#D9D9D9", corner_radius=0)
top_frame.pack(fill="x")
title_label = ctk.CTkLabel(top_frame, text="MODIFY EVENT DETAILS", font=("Arial", 22, "bold"), text_color="black")
title_label.place(relx=0.10, rely=0.5, anchor="w")

# Resize image utility
def resize_image(size, image_url):
    image = Image.open(image_url)
    return ctk.CTkImage(light_image=image, size=size)

# Navigation
def go_home():
    subprocess.Popen(["python", "HomePage.py"])
    modify_app.destroy()

def go_back():
    subprocess.Popen(["python", "CustomerDashboard.py"])
    modify_app.destroy()

# Tooltip
tooltip_label = ctk.CTkLabel(modify_app, text="Logout", text_color="#000000", fg_color="#FFFFFF",
                             font=("Segoe UI", 10), corner_radius=4, width=60, height=20)
tooltip_label.place_forget()

def show_tooltip(event): tooltip_label.place(x=650, y=65)
def hide_tooltip(event): tooltip_label.place_forget()

# Icons
door_icon = resize_image((55, 55), "icons/door.png")
door_label = ctk.CTkLabel(top_frame, text="", image=door_icon, fg_color="#D9D9D9", cursor="hand2")
door_label.place(x=650, y=5)
door_label.bind("<Enter>", show_tooltip)
door_label.bind("<Leave>", hide_tooltip)
door_label.bind("<Button-1>", lambda e: go_home())

back_icon = resize_image((40, 40), "icons/backarrow.png")
back_label = ctk.CTkLabel(top_frame, text="", image=back_icon, fg_color="#D9D9D9", cursor="hand2")
back_label.place(x=20, y=20)
back_label.bind("<Button-1>", lambda e: go_back())

# Read logged-in email
try:
    with open("user_email.txt", "r") as f:
        customer_email = f.read().strip()
except FileNotFoundError:
    messagebox.showerror("Error", "User email file not found.")
    modify_app.destroy()
    exit()

# Form Frame
form_frame = ctk.CTkFrame(modify_app, fg_color="white", corner_radius=10)
form_frame.pack(pady=30, padx=40, fill="both", expand=True)

# Event Mapping
event_display_map = {}

# Dropdown Label
ctk.CTkLabel(form_frame, text="SELECT EVENT", font=("Arial", 15, "bold"), text_color="black")\
    .grid(row=0, column=0, sticky="w", padx=120, pady=(20, 5))

# Dropdown Styled
event_dropdown = ctk.CTkComboBox(
    form_frame,
    width=400,
    height=35,
    font=("Arial", 13),
    button_color="#444444",
    dropdown_font=("Arial", 13),
    state="readonly",
    command=lambda _: populate_event_fields()
)
event_dropdown.grid(row=1, column=0, padx=120, pady=(0, 20))

# Date Field
ctk.CTkLabel(form_frame, text="EVENT DATE", font=("Arial", 15, "bold"), text_color="black")\
    .grid(row=2, column=0, sticky="w", padx=120, pady=(0, 5))
date_entry = ctk.CTkEntry(form_frame, width=400, height=35)
date_entry.grid(row=3, column=0, padx=120, pady=(0, 20))
date_entry.bind("<Button-1>", lambda e: show_calendar())

# Location Field
ctk.CTkLabel(form_frame, text="LOCATION", font=("Arial", 15, "bold"), text_color="black")\
    .grid(row=4, column=0, sticky="w", padx=120, pady=(0, 5))
location_entry = ctk.CTkEntry(form_frame, width=400, height=35)
location_entry.grid(row=5, column=0, padx=120, pady=(0, 30))

# Save Button
save_button = ctk.CTkButton(
    form_frame, text="💾 SAVE CHANGES", width=160, height=40,
    fg_color="#4CAF50", hover_color="#45A049", text_color="white", font=("Arial", 13, "bold"),
    command=lambda: save_changes()
)
save_button.grid(row=6, column=0, pady=(0, 20))

# Show Calendar
def show_calendar():
    top = tk.Toplevel(modify_app)
    top.title("Select Date")
    cal = Calendar(top, selectmode='day', date_pattern='yyyy-mm-dd')
    cal.pack(padx=10, pady=10)

    def get_date():
        selected_date = cal.get_date()
        date_entry.delete(0, tk.END)
        date_entry.insert(0, selected_date)
        top.destroy()

    ctk.CTkButton(top, text="OK", command=get_date).pack(pady=5)

# Load Dropdown Events
def load_customer_events():
    global event_display_map
    try:
        conn = mysql.connector.connect(
            host="141.209.241.57",
            user="tiruv1h",
            password="mypass",
            database="BIS698W1830_GRP1"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT id, event_name, date, location FROM events WHERE email = %s ORDER BY date DESC", (customer_email,))
        events = cursor.fetchall()
        conn.close()

        options = []
        event_display_map = {}
        for eid, name, date, location in events:
            formatted_date = date.strftime('%Y-%m-%d') if isinstance(date, datetime) else str(date)
            display_text = f"{name} ({formatted_date})"
            options.append(display_text)
            event_display_map[display_text] = (eid, formatted_date, location)

        event_dropdown.configure(values=options)
        if options:
            event_dropdown.set(options[0])
            populate_event_fields()
        else:
            messagebox.showinfo("No Events", "No events found for this customer.")
    except Exception as e:
        messagebox.showerror("Database Error", str(e))

# Populate Form Fields
def populate_event_fields():
    selected = event_dropdown.get()
    if selected in event_display_map:
        _, date, location = event_display_map[selected]
        date_entry.delete(0, tk.END)
        date_entry.insert(0, date)
        location_entry.delete(0, tk.END)
        location_entry.insert(0, location)

# Save Updates
def save_changes():
    selected = event_dropdown.get()
    if selected not in event_display_map:
        messagebox.showwarning("Missing Selection", "Please select an event to update.")
        return

    event_id, _, _ = event_display_map[selected]
    new_date = date_entry.get()
    new_location = location_entry.get()

    if not all([new_date, new_location]):
        messagebox.showwarning("Missing Fields", "Please fill in all fields.")
        return

    try:
        conn = mysql.connector.connect(
            host="141.209.241.57",
            user="tiruv1h",
            password="mypass",
            database="BIS698W1830_GRP1"
        )
        cursor = conn.cursor()
        query = """
            UPDATE events
            SET date = %s, location = %s
            WHERE id = %s
        """
        cursor.execute(query, (new_date, new_location, event_id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Event updated successfully!")
    except Exception as e:
        messagebox.showerror("Database Error", str(e))

# Start
load_customer_events()
modify_app.mainloop()
