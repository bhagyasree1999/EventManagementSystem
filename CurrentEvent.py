import customtkinter as ctk
import tkinter as tk
from tkinter import simpledialog
from PIL import Image
from datetime import datetime
import mysql.connector
import subprocess

# === App Setup ===
ctk.set_appearance_mode("light")
admin_app = ctk.CTk()
admin_app.geometry("1111x750")
admin_app.title("Current Events")
admin_app.configure(fg_color="#7F5B6A")

# === Utility Functions ===
def resize_image(size, path):
    return ctk.CTkImage(light_image=Image.open(path), size=size)

def open_window(script):
    subprocess.Popen(["python", script])
    admin_app.destroy()

def db_connect():
    return mysql.connector.connect(
        host="141.209.241.57",
        user="tiruv1h",
        password="mypass",
        database="BIS698W1830_GRP1"
    )

def get_day_countdown(date_str):
    try:
        delta = (datetime.strptime(date_str, "%m/%d/%Y").date() - datetime.now().date()).days
        return f"In {delta} Days" if delta > 0 else "Today" if delta == 0 else "Past"
    except:
        return "Unknown"

# === Top Frame ===
top_frame = ctk.CTkFrame(admin_app, height=81, fg_color="#D9D9D9", corner_radius=0)
top_frame.pack(fill="x")

ctk.CTkLabel(top_frame, text="CURRENT EVENTS", font=("Arial", 22, "bold"), text_color="black").place(relx=0.07, rely=0.5, anchor="w")

back_label = ctk.CTkLabel(top_frame, text="", image=resize_image((40, 40), "icons/backarrow.png"), cursor="hand2")
back_label.place(x=10, y=20)
back_label.bind("<Button-1>", lambda e: open_window("AdminDashboard.py"))

logout_label = ctk.CTkLabel(top_frame, text="", image=resize_image((55, 55), "icons/door.png"), cursor="hand2")
logout_label.place(x=1010, y=5)
logout_label.bind("<Button-1>", lambda e: open_window("HomePage.py"))

# === Search and Scroll Area ===
search_var = tk.StringVar()
ctk.CTkEntry(admin_app, width=300, placeholder_text="Search by name/location", textvariable=search_var).place(x=400, y=95)

body_frame = ctk.CTkFrame(admin_app, fg_color="#7F5B6A")
body_frame.pack(fill="both", expand=True, padx=20, pady=(140, 20))

canvas = tk.Canvas(body_frame, bg="#7F5B6A", highlightthickness=0)
scroll_y = tk.Scrollbar(body_frame, orient="vertical", command=canvas.yview)
scroll_frame = tk.Frame(canvas, bg="#7F5B6A")

canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
canvas.configure(yscrollcommand=scroll_y.set)
scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.pack(side="left", fill="both", expand=True)
scroll_y.pack(side="right", fill="y")

# === Event Logic ===
event_cards = []

def fetch_events():
    try:
        conn = db_connect()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM events")
        data = cursor.fetchall()
        conn.close()
        return sorted(data, key=lambda x: datetime.strptime(x['date'], "%m/%d/%Y"))
    except Exception as e:
        print("Error fetching events:", e)
        return []

def delete_event(event_id):
    try:
        conn = db_connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM events WHERE id = %s", (event_id,))
        conn.commit()
        conn.close()
        load_events()
    except Exception as e:
        print("Delete Error:", e)

def update_status(event_id):
    new_status = simpledialog.askstring("Update Status", "Enter new status (e.g. Planning in Process, Vendors Booked, Event Day):")
    if new_status:
        try:
            conn = db_connect()
            cursor = conn.cursor()
            cursor.execute("UPDATE events SET status = %s WHERE id = %s", (new_status, event_id))
            conn.commit()
            conn.close()
            load_events()
        except Exception as e:
            print("Update Error:", e)

def create_event_card(event):
    container = tk.Frame(scroll_frame, bg="#ECECEC", width=900, pady=10)
    container.pack(pady=10, padx=20, fill="x")

    tk.Label(container, text=event['event_name'].upper(), font=("Arial", 18, "bold"), bg="#ECECEC").grid(row=0, column=0, sticky="w", padx=10)
    tk.Label(container, text=get_day_countdown(event['date']), font=("Arial", 12), bg="#ECECEC").grid(row=0, column=1, sticky="e", padx=10)
    tk.Label(container, text=f"{event['date']}, {event['time']} - {event['duration']}", font=("Arial", 13), bg="#ECECEC").grid(row=1, column=0, sticky="w", padx=10, pady=(5, 0))
    tk.Label(container, text=f"📍 {event['location']}", font=("Arial", 13), bg="#ECECEC").grid(row=2, column=0, sticky="w", padx=10)

    tk.Button(container, text="Delete", bg="#e74c3c", fg="white", command=lambda: delete_event(event['id'])).grid(row=1, column=1, sticky="e", padx=5)
    tk.Button(container, text="Update", bg="#3498db", fg="white", command=lambda: update_status(event['id'])).grid(row=2, column=1, sticky="e", padx=5)

    event_cards.append(container)

def load_events():
    for card in event_cards:
        card.destroy()
    event_cards.clear()

    keyword = search_var.get().lower()
    for event in fetch_events():
        if keyword in event['event_name'].lower() or keyword in event['location'].lower():
            create_event_card(event)

search_var.trace_add("write", lambda *args: load_events())
load_events()

admin_app.mainloop()
