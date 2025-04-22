import customtkinter as ctk
import tkinter as tk
from tkcalendar import Calendar
from tkinter import messagebox
import mysql.connector
from PIL import Image
import subprocess

# App config
ctk.set_appearance_mode("light")
modify_app = ctk.CTk()
modify_app.geometry("1111x750")
modify_app.title("Modify Event Details")
modify_app.configure(fg_color="#7F5B6A")

# Top Frame
top_frame = ctk.CTkFrame(modify_app, height=81, fg_color="#D9D9D9", corner_radius=0)
top_frame.pack(fill="x")
title_label = ctk.CTkLabel(top_frame, text="MODIFY EVENT DETAILS", font=("Arial", 22, "bold"), text_color="black")
title_label.place(relx=0.06, rely=0.5, anchor="w")

# Proper CTkImage resize function
def resize_image(size, image_url):
    image = Image.open(image_url)
    return ctk.CTkImage(light_image=image, size=size)

# Function to go home
def go_home():
    subprocess.Popen(["python", "HomePage.py"])
    modify_app.destroy()

# Tooltip Label
tooltip_label = ctk.CTkLabel(modify_app, text="Logout", text_color="#000000", fg_color="#FFFFFF",
                             font=("Segoe UI", 10), corner_radius=4, width=60, height=20)
tooltip_label.place_forget()

# Go Back
def go_back():
    subprocess.Popen(["python", "CustomerDashboard.py"])
    modify_app.destroy()

def show_tooltip(event):
    tooltip_label.place(x=1010, y=65)

def hide_tooltip(event):
    tooltip_label.place_forget()

# Door Icon (logout)
door_icon = resize_image((55, 55), "icons/door.png")
door_label = ctk.CTkLabel(top_frame, text="", image=door_icon, fg_color="#D9D9D9", cursor="hand2")
door_label.place(x=1010, y=5)
door_label.bind("<Enter>", show_tooltip)
door_label.bind("<Leave>", hide_tooltip)
door_label.bind("<Button-1>", lambda e: go_home())

# Back Icon
back_icon = resize_image((40, 40), "icons/backarrow.png")
back_label = ctk.CTkLabel(top_frame, text="", image=back_icon, fg_color="#D9D9D9", cursor="hand2")
back_label.place(x=20, y=20)
back_label.bind("<Button-1>", lambda e: go_back())

# DB Update Function
def update_event(event_id, new_date, new_location):
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
        return True
    except Exception as e:
        messagebox.showerror("Database Error", str(e))
        return False

# Calendar popup
def show_calendar():
    top = tk.Toplevel(modify_app)
    top.title("Select Date")
    cal = Calendar(top, selectmode='day', date_pattern='mm/dd/yyyy')
    cal.pack(padx=10, pady=10)

    def get_date():
        selected_date = cal.get_date()
        date_entry.delete(0, tk.END)
        date_entry.insert(0, selected_date)
        top.destroy()

    ctk.CTkButton(top, text="OK", command=get_date).pack(pady=5)

# Save Changes Function
def save_changes():
    event_id = event_id_entry.get()
    new_date = date_entry.get()
    new_location = location_entry.get()

    if not all([event_id, new_date, new_location]):
        messagebox.showwarning("Missing Fields", "Please fill in all fields.")
        return

    success = update_event(event_id, new_date, new_location)
    if success:
        messagebox.showinfo("Success", "Event updated successfully!")
        event_id_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)
        location_entry.delete(0, tk.END)

# Form Container
form_frame = ctk.CTkFrame(modify_app, fg_color="#7F5B6A")
form_frame.pack(pady=40, padx=60, fill="both", expand=True)

# Form Title
ctk.CTkLabel(form_frame, text="EVENT ID", font=("Arial", 14), text_color="white")\
    .grid(row=0, column=0, sticky="w", padx=10, pady=(10, 2))
event_id_entry = ctk.CTkEntry(form_frame, width=950, height=40)
event_id_entry.grid(row=1, column=0, columnspan=3, padx=10, pady=(0, 10))

ctk.CTkLabel(form_frame, text="EVENT DATE", font=("Arial", 14), text_color="white")\
    .grid(row=2, column=0, sticky="w", padx=10, pady=(10, 2))
date_entry = ctk.CTkEntry(form_frame, width=950, height=40)
date_entry.grid(row=3, column=0, columnspan=3, padx=10, pady=(0, 10))
date_entry.bind("<Button-1>", lambda e: show_calendar())

ctk.CTkLabel(form_frame, text="LOCATION", font=("Arial", 14), text_color="white")\
    .grid(row=4, column=0, sticky="w", padx=10, pady=(10, 2))
location_entry = ctk.CTkEntry(form_frame, width=950, height=40)
location_entry.grid(row=5, column=0, columnspan=3, padx=10, pady=(0, 10))

save_button = ctk.CTkButton(form_frame, text="SAVE CHANGES", width=160, height=40, command=save_changes)
save_button.grid(row=6, column=0, columnspan=3, pady=30)

modify_app.mainloop()
