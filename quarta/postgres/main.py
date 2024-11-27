import tkinter as tk
from tkinter import *
import matplotlib.pyplot as plt
from query import get_rentals

def graph(genres, rentals_per_genre, year):
    plt.title(f"DVD Rentals per Genre in {year}")
    plt.xlabel("Genre")
    plt.ylabel("Number of Rentals")

    plt.bar(genres, rentals_per_genre)
    plt.grid(axis='y', color='green', linestyle='--', linewidth=1)
    plt.show()

def query(year):
    rentals = {}

    if get_rentals(year):
        for genre, times_rented in get_rentals(year):
            rentals[genre] = times_rented

        genres = list(rentals.keys())
        rentals_per_genre = list(rentals.values())

        graph(genres, rentals_per_genre, year)
    else:
        warning = Label(window, text=f"There are no rentals in {year}", font=('Arial', 15))
        warning.pack(pady=20)
        warning.after(5000, warning.destroy)


window = Tk()
window.geometry('400x250')

Label(window, text="Insert year", font=('Arial', 25)).pack()

entry = Entry(window, width=40, font=('Arial', 20))
entry.focus_set()
entry.pack(padx=100, pady=20)

tk.Button(window, text="Go", width=20, font=('Arial', 15), command=lambda: query(entry.get())).pack(padx=150)
tk.Button(window, text="Quit", width=20, font=('Arial', 15), command=lambda: window.destroy()).pack(padx=150)

window.mainloop()
