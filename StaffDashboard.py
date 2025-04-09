import customtkinter as ctk
from customtkinter import CTkImage
from PIL import Image

app = ctk.CTk(fg_color="#7F5B6A")
app.title("Staff Dashboard")
app.geometry("1111x851")
app.resizable(False, False)

def resize_image(size, image_url):
    """Load and resize image using CTkImage"""
    original_image = Image.open(image_url)
    return CTkImage(light_image=original_image, size=size)

# Top Frame
top_frame = ctk.CTkFrame(app, width=1111, height=81, fg_color="#D9D9D9", corner_radius=10)
top_frame.place(x=0, y=0)

# Calendar Photo
calendar = resize_image((64, 64), "icons/calendar.png")
calendar_label = ctk.CTkLabel(top_frame, text="", image=calendar, fg_color="#D9D9D9")
calendar_label.place(x=900, y=15)

# Menu Photo
menu = resize_image((64, 64), "icons/Menu.png")
menu_label = ctk.CTkLabel(top_frame, text="", image=menu, fg_color="#D9D9D9")
menu_label.place(x=1000, y=15)

# Dashboard text label
dash_label = ctk.CTkLabel(top_frame, text="STAFF DASHBOARD", text_color="#000000", font=('inter', 40))
dash_label.place(x=51, y=17)

# Frame1
frame1 = ctk.CTkFrame(app, width=284, height=244, fg_color="#D9D9D9", corner_radius=10)
frame1.place(x=80, y=120)

# Upcoming Events Photo
upcoming = resize_image((95, 95), "icons/UpcomingEvents.png")
upcoming_button = ctk.CTkButton(app, text="", image=upcoming, fg_color="#EBE6E6")
upcoming_button.place(x=150, y=200)

# Upcoming Events Label
events_label = ctk.CTkLabel(frame1, text="Upcoming Events", text_color="#000000", font=('inter', 24))
events_label.place(x=50, y=180)

# Frame2
frame2 = ctk.CTkFrame(app, width=284, height=244, fg_color="#D9D9D9", corner_radius=10)
frame2.place(x=400, y=120)

# Contact Manager Photo
contact = resize_image((95, 95), "icons/Contact Admin.png")
contact_button = ctk.CTkButton(app, text="", image=contact, fg_color="#EBE6E6")
contact_button.place(x=475, y=200)

# Contact Manager Label
manager_label = ctk.CTkLabel(frame2, text="Contact Manager", text_color="#000000", font=('inter', 24))
manager_label.place(x=50, y=180)

app.mainloop()
