import random
import string
import tkinter as tk
import pyperclip
from tkinter import ttk
from colorsys import hsv_to_rgb

def generate_password():
    password_length = password_length_entry.get()
    
    if not password_length.isdigit() or int(password_length) <= 0:
        feedback_label.config(text="Invalid password length", fg="red")
        return
    

    characters = string.ascii_letters + string.digits + string.punctuation
    

    password = ''.join(random.choice(characters) for _ in range(int(password_length)))
    

    password_label.config(text="Generated Password: " + password)
    
    global generated_password
    generated_password = password

def copy_password():
    if generated_password:

        pyperclip.copy(generated_password)
        feedback_label.config(text="Password copied to clipboard", fg="green")
    else:
        feedback_label.config(text="No password generated yet", fg="red")


window = tk.Tk()
window.title("Random Password Generator")
window.configure(bg="purple")

password_length_label = tk.Label(window, text="Password Length: ", bg="purple", fg="white")
password_length_label.pack(pady=10)
password_length_entry = tk.Entry(window)
password_length_entry.pack(pady=5)

password_label = tk.Label(window, text="Generated Password: ", bg="purple", fg="white")
password_label.pack(pady=10)

generate_button = tk.Button(window, text="Generate Password", command=generate_password, bg="purple", fg="white")
generate_button.pack(pady=5)

copy_button = tk.Button(window, text="Copy Password", command=copy_password, bg="purple", fg="white")
copy_button.pack(pady=5)

feedback_label = tk.Label(window, text="", bg="purple", fg="white")
feedback_label.pack(pady=5)

h, s, v = 0.7, 1.0, 1.0  
complementary_h = (h + 0.5) % 1.0  
complementary_rgb = hsv_to_rgb(complementary_h, s, v)  
complementary_fg_color = '#%02x%02x%02x' % tuple(int(c * 255) for c in complementary_rgb)
password_label.config(fg=complementary_fg_color)

window.mainloop()
