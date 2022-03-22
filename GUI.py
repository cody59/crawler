import tkinter as tk

def window():
    window = tk.Tk()
    greeting = tk.Label(text="hi")
    greeting.pack()


if __name__ == "__main__":
    window()