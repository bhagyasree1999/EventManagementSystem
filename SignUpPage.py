import customtkinter as ctk
import tkinter as tk
from PIL import Image
import subprocess
import mysql.connector
from tkinter import messagebox
import re

# MySQL connection function
def get_connection():
    return mysql.connector.connect(
        host="141.209.241.57",
        user="tiruv1h",
        password="mypass",
        database="BIS698W1830_GRP1"
    )

# Email validation
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Password validation
def is_valid_password(password):
    pattern = (
        r'^(?=.*[a-z])'
        r'(?=.*[A-Z])'
        r'(?=.*\d)'
        r'(?=.*[@$!%*?&])'
        r'[A-Za-z\d@$!%*?&]{8,}$'
    )
    return re.match(pattern, password) is not None

# App setup
root = ctk.CTk()
root.title("SignUp Screen")
root.geometry("1111x851")
root.resizable(False, False)

def open_trial():
    subprocess.Popen(["python", "LoginPage.py"])
    root.destroy()

# Layout dimensions
frame_width = 555
frame_height = 851
inner_frame_width = 400
inner_frame_height = 650
field_width = 250
center_x = (inner_frame_width - field_width) // 2
button_width = 110

# Left Frame
left_login_frame = ctk.CTkFrame(root, fg_color="#7F5B6A", width=frame_width, height=frame_height, corner_radius=0)
left_login_frame.place(x=0, y=0)

# Right Frame
right_login_frame = ctk.CTkFrame(root, fg_color="#FFFBFB", width=frame_width, height=frame_height, corner_radius=0)
right_login_frame.place(x=frame_width, y=0)

# Inner Left Frame
inner_left_frame = ctk.CTkFrame(left_login_frame, fg_color="#FFFBFB", width=inner_frame_width, height=inner_frame_height, corner_radius=20)
inner_left_frame.place(x=(frame_width - inner_frame_width) // 2, y=(frame_height - inner_frame_height) // 2)

# Title
ctk.CTkLabel(inner_left_frame, text="Sign Up", text_color='#000000', font=('Arya', 32, 'bold')).place(x=(inner_frame_width - 150)//2, y=40)

# First Name
ctk.CTkLabel(inner_left_frame, text="First Name", text_color="#3F5861", font=('inter', 15, 'bold')).place(x=center_x, y=90)
first_name_entry = ctk.CTkEntry(inner_left_frame, text_color="#000000", font=('inter', 12), width=field_width, height=35, fg_color="#FEFEFE")
first_name_entry.place(x=center_x, y=120)

# Last Name
ctk.CTkLabel(inner_left_frame, text="Last Name", text_color="#3F5861", font=('inter', 15, 'bold')).place(x=center_x, y=170)
last_name_entry = ctk.CTkEntry(inner_left_frame, text_color="#000000", font=('inter', 12), width=field_width, height=35, fg_color="#FEFEFE")
last_name_entry.place(x=center_x, y=200)

# Email
ctk.CTkLabel(inner_left_frame, text="Email", text_color="#3F5861", font=('inter', 15, 'bold')).place(x=center_x, y=250)
email_entry = ctk.CTkEntry(inner_left_frame, text_color="#000000", font=('inter', 12), width=field_width, height=35, fg_color="#FEFEFE")
email_entry.place(x=center_x, y=280)

# Password
ctk.CTkLabel(inner_left_frame, text="Password", text_color="#3F5861", font=('inter', 15, 'bold')).place(x=center_x, y=330)
password_entry = ctk.CTkEntry(inner_left_frame, text_color="#000000", font=('inter', 12), width=field_width, height=35, fg_color="#FEFEFE", show="*")
password_entry.place(x=center_x, y=360)

# Confirm Password
ctk.CTkLabel(inner_left_frame, text="Confirm Password", text_color="#3F5861", font=('inter', 15, 'bold')).place(x=center_x, y=410)
confirm_password_entry = ctk.CTkEntry(inner_left_frame, text_color="#000000", font=('inter', 12), width=field_width, height=35, fg_color="#FEFEFE", show="*")
confirm_password_entry.place(x=center_x, y=440)

# Password Visibility Toggle
def password_visibility():
    show = "" if show_password.get() else "*"
    password_entry.configure(show=show)
    confirm_password_entry.configure(show=show)

show_password = ctk.BooleanVar()
ctk.CTkCheckBox(inner_left_frame, text="Show Password", variable=show_password,
                command=password_visibility, font=('inter', 12),
                text_color="#3F5861", checkbox_width=18, checkbox_height=18).place(x=center_x + 100, y=480)

# Signup Function
def signup():
    first_name = first_name_entry.get().strip()
    last_name = last_name_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()
    confirm_password = confirm_password_entry.get().strip()
    role = "customer"  # Fixed

    if not all([first_name, last_name, email, password, confirm_password]):
        messagebox.showerror("Error", "All fields are required. Please fill them in.")
        return

    if not is_valid_email(email):
        messagebox.showerror("Invalid Email", "Please enter a valid email address.")
        return

    if not is_valid_password(password):
        messagebox.showerror(
            "Invalid Password",
            "Password must be at least 8 characters long and include:\n"
            "- One uppercase letter\n"
            "- One lowercase letter\n"
            "- One number\n"
            "- One special character (e.g., @, #, $, !)"
        )
        return

    if password != confirm_password:
        messagebox.showerror("Password Mismatch", "Passwords do not match. Please re-enter them.")
        return

    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO details (first_name, last_name, email, password, role)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (first_name, last_name, email, password, role))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Customer signed up successfully!")
        open_trial()

    except mysql.connector.IntegrityError:
        messagebox.showerror("Signup Error", "Email already exists. Try logging in.")
    except Exception as e:
        messagebox.showerror("Database Error", str(e))

# Signup Button
ctk.CTkButton(inner_left_frame, text="SignUp", text_color="#FFFFFF", width=button_width, height=35,
              fg_color="#7F5B6A", hover_color="grey", font=('inter', 14), command=signup).place(x=(inner_frame_width - button_width)//2, y=530)

# Login Redirect
login_redirect = ctk.CTkLabel(inner_left_frame, text="Already have an account? Click here to log in",
                              text_color='#1E1E1E', font=('Inter', 14), cursor="hand2",
                              width=inner_frame_width, anchor="center", justify="center")
login_redirect.place(x=0, y=580)
login_redirect.bind("<Button-1>", lambda e: open_trial())

# Image on Right Side
image_path = "images/signup.png"
image = Image.open(image_path).resize((450, 450))
ctk_image = ctk.CTkImage(light_image=image, dark_image=image, size=(450, 450))

image_label = ctk.CTkLabel(right_login_frame, image=ctk_image, text="")
image_label.place(x=(frame_width - 450)//2, y=(frame_height - 450)//2)

# Home Button
home_icon = Image.open("icons/home.png").resize((35, 35))
home_ctk_image = ctk.CTkImage(light_image=home_icon, dark_image=home_icon, size=(35, 35))

def go_home():
    subprocess.Popen(["python", "HomePage.py"])
    root.destroy()

home_btn = ctk.CTkButton(root, text="", image=home_ctk_image, width=35, height=35,
                         fg_color="#7F5B6A", hover_color="grey",
                         command=go_home)
home_btn.place(x=15, y=15)

root.mainloop()