import customtkinter as ctk
import tkinter as tk
from PIL import Image
import mysql.connector
from datetime import datetime
import subprocess

# App setup
ctk.set_appearance_mode("light")
admin_app = ctk.CTk()
admin_app.geometry("1111x750")
admin_app.title("Current Events")
admin_app.configure(fg_color="#7F5B6A")

# Helper: resize images
def resize_image(size, path):
    img = Image.open(path)
    return ctk.CTkImage(light_image=img, size=size)

# Header: Back and Logout
def go_back(): subprocess.Popen(["python", "AdminDashboard.py"]); admin_app.destroy()
def go_logout(): subprocess.Popen(["python", "HomePage.py"]); admin_app.destroy()

top_frame = ctk.CTkFrame(admin_app, height=81, fg_color="#D9D9D9", corner_radius=0)
top_frame.pack(fill="x")

ctk.CTkLabel(top_frame, text="CURRENT EVENTS", font=("Arial", 22, "bold"), text_color="black")\
    .place(relx=0.07, rely=0.5, anchor="w")

back_icon = resize_image((40, 40), "icons/backarrow.png")
logout_icon = resize_image((55, 55), "icons/door.png")

back_label = ctk.CTkLabel(top_frame, text="", image=back_icon, cursor="hand2")
back_label.place(x=10, y=20)
back_label.bind("<Button-1>", lambda e: go_back())

logout_label = ctk.CTkLabel(top_frame, text="", image=logout_icon, cursor="hand2")
logout_label.place(x=1010, y=5)
logout_label.bind("<Button-1>", lambda e: go_logout())

# Helper: calculate countdown
def get_day_countdown(date_str):
    try:
        today = datetime.now().date()
        event_date = datetime.strptime(date_str, "%m/%d/%Y").date()
        delta = (event_date - today).days
        return f"In {delta} Days" if delta > 0 else "Today" if delta == 0 else "Past"
    except:
        return "Unknown"

# Fetch and sort events by date
def fetch_events():
    try:
        conn = mysql.connector.connect(
            host="141.209.241.57",
            user="tiruv1h",
            password="mypass",
            database="BIS698W1830_GRP1"
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM events")
        data = cursor.fetchall()
        conn.close()
        # Sort by upcoming dates
        return sorted(data, key=lambda x: datetime.strptime(x['date'], "%m/%d/%Y"))
    except Exception as e:
        print("Error:", e)
        return []

# Delete event
def delete_event(event_id):
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
        load_events()
    except Exception as e:
        print("Delete Error:", e)

# UI Containers
search_var = tk.StringVar()
search_entry = ctk.CTkEntry(admin_app, width=300, placeholder_text="Search by name/location", textvariable=search_var)
search_entry.place(x=400, y=95)

body_frame = ctk.CTkFrame(admin_app, fg_color="#7F5B6A")
body_frame.pack(fill="both", expand=True, padx=20, pady=(140, 20))

canvas = tk.Canvas(body_frame, bg="#7F5B6A", highlightthickness=0)
scroll_y = tk.Scrollbar(body_frame, orient="vertical", command=canvas.yview)
scroll_frame = tk.Frame(canvas, bg="#7F5B6A")

scroll_frame.bind(
    "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
canvas.configure(yscrollcommand=scroll_y.set)

canvas.pack(side="left", fill="both", expand=True)
scroll_y.pack(side="right", fill="y")

# Load events
event_cards = []

def create_event_card(event):
    container = tk.Frame(scroll_frame, bg="#ECECEC", width=900, pady=10)
    container.pack(pady=10, padx=20, fill="x")

    title = tk.Label(container, text=event['event_name'].upper(), font=("Arial", 18, "bold"), bg="#ECECEC")
    countdown = tk.Label(container, text=get_day_countdown(event['date']), font=("Arial", 12), bg="#ECECEC")
    details = tk.Label(container, text=f"{event['date']}, {event['time']} - {event['duration']}", font=("Arial", 13), bg="#ECECEC")
    location = tk.Label(container, text=f"📍 {event['location']}", font=("Arial", 13), bg="#ECECEC")

    delete_btn = tk.Button(container, text="Delete", bg="#e74c3c", fg="white", command=lambda: delete_event(event['id']))
    # Optionally: edit_btn = tk.Button(container, text="Edit", bg="#3498db", fg="white")

    title.grid(row=0, column=0, sticky="w", padx=10)
    countdown.grid(row=0, column=1, sticky="e", padx=10)
    details.grid(row=1, column=0, sticky="w", padx=10, pady=(5, 0))
    location.grid(row=2, column=0, sticky="w", padx=10)
    delete_btn.grid(row=1, column=1, rowspan=2, sticky="e", padx=10)

    event_cards.append(container)

def load_events():
    for widget in event_cards:
        widget.destroy()
    event_cards.clear()

    keyword = search_var.get().lower()
    for ev in fetch_events():
        if keyword in ev['event_name'].lower() or keyword in ev['location'].lower():
            create_event_card(ev)

search_var.trace_add("write", lambda *args: load_events())
load_events()

admin_app.mainloop()
