import customtkinter as ctk
from PIL import Image

def logout(): pass
def add_event(): pass

app = ctk.CTk()
app.geometry("400x480")
app.title("Upcoming Events")
app.configure(fg_color="#7F5B6A")

# Top Header Frame
header_frame = ctk.CTkFrame(app, fg_color="#C9C0C0", height=50, corner_radius=0)
header_frame.pack(fill="x")

ctk.CTkButton(header_frame, text="➕", width=40, command=add_event, fg_color="transparent").place(x=5, y=10)
ctk.CTkLabel(header_frame, text="UPCOMING EVENTS", font=("Arial", 14, "bold"), text_color="black").place(relx=0.5, rely=0.5, anchor="center")
ctk.CTkButton(header_frame, text="🚪", width=40, command=logout, fg_color="transparent").place(relx=1.0, x=-45, y=10)

# Outer Container for Event Card
event_outer = ctk.CTkFrame(app, fg_color="#A6939E", width=300, height=250, corner_radius=10)
event_outer.place(relx=0.5, rely=0.5, anchor="center")

# Inner Event Card
event_card = ctk.CTkFrame(event_outer, width=250, height=80, fg_color="white", corner_radius=10)
event_card.place(relx=0.5, rely=0.2, anchor="n")

# Icon (optional: replace with an actual image)
calendar_icon = ctk.CTkLabel(event_card, text="📅", font=("Arial", 24), text_color="black")
calendar_icon.place(x=10, y=20)

# Event Title
ctk.CTkLabel(event_card, text="Graduation Party", font=("Arial", 16), text_color="black").place(x=60, y=25)

app.mainloop()
