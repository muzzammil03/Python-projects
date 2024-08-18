from tkinter import *  # Import all functions from tkinter for GUI creation
import tkinter as tk  # Import tkinter with alias tk
import pyttsx3  # Import pyttsx3 for text-to-speech functionality

# Initialize the text-to-speech engine
text_speech = pyttsx3.init()

# Function to convert text to speech
def speak():
    text_speech.say(textv.get())  # Speak the text entered by the user
    text_speech.runAndWait()  # Wait until speaking is done
    text_speech.stop()  # Stop the speech engine

# Function to clear the text entry field
def clear():
    text.delete(0, END)  # Clear the text in the entry widget

# Set up the main window
root = Tk()
root.title("Text to Speech")  # Set the title of the window
root.geometry("600x300")  # Set the size of the window
root.resizable(False, False)  # Disable window resizing

# To add a logo, make sure you have a 'logo.ico' file in the same directory
root.iconbitmap("images.ico")  

textv = StringVar()  # Variable to store text from the entry widget

# Create a frame for the text-to-speech section
obj = LabelFrame(root, text="Text to Speech", font=20, bd=1)
obj.pack(fill="both", expand="yes", padx=10, pady=10)

# Label for the text entry
lbl = Label(obj, text="Text", font=30)
lbl.pack(side=tk.LEFT, padx=10)

# Entry widget for user to input text
text = Entry(obj, textvariable=textv, font=30, width=25, bd=5)
text.pack(side=tk.LEFT, padx=10)

# Button to trigger speech
btn = Button(obj, text="Speak", font=20, bg="black", fg="white", command=speak)
btn.pack(side=tk.LEFT, padx=10)

# Button to clear the text entry
btn = Button(obj, text="Clear", font=20, bg="black", fg="white", command=clear)
btn.pack(side=tk.LEFT, padx=10)

# Start the main event loop
root.mainloop()
