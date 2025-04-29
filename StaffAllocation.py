import customtkinter as ctk
import tkinter as tk
import mysql.connector
from mysql.connector import Error
import datetime
from PIL import Image
import subprocess

def fetch_staff_allocation_data():
    try:
        conn = mysql.connector.connect(
            host="141.209.241.57",
            user="tiruv1h",
            password="mypass",
            database="BIS698W1830_GRP1"
        )
        cursor = conn.cursor()
        cursor.execute("""
            SELECT name, event_role, DATE_FORMAT(event_date, '%Y-%m-%d'), location 
            FROM staff_allocation 
            ORDER BY event_date ASC
        """)
        return cursor.fetchall()
    except Error as e:
        print("Database error:", e)
        return []
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def fetch_event_data():
    try:
        conn = mysql.connector.connect(
            host="141.209.241.57",
            user="tiruv1h",
            password="mypass",
            database="BIS698W1830_GRP1"
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT event_name, date, location FROM events")
        return cursor.fetchall()
    except Error as e:
        print("Event fetch error:", e)
        return []
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def update_staff_assignment(name, role, date, location):
    try:
        conn = mysql.connector.connect(
            host="141.209.241.57",
            user="tiruv1h",
            password="mypass",
            database="BIS698W1830_GRP1"
        )
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE staff_allocation 
            SET event_role = %s, event_date = %s, location = %s 
            WHERE name = %s
        """, (role, date, location, name))
        conn.commit()
        return True
    except Error as e:
        print("Update error:", e)
        return False
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def open_assign_popup(name, old_role, old_date, old_location):
    popup = ctk.CTkToplevel(app)
    popup.title(f"Assign Event - {name}")
    popup.geometry("400x400")
    popup.grab_set()

    ctk.CTkLabel(popup, text=f"Assign event for {name}", font=("Arial", 18)).pack(pady=15)

    events = fetch_event_data()
    event_names = [e["event_name"] for e in events]
    selected_event = ctk.StringVar(value=event_names[0] if event_names else "")

    role_entry = ctk.CTkEntry(popup, placeholder_text="Event Role")
    role_entry.insert(0, old_role)
    role_entry.pack(pady=10)

    date_entry = ctk.CTkEntry(popup)
    date_entry.pack(pady=10)

    location_entry = ctk.CTkEntry(popup)
    location_entry.pack(pady=10)

    def autofill_fields(event_name):
        match = next((e for e in events if e["event_name"] == event_name), None)
        if match:
            date_entry.delete(0, tk.END)
            location_entry.delete(0, tk.END)
            try:
                formatted_date = datetime.datetime.strptime(match["date"], "%m/%d/%Y").strftime("%Y-%m-%d")
            except ValueError:
                formatted_date = match["date"]
            date_entry.insert(0, formatted_date)
            location_entry.insert(0, match["location"])

    dropdown = ctk.CTkOptionMenu(popup, values=event_names, variable=selected_event, command=autofill_fields)
    dropdown.pack(pady=10)
    autofill_fields(selected_event.get())

    def save_assignment():
        success = update_staff_assignment(name, role_entry.get(), date_entry.get(), location_entry.get())
        if success:
            ctk.CTkLabel(popup, text="Assignment saved!", text_color="green").pack()
        else:
            ctk.CTkLabel(popup, text="Error saving assignment", text_color="red").pack()
        popup.after(1500, popup.destroy)

    ctk.CTkButton(popup, text="Save", command=save_assignment).pack(pady=20)

# Main App
app = ctk.CTk()
app.title("Staff Dashboard")
app.geometry("1111x750")
app.configure(fg_color="#7F5B6A")
app.resizable(False, False)

# Header
header_frame = ctk.CTkFrame(app, height=80, width=1111, fg_color="#D9D9D9", corner_radius=0)
header_frame.place(x=0, y=0)
ctk.CTkLabel(header_frame, text="Staff Allocation", font=("Arial", 40, "bold"), text_color="#000000").place(x=70, y=20)

# Canvas for scrolling
canvas = tk.Canvas(app, bg="#7F5B6A", highlightthickness=0)
canvas.place(x=0, y=180, width=1110, height=670)

scrollbar = tk.Scrollbar(app, orient="vertical", command=canvas.yview)
scrollbar.place(x=1350, y=150, height=750)
canvas.configure(yscrollcommand=scrollbar.set)

frame_container = ctk.CTkFrame(canvas, fg_color="#7F5B6A")
canvas.create_window((0, 0), window=frame_container, anchor="nw")

def update_scroll(event):
    canvas.configure(scrollregion=canvas.bbox("all"))
frame_container.bind("<Configure>", update_scroll)

# Column headers
header_row = ctk.CTkFrame(frame_container, fg_color="grey", height=50)
header_row.pack(fill="x", padx=25, pady=(0, 15))
ctk.CTkLabel(header_row, text="Name", font=("Arial", 18, "bold"), text_color="white", width=200, anchor="w").pack(side="left", padx=(20, 0))
ctk.CTkLabel(header_row, text="Event Role", font=("Arial", 18, "bold"), text_color="white", width=320, anchor="w").pack(side="left")
ctk.CTkLabel(header_row, text="Date", font=("Arial", 18, "bold"), text_color="white", width=120, anchor="w").pack(side="left")
ctk.CTkLabel(header_row, text="Location", font=("Arial", 18, "bold"), text_color="white", width=120, anchor="w").pack(side="left")

# Staff rows
data = fetch_staff_allocation_data()
for index, (name, role, date, location) in enumerate(data):
    row_bg = "#E8E2E2" if index % 2 == 0 else "#D3CCD3"
    row = ctk.CTkFrame(frame_container, fg_color=row_bg, height=50, corner_radius=6)
    row.pack(fill="x", padx=25, pady=4)

    row.bind("<Button-1>", lambda e, n=name, r=role, d=date, l=location: open_assign_popup(n, r, d, l))
    for widget in [
        ctk.CTkLabel(row, text=name, font=("Arial", 16), text_color="#000000", width=200, anchor="w"),
        ctk.CTkLabel(row, text=role.upper(), font=("Arial", 16), text_color="#000000", width=320, anchor="w"),
        ctk.CTkLabel(row, text=date.upper(), font=("Arial", 16), text_color="#000000", width=120, anchor="w"),
        ctk.CTkLabel(row, text=location.upper(), font=("Arial", 16), text_color="#000000", width=120, anchor="w"),
    ]:
        widget.pack(side="left", padx=(20, 0) if widget.cget("text") == name else 10)
        widget.bind("<Button-1>", lambda e, n=name, r=role, d=date, l=location: open_assign_popup(n, r, d, l))

# Mousewheel scroll
def on_mousewheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
canvas.bind_all("<MouseWheel>", on_mousewheel)

# Function to go home
# Proper CTkImage resize function
def resize_image(size, image_url):
    image = Image.open(image_url)
    return ctk.CTkImage(light_image=image, size=size)

def go_home():
    subprocess.Popen(["python", "HomePage.py"])
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
door_label = ctk.CTkLabel(app, text="", image=door_icon, fg_color="#D9D9D9", cursor="hand2")
door_label.place(x=1010, y=5)
door_label.bind("<Enter>", show_tooltip)
door_label.bind("<Leave>", hide_tooltip)
door_label.bind("<Button-1>", lambda e: go_home())

# Go Back
def go_back():
    subprocess.Popen(["python", "AdminDashboard.py"])
    app.destroy()
# Back Icon
back_icon = resize_image((40, 40), "icons/backarrow.png")
back_label = ctk.CTkLabel(app, text="", image=back_icon, fg_color="#D9D9D9", cursor="hand2")
back_label.place(x=20, y=20)
back_label.bind("<Button-1>", lambda e: go_back())



app.mainloop()