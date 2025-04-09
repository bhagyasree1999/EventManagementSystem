import customtkinter as ctk
import tkinter as tk
from PIL import Image
import subprocess
import mysql.connector
from tkinter import messagebox

# MySQL connection function
def get_connection():
    return mysql.connector.connect(
        host="141.209.241.57",
        user="tiruv1h",
        password="mypass",
        database="BIS698W1830_GRP1"
    )

# App setup
root = ctk.CTk()
root.title("SignUp Screen")
root.geometry("1111x851")
root.resizable(False, False)

def open_login():
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
ctk.CTkLabel(inner_left_frame, text="First Name", text_color="#3F5861", font=('inter', 15, 'bold')).place(x=center_x, y=110)
first_name_entry = ctk.CTkEntry(inner_left_frame, text_color="#000000", font=('inter', 12), width=field_width, height=35, fg_color="#FEFEFE")
first_name_entry.place(x=center_x, y=140)

# Last Name
ctk.CTkLabel(inner_left_frame, text="Last Name", text_color="#3F5861", font=('inter', 15, 'bold')).place(x=center_x, y=190)
last_name_entry = ctk.CTkEntry(inner_left_frame, text_color="#000000", font=('inter', 12), width=field_width, height=35, fg_color="#FEFEFE")
last_name_entry.place(x=center_x, y=220)

# Email
ctk.CTkLabel(inner_left_frame, text="Email", text_color="#3F5861", font=('inter', 15, 'bold')).place(x=center_x, y=270)
email_entry = ctk.CTkEntry(inner_left_frame, text_color="#000000", font=('inter', 12), width=field_width, height=35, fg_color="#FEFEFE")
email_entry.place(x=center_x, y=300)

# Password
ctk.CTkLabel(inner_left_frame, text="Password", text_color="#3F5861", font=('inter', 15, 'bold')).place(x=center_x, y=350)
password_entry = ctk.CTkEntry(inner_left_frame, text_color="#000000", font=('inter', 12), width=field_width, height=35, fg_color="#FEFEFE", show="*")
password_entry.place(x=center_x, y=380)

# --- Role Dropdown ---
ctk.CTkLabel(inner_left_frame, text="Role", text_color="#3F5861", font=('inter', 15, 'bold')).place(x=center_x, y=430)

selected_role = ctk.StringVar(value="Select a Role")

def update_role_text(*args):
    role_text = selected_role.get()
    space_padding = 43
    role_btn.configure(text=f"{role_text}{' ' * space_padding}▼")

selected_role.trace_add("write", update_role_text)

def toggle_dropdown():
    if hasattr(root, 'dropdown_window') and root.dropdown_window.winfo_exists():
        root.dropdown_window.destroy()
    else:
        root.dropdown_window = ctk.CTkToplevel(root)
        root.dropdown_window.geometry(f"{field_width}x135+{root.winfo_x() + center_x + 80}+{root.winfo_y() + 570}")
        root.dropdown_window.overrideredirect(True)
        root.dropdown_window.attributes('-topmost', True)

        def select(role):
            selected_role.set(role)
            root.dropdown_window.destroy()

        for role in ["ADMIN", "CUSTOMER", "STAFF"]:
            ctk.CTkButton(root.dropdown_window, text=role, width=field_width, height=45,
                          font=('inter', 13), fg_color="#F3F3F3", text_color="#000000",
                          hover_color="#D6D6D6", command=lambda r=role: select(r)).pack()

role_btn = ctk.CTkButton(inner_left_frame, text="Select a Role" + " " * 43 + "▼",
                         text_color="#FFFFFF", fg_color="#7F5B6A", hover_color="#915E77",
                         font=("inter", 13), width=field_width, height=43,
                         command=toggle_dropdown, anchor="w", corner_radius=6)
role_btn.place(x=center_x, y=460)

# --- Signup Function ---
def signup():
    first_name = first_name_entry.get().strip()
    last_name = last_name_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()
    role = selected_role.get().lower()

    if role not in ["admin", "customer", "staff"]:
        messagebox.showerror("Error", "Please select a valid role.")
        return

    if not all([first_name, last_name, email, password]):
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO customer (first_name, last_name, email, password, role)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (first_name, last_name, email, password, role))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", f"{role.title()} signed up successfully!")
        open_login()

    except mysql.connector.IntegrityError:
        messagebox.showerror("Signup Error", "Email already exists. Try logging in.")
    except Exception as e:
        messagebox.showerror("Database Error", str(e))

# Signup Button
ctk.CTkButton(inner_left_frame, text="SignUp", text_color="#FFFFFF", width=button_width, height=35,
              fg_color="#7F5B6A", hover_color="grey", font=('inter', 14), command=signup).place(x=(inner_frame_width - button_width)//2, y=510)

# Login Redirect
login_redirect = ctk.CTkLabel(inner_left_frame, text="Already have an account? Click here to log in",
                              text_color='#1E1E1E', font=('Inter', 14), cursor="hand2",
                              width=inner_frame_width, anchor="center", justify="center")
login_redirect.place(x=0, y=550)
login_redirect.bind("<Button-1>", lambda e: open_login())

# Image on Right Side
image_path = "images/signup.png"
image = Image.open(image_path).resize((450, 450))
ctk_image = ctk.CTkImage(light_image=image, dark_image=image, size=(450, 450))

image_label = ctk.CTkLabel(right_login_frame, image=ctk_image, text="")
image_label.place(x=(frame_width - 450)//2, y=(frame_height - 450)//2)

# Start app
root.mainloop()
