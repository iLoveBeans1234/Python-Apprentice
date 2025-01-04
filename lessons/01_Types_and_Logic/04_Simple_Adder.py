"""
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.
bob
In this program we will just give you the comments for what you need to do. Look
at the comments and the code snippets in the previous lessons, like
03_My_Ages.py, to figure out how to complete the program.


"""

# Import the required modules
from tkinter import simpledialog, messagebox, Tk
# Create a window object
window = Tk
# Hide the window, hint: use the withdraw method
window.withdraw
# Ask the user for the first number   
user = simpledialog.askstring(title="user", prompt="Give me any nunber 1 through 5")
# Ask the user for the second number
user = simpledialog.askstring(title="user", prompt="Give me another number 1 through 100")
# Display the sum of the two numbers 
if user == 1:
    messagebox.showinfo(1+1=2)
# Keep the window open