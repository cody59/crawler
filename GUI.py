import tkinter as tk

def Window():
    window = tk.Tk()
    label = tk.Label(window, text="")
    label.pack()
    window.mainloop()


if __name__ == "__main__":
    Window()