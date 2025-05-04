import customtkinter as ctk
from PIL import Image, ImageTk
from customtkinter import CTkImage
import subprocess
import mysql.connector
from tkinter import messagebox
import keyboard
import ctypes
from itertools import cycle
import threading

app = ctk.CTk(fg_color="#D9D9D9")
app.title("Event Ease Login Page")
app.geometry("1111x800")
app.resizable(False, False)

# Open pages
def open_signup():
    subprocess.Popen(["python", "SignUpPage.py"])
    app.destroy()

def open_customerdashboard():
    subprocess.Popen(["python", "CustomerDashboard.py"])
    app.destroy()

def open_admindashboard():
    subprocess.Popen(["python", "AdminDashboard.py"])
    app.destroy()

def open_staffdashboard():
    subprocess.Popen(["python", "StaffDashboard.py"])
    app.destroy()

# Resize image function
def resize_image(size, image_url):
    original_image = Image.open(image_url)
    return CTkImage(light_image=original_image, size=size)

# Logo and welcome
login_logo = resize_image((268, 163), "images/loginlogo.jpg")
ctk.CTkLabel(app, text="", image=login_logo, fg_color="#EBE6E6").place(x=400, y=57)
ctk.CTkLabel(app, text="WELCOME", text_color='#000000', font=('Cinzel', 64, 'bold')).place(x=381, y=225)

# Main Frame
center_frame = ctk.CTkFrame(app, width=951, height=490, fg_color="#FFFFFF", corner_radius=10)
center_frame.place(x=80, y=311)

field_x = 302
field_width = 351

# Email
ctk.CTkLabel(center_frame, text="Email", text_color="#3F5861", font=('inter', 15, 'bold')).place(x=field_x - 4, y=35)
email_entry = ctk.CTkEntry(center_frame, text_color="black", font=('inter', 12),
                           width=field_width, height=47, border_width=1, fg_color="#FEFEFE")
email_entry.place(x=field_x, y=69)

# Password
ctk.CTkLabel(center_frame, text="Password", text_color="#3F5861", font=('inter', 15, 'bold')).place(x=field_x - 4, y=146)
password_var = ctk.StringVar()
password_entry = ctk.CTkEntry(center_frame, text_color="black", font=('inter', 12),
                               width=field_width, height=47, border_width=1,
                               fg_color="#FEFEFE", show="*", textvariable=password_var)
password_entry.place(x=field_x, y=180)

# CapsLock warning
capslock_label = ctk.CTkLabel(center_frame, text="Caps Lock is ON", text_color="red", font=('inter', 12))
capslock_label.place(x=field_x, y=230)
capslock_label.place_forget()

monitoring = False

def monitor_capslock():
    if monitoring:
        capslock_on = bool(ctypes.WinDLL("User32.dll").GetKeyState(0x14))
        if capslock_on:
            capslock_label.place(x=field_x, y=230)
        else:
            capslock_label.place_forget()
        app.after(200, monitor_capslock)

def start_monitoring(event):
    global monitoring
    monitoring = True
    monitor_capslock()

def stop_monitoring(event):
    global monitoring
    monitoring = False
    capslock_label.place_forget()

password_entry.bind("<FocusIn>", start_monitoring)
password_entry.bind("<FocusOut>", stop_monitoring)

# Toggle Password
def toggle_password_visibility():
    if show_password.get():
        password_entry.configure(show="")
    else:
        password_entry.configure(show="*")

show_password = ctk.BooleanVar()
ctk.CTkCheckBox(center_frame, text="Show Password", variable=show_password,
                command=toggle_password_visibility, font=('inter', 12),
                text_color="#3F5861", checkbox_width=18, checkbox_height=18).place(x=field_x + 240, y=230)

# Role dropdown
ctk.CTkLabel(center_frame, text="Role", text_color="#3F5861", font=('inter', 15, 'bold')).place(x=field_x - 4, y=257)
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
            ctk.CTkButton(app.dropdown_window, text=role, width=field_width, height=45,
                          font=('inter', 13), fg_color="#F3F3F3", text_color="#000000",
                          hover_color="#D6D6D6", command=lambda r=role: select(r)).pack()

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
role_btn.place(x=field_x, y=291)

# GIF Loader
gif_label = ctk.CTkLabel(center_frame, text="")
gif_label.place(x=(951 - 100) // 2, y=330)
gif_label.place_forget()



# Login logic
def login():


    def threaded_login():
        email = email_entry.get()
        password = password_var.get()
        role = selected_role.get()

        if role == "Select a Role":
            gif_label.place_forget()
            messagebox.showerror("Login Failed", "Please select a role.")
            return

        try:
            conn = mysql.connector.connect(
                host="141.209.241.57",
                user="surak1m",
                password="mypass",
                database="BIS698W1830_GRP1"
            )
            cursor = conn.cursor()
            query = "SELECT * FROM details WHERE email=%s AND password=%s AND role=%s"
            cursor.execute(query, (email, password, role))
            result = cursor.fetchone()
            print("Login result:", result)

            if result:
                if role == "ADMIN":
                    app.after(100, open_admindashboard)
                elif role == "CUSTOMER":
                    with open("user_info.txt", "w") as f:
                        f.write(result[1])
                    with open("user_email.txt", "w") as f:
                        f.write(result[3])
                    app.after(100, open_customerdashboard)
                elif role == "STAFF":
                    app.after(100, open_staffdashboard)
            else:
                messagebox.showerror("Access Denied", "Invalid credentials or role.")

            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            gif_label.place_forget()
            messagebox.showerror("Database Error", f"Error: {err}")

    threading.Thread(target=threaded_login, daemon=True).start()

# Login button
ctk.CTkButton(center_frame, text="Login", text_color="#FFFFFF", width=146, height=45,
              fg_color="#7F5B6A", hover_color="grey", font=('inter', 14),
              command=login).place(x=(951 - 146) // 2, y=381)

# Sign up
signup_label = ctk.CTkLabel(center_frame, text="Don’t have an account? Sign Up",
                            text_color="#1E1E1E", font=('Inter', 16), cursor="hand2",
                            width=951, anchor="center", justify="center")
signup_label.place(x=0, y=436)
signup_label.bind("<Button-1>", lambda e: open_signup())

app.mainloop()
