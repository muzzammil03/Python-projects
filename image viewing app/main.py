from tkinter import *  # Import everything from tkinter for GUI creation
from tkinter import filedialog  # Import filedialog for opening file dialog boxes
import tkinter as tk  # Import tkinter with an alias for convenience
from PIL import Image, ImageTk  # Import PIL (Pillow) for image handling
import os  # Import os for operating system related functions

# Function to open and display an image
def showimage():
    # Open a file dialog to select an image file
    filename = filedialog.askopenfilename(
        initialdir=os.getcwd(),  # Start in the current working directory
        title="Select image file",  # Title of the file dialog
        filetype=(("JPG File", "*.jpg"), ("PNG file", "*.png"), ("All file", "how are you.txt"))  # Supported file types
    )
    
    # Open the selected image using PIL
    img = Image.open(filename)
    # Convert the image to a format that tkinter can use
    img = ImageTk.PhotoImage(img)
    
    # Configure the label to display the selected image
    lbl.configure(image=img)
    lbl.image = img  # Keep a reference to the image to prevent garbage collection

# Set up the main window
root = Tk()

# Create a frame at the bottom of the window to hold buttons
fram = Frame(root)
fram.pack(side=BOTTOM, padx=15, pady=15)

# Create a label that will display the image
lbl = Label(root)
lbl.pack()

# Button to trigger the showimage function
btn = Button(fram, text="Select Image", command=showimage)
btn.pack(side=tk.LEFT)

# Button to exit the application
btn2 = Button(fram, text="Exit", command=lambda: exit())
btn2.pack(side=tk.LEFT, padx=12)

# Set the title of the window
root.title("Image Viewer")

# Start the main event loop
root.mainloop()
