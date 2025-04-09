import customtkinter as ctk
from PIL import Image
from customtkinter import CTkImage
import subprocess

app = ctk.CTk(fg_color="#D9D9D9")
app.title("Event Ease Login Page")
app.geometry("1111x851")
app.resizable(False, False)

# Function to open signup page
def open_signup():
    subprocess.Popen(["python", "SignUpPage.py"])
    app.destroy()

# Image loader
def resize_image(size, image_url):
    original_image = Image.open(image_url)
    return CTkImage(light_image=original_image, size=size)

login_logo = resize_image((268, 163), "images/loginlogo.jpg")
ctk.CTkLabel(app, text="", image=login_logo, fg_color="#EBE6E6").place(x=400, y=57)

# Welcome text
ctk.CTkLabel(app, text="WELCOME", text_color='#000000', font=('Cinzel', 64, 'bold')).place(x=381, y=225)

# Center frame
center_frame = ctk.CTkFrame(app, width=951, height=490, fg_color="#FFFFFF", corner_radius=10)
center_frame.place(x=80, y=311)

field_x = 302
field_width = 351

# Email
ctk.CTkLabel(center_frame, text="Email", text_color="#3F5861", font=('inter', 15, 'bold')).place(x=field_x - 4, y=35)
ctk.CTkEntry(center_frame, text_color="#D1D1D1", font=('inter', 12),
             width=field_width, height=47, border_width=1, fg_color="#FEFEFE").place(x=field_x, y=69)

# Password
ctk.CTkLabel(center_frame, text="Password", text_color="#3F5861", font=('inter', 15, 'bold')).place(x=field_x - 4, y=146)
ctk.CTkEntry(center_frame, text_color="#D1D1D1", font=('inter', 12),
             width=field_width, height=47, border_width=1, fg_color="#FEFEFE").place(x=field_x, y=180)

# Role label
ctk.CTkLabel(center_frame, text="Role", text_color="#3F5861", font=('inter', 15, 'bold')).place(x=field_x - 4, y=257)

# Variable for role
selected_role = ctk.StringVar(value="Select a Role")

# Function to update button text with arrow right aligned
def update_role_text(*args):
    role_text = selected_role.get()
    space_padding = 86  # add spaces to push arrow to the right
    role_btn.configure(text=f"{role_text}{' ' * space_padding}▼")

selected_role.trace_add("write", update_role_text)

# Custom dropdown popup
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

# Create role button (manual right-arrow)
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

# Login button
ctk.CTkButton(center_frame, text="Login", text_color="#FFFFFF", width=146, height=45,
              fg_color="#7F5B6A", hover_color="grey", font=('inter', 14)).place(x=(951 - 146) // 2, y=381)

# Sign up text
signup_label = ctk.CTkLabel(center_frame, text="Don’t have an account? Sign Up",
                            text_color="#1E1E1E", font=('Inter', 16), cursor="hand2",
                            width=951, anchor="center", justify="center")
signup_label.place(x=0, y=436)
signup_label.bind("<Button-1>", lambda e: open_signup())

app.mainloop()
