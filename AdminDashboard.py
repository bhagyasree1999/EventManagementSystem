import customtkinter as ctk
from PIL import Image
import mysql.connector

# App setup
app = ctk.CTk(fg_color="#7F5B6A")
app.title("Staff Dashboard")
app.geometry("1111x750")
app.resizable(False, False)

# ✅ Correct Image Resize Function using CTkImage
def resize_image(size, image_url):
    """Returns a CTkImage resized to the given size"""
    image = Image.open(image_url)
    return ctk.CTkImage(light_image=image, size=size)

# Top Frame
top_frame = ctk.CTkFrame(app, width=1111, height=81, fg_color="#D9D9D9", corner_radius=10)
top_frame.place(x=0, y=0)

# Calendar Icon
calendar_icon = resize_image((64, 64), "icons/calendar.png")
calendar_label = ctk.CTkLabel(top_frame, text="", image=calendar_icon, fg_color="#D9D9D9")
calendar_label.place(x=900, y=15)

# Menu Icon
menu_icon = resize_image((64, 64), "icons/Menu.png")
menu_label = ctk.CTkLabel(top_frame, text="", image=menu_icon, fg_color="#D9D9D9")
menu_label.place(x=1000, y=15)

# Dashboard Title
dash_label = ctk.CTkLabel(top_frame, text="ADMIN DASHBOARD", text_color="#000000", font=('inter', 40))
dash_label.place(x=20, y=17)

# Frame 1: Create Events
frame1 = ctk.CTkFrame(app, width=284, height=244, fg_color="#D9D9D9", corner_radius=10)
frame1.place(x=80, y=120)

event_icon = resize_image((95, 95), "icons/Create Events.png")
event_btn = ctk.CTkButton(frame1, text="", image=event_icon, fg_color="#EBE6E6", width=95, height=95)
event_btn.place(x=95, y=30)

event_label = ctk.CTkLabel(frame1, text="Create Events", text_color="#000000", font=('inter', 24))
event_label.place(x=70, y=180)

# Frame 2: Current Events
frame2 = ctk.CTkFrame(app, width=284, height=244, fg_color="#D9D9D9", corner_radius=10)
frame2.place(x=400, y=120)

cevent_icon = resize_image((95, 95), "icons/Current Events.png")
cevent_btn = ctk.CTkButton(frame2, text="", image=cevent_icon, fg_color="#EBE6E6", width=95, height=95)
cevent_btn.place(x=95, y=30)

cevent_label = ctk.CTkLabel(frame2, text="Current Events", text_color="#000000", font=('inter', 24))
cevent_label.place(x=55, y=180)

# Frame 3: Staff Allocation
frame3 = ctk.CTkFrame(app, width=284, height=244, fg_color="#D9D9D9", corner_radius=10)
frame3.place(x=720, y=120)

staff_icon = resize_image((95, 95), "icons/Staff Allocation.png")
staff_btn = ctk.CTkButton(frame3, text="", image=staff_icon, fg_color="#EBE6E6", width=95, height=95)
staff_btn.place(x=95, y=30)

staff_label = ctk.CTkLabel(frame3, text="Staff Allocation", text_color="#000000", font=('inter', 24))
staff_label.place(x=55, y=180)

# Run app
app.mainloop()
