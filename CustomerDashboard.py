import customtkinter as ctk
from PIL import Image
import subprocess

# App setup
app = ctk.CTk(fg_color="#7F5B6A")
app.title("Customer Dashboard")
app.geometry("1111x750")
app.resizable(False, False)

# Proper CTkImage resize function
def resize_image(size, image_url):
    image = Image.open(image_url)
    return ctk.CTkImage(light_image=image, size=size)

# Function to go home
def go_home():
    subprocess.Popen(["python", "HomePage.py"])
    app.destroy()

# ----------------- TOP FRAME -----------------
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

# Dashboard Title
dash_label = ctk.CTkLabel(top_frame, text="CUSTOMER DASHBOARD", text_color="#000000", font=('inter', 40))
dash_label.place(x=20, y=17)

# ----------------- FRAME 1: Create Events -----------------
frame1 = ctk.CTkFrame(app, width=284, height=244, fg_color="#D9D9D9", corner_radius=10)
frame1.place(x=80, y=120)

process_icon = resize_image((95, 95), "icons/Create Events.png")
process_button = ctk.CTkButton(frame1, text="", image=process_icon, fg_color="#D9D9D9", width=95, height=95)
process_button.place(x=95, y=30)

requests_label = ctk.CTkLabel(frame1, text="Create Events", text_color="#000000", font=('inter', 24))
requests_label.place(x=50, y=180)

# ----------------- FRAME 2: Modify Event Details -----------------
frame2 = ctk.CTkFrame(app, width=284, height=244, fg_color="#D9D9D9", corner_radius=10)
frame2.place(x=400, y=120)

event_icon = resize_image((95, 95), "icons/RequestToEditDetails.png")
event_button = ctk.CTkButton(frame2, text="", image=event_icon, fg_color="#D9D9D9", width=95, height=95)
event_button.place(x=95, y=30)

event_label = ctk.CTkLabel(frame2, text="Modify Event Details", text_color="#000000", font=('inter', 24))
event_label.place(x=30, y=180)

# ----------------- FRAME 3: Track Events -----------------
frame3 = ctk.CTkFrame(app, width=284, height=244, fg_color="#D9D9D9", corner_radius=10)
frame3.place(x=720, y=120)

contact_icon = resize_image((95, 95), "icons/Process Tracking.png")
contact_button = ctk.CTkButton(frame3, text="", image=contact_icon, fg_color="#D9D9D9", width=95, height=95)
contact_button.place(x=95, y=30)

contact_label = ctk.CTkLabel(frame3, text="Track Events", text_color="#000000", font=('inter', 24))
contact_label.place(x=60, y=180)

# Run the app
app.mainloop()
