import customtkinter as ctk
import tkinter as tk
from customtkinter import CTkImage
from PIL import ImageTk, Image

app = ctk.CTk(fg_color = "#D9D9D9")
app.title("Event Ease Login Page")
app.geometry("1111x851")
app.resizable(False,False)

# Login Image using CTkImage
def resize_image(size, image_url):
    """ Function to resize an image and return CTkImage """
    original_image = Image.open(image_url)
    resized_ctk_image = CTkImage(light_image=original_image, size=size)
    return resized_ctk_image

login_logo = resize_image((268,163), "images/loginlogo.png")
logo_label = ctk.CTkLabel(app, text="", image=login_logo, fg_color="#EBE6E6")
logo_label.place(x=450, y=57)

#Login Image
login_logo = resize_image((268,163),"images/loginlogo.png")
logo_label = ctk.CTkLabel(app,text = "",image = login_logo,fg_color = "#EBE6E6")
logo_label.place(x = 450, y = 57)


#Text Below Login Logo
register_label = ctk.CTkLabel(app,text = "WELCOME"
,text_color = '#000000',font = ('Cinzel',64,'bold')).place(x = 381, y = 225)

#Center Frame
center_frame=ctk.CTkFrame(app, width=951, height=490, fg_color="#FFFFFF",corner_radius=10)
center_frame.place(x=80, y=311)

#email text label
email_label = ctk.CTkLabel(center_frame,text = "Email",text_color = "#3F5861",font = ('inter',15,'bold'))
email_label.place(x = 298, y = 35)

#email_entry_widget
email_entry = ctk.CTkEntry(center_frame,text_color = "#D1D1D1",font = ('inter',12),width = 351, height = 47,border_width = 1,fg_color = "#FEFEFE")
email_entry.place(x = 302,y = 69)

#password text label
password_label = ctk.CTkLabel(center_frame,text = "Password",text_color = "#3F5861",font = ('inter',15,'bold'))
password_label.place(x = 298, y = 146)

#password_entry_widget
password_entry = ctk.CTkEntry(center_frame,text_color = "#D1D1D1",font = ('inter',12),width = 351, height = 47,border_width = 1,fg_color = "#FEFEFE")
password_entry.place(x = 302,y = 180)

#Role text label
role_label = ctk.CTkLabel(center_frame,text = "Role",text_color = "#3F5861",font = ('inter',15,'bold'))
role_label.place(x = 298, y = 257)

#DropBox for Role
drop_menu=ctk.CTkOptionMenu(center_frame,values=["Admin","Customer","Staff"],fg_color="#6B5720",width=351,height=47)
drop_menu.set("Select a Role")
drop_menu.place(x=302,y=291)

#login_button
login_button = ctk.CTkButton(center_frame,text = "Login",text_color = "#FFFFFF",width = 146,height = 45,fg_color = "#6B5720",hover_color = "#F6CA51",font = ('inter',14))
login_button.place(x = 411, y = 381)

#Text under Login button
register_label = ctk.CTkLabel(center_frame,text = "Don’t have an account? Sign Up"
,text_color = '#1E1E1E',font = ('Inter',16)).place(x = 363, y = 436)


app.mainloop()