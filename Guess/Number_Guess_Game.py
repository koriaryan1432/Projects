import random
import tkinter as tk
from tkinter import messagebox
import ico

# Generate a random number between 1 and 100
secret_number = random.randint(1, 10)

# Create the main window
window = tk.Tk()
window.title("Number Guessing Game")
window.geometry("400x400")

# Set the background image
bg_image = tk.PhotoImage(file="C:/Users/koria/Downloads/ii.jpg")
bg_label = tk.Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create the text box and label
text_box = tk.Entry(window, font=("Times New Roman", 24))
text_box.place(relx=0.5, rely=0.5, anchor="center")
label = tk.Label(window, text="Guess the number between 1 and 10:", font=("Times New Roman", 18))
label.pack(pady=10)

# Keep track of the number of guesses
num_guesses = 0

# Function to handle button click
def check_guess():
    global num_guesses
    num_guesses += 1
    guess = int(text_box.get())
    if guess == secret_number:
        result = f"Congratulations! You guessed the number in {num_guesses} guesses."
        tk.messagebox.showinfo("Result", result)
        window.destroy()
    elif guess < secret_number:
        tk.messagebox.showerror("Error", "Your guess is too low. Try again.")
    else:
        tk.messagebox.showerror("Error", "Your guess is too high. Try again.")

# Create the submit button
submit_button = tk.Button(window, text="Submit", font=("Times New Roman", 18), command=check_guess)
submit_button.pack(pady=10)

# Start the main loop
window.mainloop()
