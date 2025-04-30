import customtkinter as ctk
import tkinter as tk
import mysql.connector
from mysql.connector import Error

# Fetch upcoming events
def fetch_upcoming_events():
    try:
        conn = mysql.connector.connect(
            host="141.209.241.57",
            user="tiruv1h",
            password="mypass",
            database="BIS698W1830_GRP1"
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT event_name FROM events ORDER BY date ASC")
        return cursor.fetchall()
    except Error as e:
        print("DB Error:", e)
        return []
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def logout(): pass
def add_event(): pass

# App Window
app = ctk.CTk()
app.geometry("400x500")
app.title("Upcoming Events")
app.configure(fg_color="#7F5B6A")

# Header
header = ctk.CTkFrame(app, fg_color="#C9C0C0", height=50, corner_radius=0)
header.pack(fill="x")

ctk.CTkButton(header, text="+", width=40, command=add_event, fg_color="transparent").place(x=10, y=10)
ctk.CTkLabel(header, text="UPCOMING EVENTS", font=("Arial", 14, "bold"), text_color="black").place(relx=0.5, rely=0.5, anchor="center")
ctk.CTkButton(header, text="⎋", width=40, command=logout, fg_color="transparent").place(relx=1.0, x=-50, y=10)

# Scrollable container
canvas = tk.Canvas(app, bg="#7F5B6A", highlightthickness=0)
canvas.pack(fill="both", expand=True)

scrollbar = tk.Scrollbar(app, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.configure(yscrollcommand=scrollbar.set)

scrollable_frame = ctk.CTkFrame(canvas, fg_color="#A88FA3")
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

def configure_scroll(event):
    canvas.configure(scrollregion=canvas.bbox("all"))
scrollable_frame.bind("<Configure>", configure_scroll)

# Event cards
events = fetch_upcoming_events()

for i, event in enumerate(events):
    card = ctk.CTkFrame(scrollable_frame, fg_color="#D9D9D9", width=250, height=60, corner_radius=10)
    card.pack(pady=20, padx=50)

    icon_label = ctk.CTkLabel(card, text="📅", font=("Arial", 20))
    icon_label.place(x=10, y=15)

    event_label = ctk.CTkLabel(card, text=event["event_name"], font=("Arial", 14, "bold"), text_color="black")
    event_label.place(x=50, y=18)

app.mainloop()
