import customtkinter as ctk
import tkinter as tk
from PIL import Image
from customtkinter import CTkImage
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

# App Setup
app = ctk.CTk(fg_color="#D9D9D9")
app.title("Event Ease Login Page")
app.geometry("1111x851")
app.resizable(False, False)

# Open signup page
def open_signup():
    subprocess.Popen(["python", "SignUpPage.py"])
    app.destroy()

# Resize image
def resize_image(size, image_url):
    original_image = Image.open(image_url)
    return CTkImage(light_image=original_image, size=size)

# Top logo
login_logo = resize_image((268, 163), "images/loginlogo.jpg")
ctk.CTkLabel(app, text="", image=login_logo, fg_color="#EBE6E6").place(x=400, y=57)

# Welcome Text
ctk.CTkLabel(app, text="WELCOME", text_color='#000000', font=('Cinzel', 64, 'bold')).place(x=381, y=225)

# Center Frame
center_frame = ctk.CTkFrame(app, width=951, height=490, fg_color="#FFFFFF", corner_radius=10)
center_frame.place(x=80, y=311)

field_x = 302
field_width = 351

# Email Entry
ctk.CTkLabel(center_frame, text="Email", text_color="#3F5861", font=('inter', 15, 'bold')).place(x=field_x - 4, y=35)
email_entry = ctk.CTkEntry(center_frame, text_color="#000000", font=('inter', 12),
                           width=field_width, height=47, fg_color="#FEFEFE")
email_entry.place(x=field_x, y=69)

# Password Entry
ctk.CTkLabel(center_frame, text="Password", text_color="#3F5861", font=('inter', 15, 'bold')).place(x=field_x - 4, y=146)
password_entry = ctk.CTkEntry(center_frame, text_color="#000000", font=('inter', 12),
                              width=field_width, height=47, fg_color="#FEFEFE", show="*")
password_entry.place(x=field_x, y=180)

# Show Password Checkbox BELOW the Password Entry on the right side
show_password_var = tk.BooleanVar(value=False)

def toggle_password():
    password_entry.configure(show="" if show_password_var.get() else "*")

# Place it just below the password field, aligned right
show_password_checkbox = ctk.CTkCheckBox(center_frame,
                                         text="Show Password",
                                         font=('inter', 12),
                                         variable=show_password_var,
                                         command=toggle_password)
show_password_checkbox.place(x=field_x + field_width - 128, y=235)

# Role Label
ctk.CTkLabel(center_frame, text="Role", text_color="#3F5861", font=('inter', 15, 'bold')).place(x=field_x - 4, y=270)

# Role Dropdown
selected_role = ctk.StringVar(value="Select a Role")

def update_role_text(*args):
    role_text = selected_role.get()
    space_padding = 86
    role_btn.configure(text=f"{role_text}{' ' * space_padding}▼")

selected_role.trace_add("write", update_role_text)

def toggle_dropdown():
    if hasattr(app, 'dropdown_window') and app.dropdown_window.winfo_exists():
        app.dropdown_window.destroy()
    else:
        app.dropdown_window = ctk.CTkToplevel(app)
        app.dropdown_window.geometry(f"{field_width}x135+{app.winfo_x() + field_x + 80}+{app.winfo_y() + 620}")
        app.dropdown_window.overrideredirect(True)
        app.dropdown_window.attributes('-topmost', True)

        def select(role):
            selected_role.set(role)
            app.dropdown_window.destroy()

        for role in ["ADMIN", "CUSTOMER", "STAFF"]:
            ctk.CTkButton(app.dropdown_window, text=role, width=field_width,
                          height=45, font=('inter', 13),
                          fg_color="#F3F3F3", text_color="#000000",
                          hover_color="#D6D6D6",
                          command=lambda r=role: select(r)).pack()

role_btn = ctk.CTkButton(center_frame,
                         text="Select a Role" + " " * 75 + "▼",
                         text_color="#FFFFFF",
                         fg_color="#7F5B6A",
                         hover_color="#915E77",
                         font=("inter", 13),
                         width=field_width,
                         height=47,
                         command=toggle_dropdown,
                         anchor="w",
                         corner_radius=6)
role_btn.place(x=field_x, y=305)

# Login Function with First Name Greeting
def login():
    email = email_entry.get().strip()
    password = password_entry.get().strip()
    role = selected_role.get().strip().lower()

    if role not in ["admin", "customer", "staff"]:
        messagebox.showerror("Error", "Please select a valid role.")
        return

    if not all([email, password]):
        messagebox.showerror("Error", "Please enter both email and password.")
        return

    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM customer WHERE email=%s AND password=%s AND role=%s"
        cursor.execute(query, (email, password, role))
        result = cursor.fetchone()
        conn.close()

        if result:
            first_name = result[1]  # assuming 2nd column is first_name
            messagebox.showinfo("Success", f"Welcome, {first_name}!")

            # Role-based dashboard launching
            if role == "admin":
                subprocess.Popen(["python", "AdminDashboard.py"])
            elif role == "customer":
                subprocess.Popen(["python", "CustomerDashboard.py"])
            elif role == "staff":
                subprocess.Popen(["python", "StaffDashboard.py"])

            app.destroy()
        else:
            messagebox.showerror("Login Failed", "Incorrect email, password, or role.")

    except Exception as e:
        messagebox.showerror("Database Error", str(e))

# Login Button
ctk.CTkButton(center_frame, text="Login", text_color="#FFFFFF", width=146, height=45,
              fg_color="#7F5B6A", hover_color="grey", font=('inter', 14),
              command=login).place(x=(951 - 146) // 2, y=395)

# Signup Link
signup_label = ctk.CTkLabel(center_frame, text="Don’t have an account? Sign Up",
                            text_color="#1E1E1E", font=('Inter', 16), cursor="hand2",
                            width=951, anchor="center", justify="center")
signup_label.place(x=0, y=446)
signup_label.bind("<Button-1>", lambda e: open_signup())

# Start App
app.mainloop()
