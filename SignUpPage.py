import customtkinter as ctk
import tkinter as tk
from PIL import Image
import subprocess

root = ctk.CTk()
root.title("SignUp Screen")
root.geometry("1111x851")
root.resizable(False, False)

# Function to redirect to login page
def open_login():
    subprocess.Popen(["python", "LoginPage.py"])
    root.destroy()

# Dimensions
frame_width = 555 
frame_height = 851
inner_frame_width = 400
inner_frame_height = 650
field_width = 250
center_x = (inner_frame_width - field_width) // 2
button_width = 110

# Left login_frame
left_login_frame = ctk.CTkFrame(root, fg_color="#7F5B6A", width=frame_width, height=frame_height, corner_radius=0)
left_login_frame.pack_propagate(False)
left_login_frame.place(x=0, y=0)

# Right login_frame
right_login_frame = ctk.CTkFrame(root, fg_color="#FFFBFB", width=frame_width, height=frame_height, corner_radius=0)
right_login_frame.pack_propagate(False)
right_login_frame.place(x=frame_width, y=0)

# Inner left frame (centered)
inner_left_frame = ctk.CTkFrame(left_login_frame, fg_color="#FFFBFB", width=inner_frame_width, height=inner_frame_height, corner_radius=20)
inner_left_frame.pack_propagate(False)
inner_left_frame.place(x=(frame_width - inner_frame_width) // 2, y=(frame_height - inner_frame_height) // 2)

# Title
ctk.CTkLabel(inner_left_frame, text="Sign Up", text_color='#000000', font=('Arya', 32, 'bold')).place(x=(inner_frame_width - 150)//2, y=40)

# First Name
ctk.CTkLabel(inner_left_frame, text="First Name", text_color="#3F5861", font=('inter', 15, 'bold')).place(x=center_x, y=110)
ctk.CTkEntry(inner_left_frame, text_color="#000000", font=('inter', 12), width=field_width, height=35, border_width=1, fg_color="#FEFEFE").place(x=center_x, y=140)

# Last Name
ctk.CTkLabel(inner_left_frame, text="Last Name", text_color="#3F5861", font=('inter', 15, 'bold')).place(x=center_x, y=190)
ctk.CTkEntry(inner_left_frame, text_color="#000000", font=('inter', 12), width=field_width, height=35, border_width=1, fg_color="#FEFEFE").place(x=center_x, y=220)

# Email
ctk.CTkLabel(inner_left_frame, text="Email", text_color="#3F5861", font=('inter', 15, 'bold')).place(x=center_x, y=270)
ctk.CTkEntry(inner_left_frame, text_color="#000000", font=('inter', 12), width=field_width, height=35, border_width=1, fg_color="#FEFEFE").place(x=center_x, y=300)

# Password
ctk.CTkLabel(inner_left_frame, text="Password", text_color="#3F5861", font=('inter', 15, 'bold')).place(x=center_x, y=350)
ctk.CTkEntry(inner_left_frame, text_color="#000000", font=('inter', 12), width=field_width, height=35, border_width=1, fg_color="#FEFEFE", show="*").place(x=center_x, y=380)

# Sign Up Button
ctk.CTkButton(inner_left_frame, text="SignUp", text_color="#FFFFFF", width=button_width, height=35,
              fg_color="#7F5B6A", hover_color="grey", font=('inter', 14)).place(x=(inner_frame_width - button_width)//2, y=440)

# Login Redirect
login_redirect = ctk.CTkLabel(inner_left_frame,
                              text="Already have an account? Click here to log in",
                              text_color='#1E1E1E',
                              font=('Inter', 14),
                              cursor="hand2",
                              width=inner_frame_width,
                              anchor="center",
                              justify="center")
login_redirect.place(x=0, y=490)
login_redirect.bind("<Button-1>", lambda e: open_login())

# Load and place the image on the right side
image_path = "images/signup.png"
image = Image.open(image_path)
resized_image = image.resize((450, 450))  # Resize for better fit
ctk_image = ctk.CTkImage(light_image=resized_image, dark_image=resized_image, size=(450, 450))

image_label = ctk.CTkLabel(right_login_frame, image=ctk_image, text="")
image_label.place(x=(frame_width - 450)//2, y=(frame_height - 450)//2)

root.mainloop()
