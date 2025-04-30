import customtkinter as ctk
import tkinter as tk
from tkcalendar import Calendar
from tkinter import messagebox
import mysql.connector
from PIL import Image
import subprocess

# App config
ctk.set_appearance_mode("light")
app = ctk.CTk()
app.geometry("1111x750")
app.title("Create Events")
app.configure(fg_color="#7F5B6A")

# Top bar
top_frame = ctk.CTkFrame(app, height=81, fg_color="#D9D9D9", corner_radius=0)
top_frame.pack(fill="x")
title_label = ctk.CTkLabel(top_frame, text="CREATE EVENTS", font=("Arial", 22, "bold"), text_color="black")
title_label.place(relx=0.06, rely=0.5, anchor="w")

# Proper CTkImage resize function
def resize_image(size, image_url):
    image = Image.open(image_url)
    return ctk.CTkImage(light_image=image, size=size)

# Function to go home
def go_home():
    subprocess.Popen(["python", "HomePage.py"])
    app.destroy()

# Go Back
def go_back():
    subprocess.Popen(["python", "CustomerDashboard.py"])
    app.destroy()

# Tooltip Label (appears below the door icon)
tooltip_label = ctk.CTkLabel(app, text="Logout", text_color="#000000", fg_color="#FFFFFF",
                             font=("Segoe UI", 10), corner_radius=4, width=60, height=20)
tooltip_label.place_forget()  # Hide initially

def show_tooltip(event):
    # Tooltip appears just below the door icon
    tooltip_label.place(x=1010, y=65)

def hide_tooltip(event):
    tooltip_label.place_forget()

# Door Icon (logout) as CTkLabel to allow hover
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



# Form frame
form_frame = ctk.CTkFrame(app, fg_color="#7F5B6A")
form_frame.pack(pady=40, padx=60, fill="both", expand=True)

# DB Insert Function
def insert_event(event_name, location, date, time, duration, description, customer_email):
    try:
        # Read email from file
        # with open("user_email.txt", "r") as f:
        #     customer_email = f.read().strip()
        # print("[DEBUG] Email to insert into DB:", customer_email)
        # print(type(customer_email))
        #
        # if not customer_email or customer_email == "unknown@example.com":
        #     raise Exception("Invalid email in user_email.txt")
        #
        # print("[DEBUG] Email to insert into DB:", customer_email)

        conn = mysql.connector.connect(
            host="141.209.241.57",
            user="tiruv1h",
            password="mypass",
            database="BIS698W1830_GRP1"
        )
        cursor = conn.cursor()

        query = """
            INSERT INTO events (event_name, location, date, time, duration, description, email)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (event_name, location, date, time, duration, description, customer_email,))
        conn.commit()
        conn.close()
        return True

    # except FileNotFoundError:
    #     messagebox.showerror("Login Required", "Please login again before creating an event.")
    #     return False

    except Exception as e:
        messagebox.showerror("Database Error", str(e))
        return False

# Calendar popup
def show_calendar():
    top = tk.Toplevel(app)
    top.title("Select Date")
    cal = Calendar(top, selectmode='day', date_pattern='mm/dd/yyyy')
    cal.pack(padx=10, pady=10)

    def get_date():
        selected_date = cal.get_date()
        date_entry.delete(0, tk.END)
        date_entry.insert(0, selected_date)
        top.destroy()

    ctk.CTkButton(top, text="OK", command=get_date).pack(pady=5)

# Time picker popup
def show_time_picker():
    def set_time():
        hour = hour_spin.get()
        minute = minute_spin.get()
        meridian = am_pm_spin.get()
        formatted = f"{hour}:{minute} {meridian}"
        time_entry.delete(0, tk.END)
        time_entry.insert(0, formatted)
        top.destroy()

    top = tk.Toplevel(app)
    top.title("Select Time")
    top.geometry("200x150")

    tk.Label(top, text="Hour").pack()
    hour_spin = tk.Spinbox(top, from_=1, to=12, width=5)
    hour_spin.pack()

    tk.Label(top, text="Minute").pack()
    minute_spin = tk.Spinbox(top, from_=0, to=59, width=5, format="%02.0f")
    minute_spin.pack()

    tk.Label(top, text="AM/PM").pack()
    am_pm_spin = tk.Spinbox(top, values=("AM", "PM"), width=5)
    am_pm_spin.pack()

    tk.Button(top, text="OK", command=set_time).pack(pady=10)

# Confirmation popup
def show_confirmation():
    event = event_entry.get()
    loc = location_entry.get()
    date = date_entry.get()
    time_ = time_entry.get()
    duration = duration_entry.get()
    desc = description_entry.get()
    print(type(desc));
    if not all([event, loc, date, time_, duration, desc]):
        messagebox.showwarning("Missing Fields", "Please fill out all fields before submitting.")
        return
    try:
        # Read email from file
        with open("user_email.txt", "r") as f:
            customer_email = f.read().strip()
        print("[DEBUG] Email to insert into DB:", customer_email)
        print(type(customer_email))

        # if not customer_email or customer_email == "unknown@example.com":
        #     raise Exception("Invalid email in user_email.txt")

        print("[DEBUG] Email to insert into DB:", customer_email)
    except FileNotFoundError:
        messagebox.showerror("Login Required", "Please login again before creating an event.")
        return False

    except Exception as e:
        messagebox.showerror("Database Error", str(e))
        return False
    success = insert_event(event, loc, date, time_, duration, desc, customer_email)

    if success:
        popup = ctk.CTkToplevel(app)
        popup.title("Event Created")
        popup.geometry("350x150")
        popup.resizable(False, False)
        popup.configure(fg_color="#FFFFFF")

        # Center popup on screen
        try:
            popup.update_idletasks()
            x = app.winfo_rootx() + (app.winfo_width() // 2) - (350 // 2)
            y = app.winfo_rooty() + (app.winfo_height() // 2) - (150 // 2)
            popup.geometry(f"+{x}+{y}")
        except Exception as e:
            print("[WARN] Centering popup failed:", e)
            popup.geometry("350x150+500+300")  # fallback to fixed position

        # Confirmation message
        success_label = ctk.CTkLabel(
            popup,
            text="✅ Event Created Successfully!",
            font=("Arial", 16, "bold"),
            text_color="#222222"
        )
        success_label.pack(pady=(35, 10))

        subtext = ctk.CTkLabel(
            popup,
            text="Admin will review and contact you.",
            font=("Arial", 13),
            text_color="#555555"
        )
        subtext.pack()

        # Close button
        close_button = ctk.CTkButton(popup, text="CLOSE", width=100, command=popup.destroy)
        close_button.pack(pady=15)

        # Clear all fields
        event_entry.delete(0, tk.END)
        location_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)
        time_entry.delete(0, tk.END)
        duration_entry.delete(0, tk.END)
        description_entry.delete(0, tk.END)

# Layout
ctk.CTkLabel(form_frame, text="EVENT NAME", font=("Arial", 14), text_color="white").grid(row=0, column=0, columnspan=3, sticky="w", padx=10, pady=(10, 2))
event_entry = ctk.CTkEntry(form_frame, width=950, height=40)
event_entry.grid(row=1, column=0, columnspan=3, padx=10, pady=(0, 10))

ctk.CTkLabel(form_frame, text="LOCATION", font=("Arial", 14), text_color="white").grid(row=2, column=0, columnspan=3, sticky="w", padx=10, pady=(10, 2))
location_entry = ctk.CTkEntry(form_frame, width=950, height=40)
location_entry.grid(row=3, column=0, columnspan=3, padx=10, pady=(0, 10))

ctk.CTkLabel(form_frame, text="DATE", font=("Arial", 14), text_color="white").grid(row=4, column=0, padx=10, pady=(10, 2), sticky="w")
ctk.CTkLabel(form_frame, text="TIME", font=("Arial", 14), text_color="white").grid(row=4, column=1, padx=10, pady=(10, 2), sticky="w")
ctk.CTkLabel(form_frame, text="DURATION", font=("Arial", 14), text_color="white").grid(row=4, column=2, padx=10, pady=(10, 2), sticky="w")

date_entry = ctk.CTkEntry(form_frame, width=280, height=40)
date_entry.grid(row=5, column=0, padx=10, pady=(0, 10))
date_entry.bind("<Button-1>", lambda e: show_calendar())

time_entry = ctk.CTkEntry(form_frame, width=280, height=40)
time_entry.grid(row=5, column=1, padx=10, pady=(0, 10))
time_entry.bind("<Button-1>", lambda e: show_time_picker())

duration_entry = ctk.CTkEntry(form_frame, width=280, height=40)
duration_entry.grid(row=5, column=2, padx=10, pady=(0, 10))

ctk.CTkLabel(form_frame, text="DESCRIPTION", font=("Arial", 14), text_color="white").grid(row=6, column=0, columnspan=3, sticky="w", padx=10, pady=(10, 2))
description_entry = ctk.CTkEntry(form_frame, width=950, height=40)
description_entry.grid(row=7, column=0, columnspan=3, padx=10, pady=(0, 10))

create_button = ctk.CTkButton(form_frame, text="CREATE", width=160, height=40, command=show_confirmation)
create_button.grid(row=8, column=0, columnspan=3, pady=30)

app.mainloop()