import tkinter as tk
from ui.gui import BibliotecaApp

def main():
    root = tk.Tk()
    app = BibliotecaApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()