import random
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

root = tk.Tk()
root.geometry("400x400")
root.grid_columnconfigure(2, weight=1)
root.title("Party Hire Shop")
root.configure(bg='orange')
customers = []
