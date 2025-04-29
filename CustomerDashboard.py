import customtkinter as ctk
import mysql.connector
from PIL import Image
import subprocess

# App setup
app = ctk.CTk(fg_color="#7F5B6A")
app.title("Customer Dashboard")
app.geometry("1111x750")
app.resizable(False, False)

# Image resize helper
def resize_image(size, image_url):
    image = Image.open(image_url)
    return ctk.CTkImage(light_image=image, size=size)

# Navigation functions
def go_home():
    subprocess.Popen(["python", "HomePage.py"])
    app.destroy()

def open_create_events():
    subprocess.Popen(["python", "CreateEvent.py"])
    app.destroy()

def open_modify_events():
    subprocess.Popen(["python", "ModifyEvent.py"])
    app.destroy()

def open_track_events():
    subprocess.Popen(["python", "TrackRequest.py"])
    app.destroy()

# Top Frame
top_frame = ctk.CTkFrame(app, width=1111, height=81, fg_color="#D9D9D9", corner_radius=0)
top_frame.place(x=0, y=0)

tooltip_label = ctk.CTkLabel(app, text="Logout", text_color="#000000", fg_color="#FFFFFF",
                             font=("Segoe UI", 10), corner_radius=4, width=60, height=20)
tooltip_label.place_forget()

def show_tooltip(event): tooltip_label.place(x=1010, y=65)
def hide_tooltip(event): tooltip_label.place_forget()

door_icon = resize_image((55, 55), "icons/door.png")
door_label = ctk.CTkLabel(top_frame, text="", image=door_icon, fg_color="#D9D9D9", cursor="hand2")
door_label.place(x=1010, y=5)
door_label.bind("<Enter>", show_tooltip)
door_label.bind("<Leave>", hide_tooltip)
door_label.bind("<Button-1>", lambda e: go_home())

with open("user_info.txt", "r") as f:
    user_first_name = f.read().strip()
dash_label = ctk.CTkLabel(top_frame, text=f"{user_first_name}'s Dashboard", text_color="#000000", font=('inter', 40))
dash_label.place(x=20, y=17)

# Frame 1: Create Events
frame1 = ctk.CTkFrame(app, width=284, height=244, fg_color="#D9D9D9", corner_radius=10)
frame1.place(x=80, y=120)

create_icon = resize_image((95, 95), "icons/Create Events.png")
create_button = ctk.CTkButton(frame1, text="", image=create_icon, fg_color="#D9D9D9",
                              width=95, height=95, command=open_create_events)
create_button.place(x=95, y=30)

create_label = ctk.CTkLabel(frame1, text="Create Events", text_color="#000000", font=('inter', 24))
create_label.place(x=50, y=180)

# Frame 2: Modify Event Details
frame2 = ctk.CTkFrame(app, width=284, height=244, fg_color="#D9D9D9", corner_radius=10)
frame2.place(x=400, y=120)

modify_icon = resize_image((95, 95), "icons/RequestToEditDetails.png")
modify_button = ctk.CTkButton(frame2, text="", image=modify_icon, fg_color="#D9D9D9",
                              width=95, height=95, command=open_modify_events)
modify_button.place(x=95, y=30)

modify_label = ctk.CTkLabel(frame2, text="Modify Event Details", text_color="#000000", font=('inter', 24))
modify_label.place(x=30, y=180)

# Frame 3: Track Events
frame3 = ctk.CTkFrame(app, width=284, height=244, fg_color="#D9D9D9", corner_radius=10)
frame3.place(x=720, y=120)

track_icon = resize_image((95, 95), "icons/Process Tracking.png")
track_button = ctk.CTkButton(frame3, text="", image=track_icon, fg_color="#D9D9D9",
                             width=95, height=95, command=open_track_events)
track_button.place(x=95, y=30)

track_label = ctk.CTkLabel(frame3, text="Track Events", text_color="#000000", font=('inter', 24))
track_label.place(x=60, y=180)

app.mainloop()