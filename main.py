from tkinter import *

# উইন্ডো তৈরি
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# ক্যানভাস (Logo Image)
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=0, columnspan=3)

# Website Label & Entry
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()  # কার্সর স্বয়ংক্রিয়ভাবে এখানে থাকবে

# Email/Username Label & Entry
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "your_email@gmail.com")  # ডিফল্ট ইমেইল দেখানোর জন্য

# Password Label & Entry
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Generate Password Button
generate_button = Button(text="Generate Password")
generate_button.grid(row=3, column=2)

# Add Button
add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2)

# উইন্ডো চালু রাখা
window.mainloop()
