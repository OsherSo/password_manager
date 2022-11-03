import tkinter as tk
from tkinter import messagebox

from random import choice, randint, shuffle

LETTERS = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


class App(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.canvas = tk.Canvas(height=200, width=250)
        self.logo_img = tk.PhotoImage(file="logo.png")
        self.canvas.create_image(100, 100, image=self.logo_img)
        self.canvas.grid(row=0, column=1)
        # Labels
        self.website_label = tk.Label(text="Website:")
        self.website_label.grid(row=1, column=0)
        self.email_label = tk.Label(text="Email/Username:")
        self.email_label.grid(row=2, column=0)
        self.password_label = tk.Label(text="Password:")
        self.password_label.grid(row=3, column=0)
        # Entry's
        self.website_entry = tk.Entry(width=35)
        self.website_entry.grid(row=1, column=1, columnspan=2)
        self.website_entry.focus()
        self.email_entry = tk.Entry(width=35)
        self.email_entry.grid(row=2, column=1, columnspan=2)
        self.password_entry = tk.Entry(width=35)
        self.password_entry.grid(row=3, column=1, columnspan=2)
        # Buttons
        self.generate_password_button = tk.Button(text="Generate Password", command=self.generate_password)
        self.generate_password_button.grid(row=4, column=1, columnspan=2)
        self.add_button = tk.Button(text="Add", width=28, command=self.save)
        self.add_button.grid(row=6, column=1, columnspan=2)

    def generate_password(self):
        self.password_entry.delete(0, "end")
        password_letters = [choice(LETTERS) for _ in range(randint(8, 10))]
        password_numbers = [choice(NUMBERS) for _ in range(randint(2, 4))]
        password_symbols = [choice(SYMBOLS) for _ in range(randint(2, 4))]

        password_list = password_letters + password_symbols + password_numbers
        shuffle(password_list)

        password = "".join(password_list)
        self.password_entry.insert(0, password)

    def save(self):
        website = self.website_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        if len(website) == 0 or len(email) == 0 or len(password) == 0:
            messagebox.showinfo(title="Error", message="Please make sure you haven't left any fields empty.")
        elif messagebox.askokcancel(title=website,
                                    message=f"These are the details entered: \nEmail: {email}\nPassword: "
                                            f"{password}\nIs it ok to save?"):
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                self.website_entry.delete(0, "end")
                self.password_entry.delete(0, "end")


def main():
    window = tk.Tk()
    window.title("Password Manager")
    window.config(padx=50, pady=50)
    App(window).grid()
    window.mainloop()


if __name__ == "__main__":
    main()
