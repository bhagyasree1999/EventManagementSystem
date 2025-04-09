import customtkinter as ctk
import tkinter as tk

root = ctk.CTk()
root.title("SignUp Screen")
root.geometry("911x651")
root.resizable(False,False)

#Right login_frame
right_login_frame = ctk.CTkFrame(root,fg_color = "#FFFBFB",width =455,height =651, corner_radius= 0)
right_login_frame.pack_propagate(False)
right_login_frame.place(x = 455,y =0)

#Left login_frame
left_login_frame = ctk.CTkFrame(root,fg_color = "#7F5B6A",width =455,height =651, corner_radius= 0)
left_login_frame.pack_propagate(False)
left_login_frame.place(x = 0,y =0)

#Inside left frame
inner_left_frame = ctk.CTkFrame(left_login_frame,fg_color = "#FFFBFB",width =350,height =551, corner_radius= 0)
inner_left_frame.pack_propagate(False)
inner_left_frame.place(x = 50,y =50)

#Title
title = ctk.CTkLabel(inner_left_frame,text = "Sign Up", text_color = '#000000',font = ('Arya',30,'bold'))
title.place(x = 110, y = 40)

#firstname text label
firstname_label = ctk.CTkLabel(inner_left_frame,text = "First Name",text_color = "#3F5861",font = ('inter',15,'bold'))
firstname_label.place(x = 50, y = 100)

#firstname_entry_widget
firstname_entry = ctk.CTkEntry(inner_left_frame,text_color = "#D1D1D1",font = ('inter',12),width = 220, height = 35,border_width = 1,fg_color = "#FEFEFE")
firstname_entry.place(x = 50,y = 130)

#lastname text label
lastname_label = ctk.CTkLabel(inner_left_frame,text = "Last Name",text_color = "#3F5861",font = ('inter',15,'bold'))
lastname_label.place(x = 50, y = 180)

#lastname_entry_widget
lastname_entry = ctk.CTkEntry(inner_left_frame,text_color = "#D1D1D1",font = ('inter',12),width = 220, height = 35,border_width = 1,fg_color = "#FEFEFE")
lastname_entry.place(x = 50,y = 210)

#email text label
email_label = ctk.CTkLabel(inner_left_frame,text = "Email",text_color = "#3F5861",font = ('inter',15,'bold'))
email_label.place(x = 50, y = 260)

#email_entry_widget
email_entry = ctk.CTkEntry(inner_left_frame,text_color = "#D1D1D1",font = ('inter',12),width = 220, height = 35,border_width = 1,fg_color = "#FEFEFE")
email_entry.place(x = 50,y = 290)

#password text label
password_label = ctk.CTkLabel(inner_left_frame,text = "Password",text_color = "#3F5861",font = ('inter',15,'bold'))
password_label.place(x = 50, y = 340)

#email_entry_widget
password_entry = ctk.CTkEntry(inner_left_frame,text_color = "#D1D1D1",font = ('inter',12),width = 220, height = 35,border_width = 1,fg_color = "#FEFEFE")
password_entry.place(x = 50,y = 370)

#SignUp_button
SignUp_button = ctk.CTkButton(inner_left_frame,text = "SignUp",text_color = "#FFFFFF",width = 90,height = 35,fg_color = "#7F5B6A",hover_color = "grey",font = ('inter',14))
SignUp_button.place(x = 120, y = 440)

#Text under SignUp button
register_label = ctk.CTkLabel(inner_left_frame,text = "Already have an account? click here to log in"
,text_color = '#1E1E1E',font = ('Inter',10)).place(x = 80, y = 475)

#Right_frame_text
register_label = ctk.CTkLabel(right_login_frame,text = "NEW HERE?"
,text_color = '#000000',font = ('Inknut Antiqua',30,'bold')).place(x = 130, y =180)

#Right_frame_text_2
register_label = ctk.CTkLabel(right_login_frame,text = "SIGN UP AND"
,text_color = '#000000',font = ('Inknut Antiqua',30)).place(x = 120, y = 230)

#Right_frame_text_3
register_label = ctk.CTkLabel(right_login_frame,text = "DISCOVER HOW"
,text_color = '#000000',font = ('Inknut Antiqua',30)).place(x = 100, y = 280)

#Right_frame_text_4
register_label = ctk.CTkLabel(right_login_frame,text =  "WE CAN HELP YOU"
,text_color = '#000000',font = ('Inknut Antiqua',30)).place(x = 80, y = 330)


root.mainloop()

