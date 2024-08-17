import tkinter  # Import the tkinter library for GUI creation
from tkinter import *

# Create the main window object
root = Tk()
root.title("Simple Calculator")  # Set the title of the window
root.geometry("570x600+100+200")  # Set the window size and position
root.resizable(False, False)  # Disable window resizing
root.configure(bg="#17161b")  # Set the background color of the window
root.iconbitmap("favicon.ico")  # Set the window icon (must have the favicon.ico file)

# Global variable to store the equation entered by the user
equation = ""

# Function to display the button value on the screen
def show(value):
    global equation
    equation += value  # Append the pressed button's value to the equation
    label_result.config(text=equation)  # Update the label to show the current equation

# Function to clear the current equation
def clear():
    global equation
    equation = ""  # Reset the equation to an empty string
    label_result.config(text=equation)  # Clear the label

# Function to calculate the result of the equation
def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)  # Evaluate the equation
        except:
            result = "error"  # Show error if the evaluation fails
            equation = ""
    label_result.config(text=result)  # Update the label with the result

# Label to display the equation/result
label_result = Label(root, width=25, height=2, text="", font=("arial", 30))
label_result.pack()

# Creating buttons for the calculator
Button(root, text="C", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda: clear()).place(x=10, y=100)
Button(root, text="/", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("/")).place(x=150, y=100)
Button(root, text="%", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("%")).place(x=290, y=100)
Button(root, text="*", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("*")).place(x=430, y=100)

Button(root, text="7", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("7")).place(x=10, y=200)
Button(root, text="8", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("8")).place(x=150, y=200)
Button(root, text="9", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("9")).place(x=290, y=200)
Button(root, text="-", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("-")).place(x=430, y=200)

Button(root, text="4", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("4")).place(x=10, y=300)
Button(root, text="5", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("5")).place(x=150, y=300)
Button(root, text="6", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("6")).place(x=290, y=300)
Button(root, text="+", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("+")).place(x=430, y=300)

Button(root, text="1", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("1")).place(x=10, y=400)
Button(root, text="2", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("2")).place(x=150, y=400)
Button(root, text="3", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("3")).place(x=290, y=400)
Button(root, text="0", width=11, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show("0")).place(x=10, y=500)

Button(root, text=".", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=lambda: show(".")).place(x=290, y=500)
Button(root, text="=", width=5, height=3, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#fe9037", command=lambda: calculate()).place(x=430, y=400)

# Start the main loop of the application
root.mainloop()
