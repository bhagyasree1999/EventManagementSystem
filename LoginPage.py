import customtkinter as ctk
import tkinter as tk
from customtkinter import CTkImage
from PIL import ImageTk, Image
import subprocess  # 👈 Add this line

app = ctk.CTk(fg_color="#D9D9D9")
app.title("Event Ease Login Page")
app.geometry("1111x851")
app.resizable(False, False)

# CTkImage loader
def resize_image(size, image_url):
    original_image = Image.open(image_url)
    return CTkImage(light_image=original_image, size=size)

# Login logo
login_logo = resize_image((268, 163), "images/loginlogo.jpg")
logo_label = ctk.CTkLabel(app, text="", image=login_logo, fg_color="#EBE6E6")
logo_label.place(x=400, y=57)

# WELCOME text
ctk.CTkLabel(app, text="WELCOME", text_color='#000000', font=('Cinzel', 64, 'bold')).place(x=381, y=225)

# Center Frame
center_frame = ctk.CTkFrame(app, width=951, height=490, fg_color="#FFFFFF", corner_radius=10)
center_frame.place(x=80, y=311)

# Email
ctk.CTkLabel(center_frame, text="Email", text_color="#3F5861", font=('inter', 15, 'bold')).place(x=298, y=35)
email_entry = ctk.CTkEntry(center_frame, text_color="#D1D1D1", font=('inter', 12), width=351, height=47, border_width=1, fg_color="#FEFEFE")
email_entry.place(x=302, y=69)

# Password
ctk.CTkLabel(center_frame, text="Password", text_color="#3F5861", font=('inter', 15, 'bold')).place(x=298, y=146)
password_entry = ctk.CTkEntry(center_frame, text_color="#D1D1D1", font=('inter', 12), width=351, height=47, border_width=1, fg_color="#FEFEFE")
password_entry.place(x=302, y=180)

# Role
ctk.CTkLabel(center_frame, text="Role", text_color="#3F5861", font=('inter', 15, 'bold')).place(x=298, y=257)
drop_menu = ctk.CTkOptionMenu(center_frame, values=["Admin", "Customer", "Staff"], fg_color="grey", width=351, height=47)
drop_menu.set("Select a Role")
drop_menu.place(x=302, y=291)

# Login button
ctk.CTkButton(center_frame, text="Login", text_color="#FFFFFF", width=146, height=45,
              fg_color="#7F5B6A", hover_color="grey", font=('inter', 14)).place(x=411, y=381)

# Open signup window
def open_signup():
    subprocess.Popen(["python", "SignUpPage.py"])
    app.destroy()

# Sign Up text
signup_label = ctk.CTkLabel(center_frame, text="Don’t have an account? Sign Up",
                            text_color="#1E1E1E", font=('Inter', 16), cursor="hand2")
signup_label.place(x=363, y=436)
signup_label.bind("<Button-1>", lambda e: open_signup())

app.mainloop()
