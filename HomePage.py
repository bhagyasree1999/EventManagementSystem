import customtkinter as ctk
from PIL import ImageTk, Image

# App Window
app = ctk.CTk()
app.title("Event Ease")
app.geometry("1111x840")

# Header with image logo
header_frame = ctk.CTkFrame(app, fg_color="#7F5B6A", height=120, corner_radius=0)
header_frame.pack(fill="x")

logo_image = ctk.CTkImage(light_image=Image.open("images/logo.jpg"), size=(275, 152))
logo_label = ctk.CTkLabel(header_frame, image=logo_image, text="")
logo_label.image = logo_image
logo_label.pack(pady=0, expand=True)

# Navigation bar with left and right sections
navbar = ctk.CTkFrame(app, fg_color="#FFF5EE", height=60, corner_radius=0)
navbar.pack(fill="x")

nav_left = ctk.CTkFrame(navbar, fg_color="transparent")
nav_right = ctk.CTkFrame(navbar, fg_color="transparent")
nav_left.pack(side="left", padx=40)
nav_right.pack(side="right", padx=40)

for label in ["HOME", "EVENT SERVICES"]:
    ctk.CTkButton(nav_left, text=label, fg_color="transparent", hover_color="#D6D6D6", text_color="black", font=("Inria Serif", 28), width=130, height=40).pack(side="left", padx=15)

for label in ["SIGN UP", "LOGIN"]:
    ctk.CTkButton(nav_right, text=label, fg_color="transparent", hover_color="#D6D6D6", text_color="black", font=("Inria Serif", 28), width=130, height=40).pack(side="left", padx=15)

# Image section
image_frame = ctk.CTkFrame(app, fg_color="#7F5B6A", height=336, corner_radius=0)
image_frame.pack(fill="x")

event_img = ctk.CTkImage(light_image=Image.open("images/event.png"), size=(1111, 336))
event_photo = event_img
img_label = ctk.CTkLabel(image_frame, image=event_photo, text="")
img_label.image = event_photo
img_label.pack(padx=0, pady=0)

# Welcome Section
welcome_frame = ctk.CTkFrame(app, fg_color="#7F5B6A", height=120, corner_radius=0)
welcome_frame.pack(fill="x")

ctk.CTkLabel(welcome_frame, text="WELCOME TO EVENT EASE", font=("Georgia", 24, "bold"), text_color="white").pack(pady=(20, 3))
ctk.CTkLabel(welcome_frame, text="THE EVENT MANAGEMENT COMPANY", font=("Georgia", 14), text_color="white").pack()

# Bottom Section with 3 columns
bottom_frame = ctk.CTkFrame(app, fg_color="#7F5B6A", height=200, corner_radius=0)
bottom_frame.pack(fill="x", pady=(0, 0))

mission = ctk.CTkFrame(bottom_frame, fg_color="#7F5B6A", width=370)
contact = ctk.CTkFrame(bottom_frame, fg_color="#7F5B6A", width=370)
share = ctk.CTkFrame(bottom_frame, fg_color="#7F5B6A", width=370)

mission.pack(side="left", expand=True, padx=20, pady=30)
contact.pack(side="left", expand=True, padx=20, pady=30)
share.pack(side="left", expand=True, padx=20, pady=30)

ctk.CTkLabel(mission, text="OUR MISSION", font=("Georgia", 13, "bold"), text_color="white").pack(pady=(0, 10))
ctk.CTkLabel(mission, text="Making your event\nsmooth, memorable &\nstress-free.", font=("Georgia", 13), text_color="white").pack()


ctk.CTkLabel(contact, text="CONTACT US", font=("Georgia", 13, "bold"), text_color="white").pack(pady=(30, 10))
# Contact Icons
phone_icon = ctk.CTkImage(light_image=Image.open("icons/phone-call.png"), size=(20, 20))
email_icon = ctk.CTkImage(light_image=Image.open("icons/email.png"), size=(20, 20))
location_icon = ctk.CTkImage(light_image=Image.open("icons/location.png"), size=(20, 20))

ctk.CTkLabel(contact, image=phone_icon, text=" +1 989-000-0000", compound="left", font=("Georgia", 13), text_color="white").pack(anchor="w")
ctk.CTkLabel(contact, image=email_icon, text=" eventease@gmail.com", compound="left", font=("Georgia", 13), text_color="white").pack(anchor="w")
ctk.CTkLabel(contact, image=location_icon, text=" Mount Pleasant", compound="left", font=("Georgia", 13), text_color="white").pack(anchor="w")


ctk.CTkLabel(share, text="SHARE US", font=("Georgia", 13, "bold"), text_color="white").pack(pady=(0, 10))

# Share Icons
instagram_icon = ctk.CTkImage(light_image=Image.open("icons/instagram.png"), size=(20, 20))
social_icon = ctk.CTkImage(light_image=Image.open("icons/social-media.png"), size=(20, 20))

ctk.CTkLabel(share, image=instagram_icon, text=" @EventEase", compound="left", font=("Georgia", 13), text_color="white").pack(anchor="w")
ctk.CTkLabel(share, image=social_icon, text=" EventEase", compound="left", font=("Georgia", 13), text_color="white").pack(anchor="w")
app.mainloop()
