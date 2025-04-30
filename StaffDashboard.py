import customtkinter as ctk
from customtkinter import CTkImage
from PIL import Image
import subprocess

app = ctk.CTk(fg_color="#7F5B6A")
app.title("Staff Dashboard")
app.geometry("1111x750")
app.resizable(False, False)

def resize_image(size, image_url):
    """Load and resize image using CTkImage"""
    original_image = Image.open(image_url)
    return CTkImage(light_image=original_image, size=size)

def go_home():
    subprocess.Popen("python","Homepage.py")
    app.destroy()

def open_contactmanager():
    subprocess.Popen(["python", "ContactManager.py"])
    app.destroy()

def open_upcomingevents():
    subprocess.Popen(["python", "UpcomingEvents.py"])
    app.destroy()


# Top Frame
top_frame = ctk.CTkFrame(app, width=1111, height=81, fg_color="#D9D9D9", corner_radius=0)
top_frame.place(x=0, y=0)
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

# Dashboard text label
dash_label = ctk.CTkLabel(top_frame, text="STAFF DASHBOARD", text_color="#000000", font=('inter', 40))
dash_label.place(x=51, y=17)

# Frame1
frame1 = ctk.CTkFrame(app, width=284, height=244, fg_color="#D9D9D9", corner_radius=10)
frame1.place(x=80, y=120)

# Upcoming Events Photo
upcoming = resize_image((95, 95), "icons/UpcomingEvents.png")
upcoming_button = ctk.CTkButton(app, text="", image=upcoming, fg_color="#D9D9D9",command=open_upcomingevents)
upcoming_button.place(x=150, y=200)

# Upcoming Events Label
events_label = ctk.CTkLabel(frame1, text="Upcoming Events", text_color="#000000", font=('inter', 24))
events_label.place(x=50, y=180)

# Frame2
frame2 = ctk.CTkFrame(app, width=284, height=244, fg_color="#D9D9D9", corner_radius=10)
frame2.place(x=400, y=120)

# Contact Manager Photo
contact = resize_image((95, 95), "icons/Contact Admin.png")
contact_button = ctk.CTkButton(app, text="", image=contact, fg_color="#EBE6E6", command=open_contactmanager)
contact_button.place(x=475, y=200)

# Contact Manager Label
manager_label = ctk.CTkLabel(frame2, text="Contact Manager", text_color="#000000", font=('inter', 24))
manager_label.place(x=50, y=180)

app.mainloop()
