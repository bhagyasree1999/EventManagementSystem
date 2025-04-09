import customtkinter as ctk
import tkinter as tk
import subprocess  # 👈 Needed for launching login page

root = ctk.CTk()
root.title("SignUp Screen")
root.geometry("911x651")
root.resizable(False, False)

# Function to redirect to login page
def open_login():
    subprocess.Popen(["python", "LoginPage.py"])
    root.destroy()

# Right login_frame
right_login_frame = ctk.CTkFrame(root, fg_color="#FFFBFB", width=455, height=651, corner_radius=0)
right_login_frame.pack_propagate(False)
right_login_frame.place(x=455, y=0)

# Left login_frame
left_login_frame = ctk.CTkFrame(root, fg_color="#7F5B6A", width=455, height=651, corner_radius=0)
left_login_frame.pack_propagate(False)
left_login_frame.place(x=0, y=0)

# Inner left frame
inner_left_frame = ctk.CTkFrame(left_login_frame, fg_color="#FFFBFB", width=350, height=551, corner_radius=0)
inner_left_frame.pack_propagate(False)
inner_left_frame.place(x=50, y=50)

# Center alignment helper
field_width = 220
center_x = (350 - field_width) // 2  # = 65
button_width = 90

# Title
ctk.CTkLabel(inner_left_frame, text="Sign Up", text_color='#000000', font=('Arya', 30, 'bold')).place(x=(350 - 130)//2, y=40)

# First Name
ctk.CTkLabel(inner_left_frame, text="First Name", text_color="#3F5861", font=('inter', 15, 'bold')).place(x=center_x, y=100)
ctk.CTkEntry(inner_left_frame, text_color="#D1D1D1", font=('inter', 12), width=field_width, height=35, border_width=1, fg_color="#FEFEFE").place(x=center_x, y=130)

# Last Name
ctk.CTkLabel(inner_left_frame, text="Last Name", text_color="#3F5861", font=('inter', 15, 'bold')).place(x=center_x, y=180)
ctk.CTkEntry(inner_left_frame, text_color="#D1D1D1", font=('inter', 12), width=field_width, height=35, border_width=1, fg_color="#FEFEFE").place(x=center_x, y=210)

# Email
ctk.CTkLabel(inner_left_frame, text="Email", text_color="#3F5861", font=('inter', 15, 'bold')).place(x=center_x, y=260)
ctk.CTkEntry(inner_left_frame, text_color="#D1D1D1", font=('inter', 12), width=field_width, height=35, border_width=1, fg_color="#FEFEFE").place(x=center_x, y=290)

# Password
ctk.CTkLabel(inner_left_frame, text="Password", text_color="#3F5861", font=('inter', 15, 'bold')).place(x=center_x, y=340)
ctk.CTkEntry(inner_left_frame, text_color="#D1D1D1", font=('inter', 12), width=field_width, height=35, border_width=1, fg_color="#FEFEFE").place(x=center_x, y=370)

# Sign Up Button
ctk.CTkButton(inner_left_frame, text="SignUp", text_color="#FFFFFF", width=button_width, height=35,
              fg_color="#7F5B6A", hover_color="grey", font=('inter', 14)).place(x=(350 - button_width)//2, y=440)

# 🔗 Centered clickable login label
login_redirect = ctk.CTkLabel(inner_left_frame,
                              text="Already have an account? Click here to log in",
                              text_color='#1E1E1E',
                              font=('Inter', 10),
                              cursor="hand2",
                              width=350,  # make sure it's wide enough
                              anchor="center",  # text alignment
                              justify="center")
login_redirect.place(x=0, y=480)
login_redirect.bind("<Button-1>", lambda e: open_login())

# Right side motivational text
ctk.CTkLabel(right_login_frame, text="NEW HERE?", text_color='#000000', font=('Inknut Antiqua', 30, 'bold')).place(x=130, y=180)
ctk.CTkLabel(right_login_frame, text="SIGN UP AND", text_color='#000000', font=('Inknut Antiqua', 30)).place(x=120, y=230)
ctk.CTkLabel(right_login_frame, text="DISCOVER HOW", text_color='#000000', font=('Inknut Antiqua', 30)).place(x=100, y=280)
ctk.CTkLabel(right_login_frame, text="WE CAN HELP YOU", text_color='#000000', font=('Inknut Antiqua', 30)).place(x=80, y=330)

root.mainloop()
