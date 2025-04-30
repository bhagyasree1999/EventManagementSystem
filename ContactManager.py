import customtkinter as ctk
import mysql.connector
from PIL import Image
import subprocess

# App setup
app = ctk.CTk(fg_color="#7F5B6A")
app.title("Contact Manager")
app.geometry("850x650")
app.resizable(False, False)

def resize_image(size, image_url):
    image = Image.open(image_url)
    return ctk.CTkImage(light_image=image, size=size)

def go_home():
    subprocess.Popen(["python", "HomePage.py"])
    app.destroy()

def go_backk():
    subprocess.Popen(["python", "StaffDashboard.py"])
    app.destroy()



# Top Frame
top_frame = ctk.CTkFrame(app, width=1111, height=81, fg_color="#D9D9D9", corner_radius=0)
top_frame.place(x=0, y=0)

tooltip_label = ctk.CTkLabel(app, text="Logout", text_color="#000000", fg_color="#FFFFFF",
                             font=("Segoe UI", 10), corner_radius=4, width=60, height=20)
tooltip_label.place_forget()

# Dashboard text label
dash_label = ctk.CTkLabel(top_frame, text="CONTACT MANAGER", text_color="#000000", font=('inter', 40))
dash_label.place(x=65, y=17)

#Frame1
frame1 = ctk.CTkFrame(app, width=700, height=400, fg_color="#D9D9D9", corner_radius=10)
frame1.place(x=55, y=153)

# Emma Photo
Emma = resize_image((95, 95), "images/Emma.jpg")
Emma = ctk.CTkLabel(app, text="", image=Emma, fg_color="#EBE6E6")
Emma.place(x=150, y=200)

# Emma Clark
ctk.CTkLabel(frame1, text="Emma Clark", text_color="#000000", font=('inter', 20, 'bold')).place(x=250, y=65)
# Emma mail
ctk.CTkLabel(frame1, text="emma@gmail.com", text_color="#000000", font=('inter', 20, 'bold')).place(x=250, y=100)

#Email photo
Emma = resize_image((50, 50), "images/Email.jpg")
Emma = ctk.CTkLabel(app, text="", image=Emma, fg_color="#D9D9D9")
Emma.place(x=600, y=220)



# David Photo
David = resize_image((95, 95), "images/David.jpg")
David = ctk.CTkLabel(app, text="", image=David, fg_color="#EBE6E6")
David.place(x=150, y=400)

# David smith
ctk.CTkLabel(frame1, text="David Smith", text_color="#000000", font=('inter', 20, 'bold')).place(x=250, y=260)
# Emma mail
ctk.CTkLabel(frame1, text="david@gmail.com", text_color="#000000", font=('inter', 20, 'bold')).place(x=250, y=295)
#Email photo
Emma = resize_image((50, 50), "images/Email.jpg")
Emma = ctk.CTkLabel(app, text="", image=Emma, fg_color="#D9D9D9")
Emma.place(x=600, y=420)



def show_tooltip(event): tooltip_label.place(x=1010, y=65)
def hide_tooltip(event): tooltip_label.place_forget()

door_icon = resize_image((55, 55), "icons/door.png")
door_label = ctk.CTkLabel(top_frame, text="", image=door_icon, fg_color="#D9D9D9", cursor="hand2")
door_label.place(x=750, y=5)
door_label.bind("<Enter>", show_tooltip)
door_label.bind("<Leave>", hide_tooltip)
door_label.bind("<Button-1>", lambda e: go_home())

# Back Icon
back_icon = resize_image((40, 40), "icons/backarrow.png")
back_label = ctk.CTkLabel(top_frame, text="", image=back_icon, fg_color="#D9D9D9", cursor="hand2")
back_label.place(x=20, y=20)
back_label.bind("<Button-1>", lambda e: go_backk())

app.mainloop()
