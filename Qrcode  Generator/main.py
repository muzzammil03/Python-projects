from tkinter import *  # Import all tkinter functions for GUI creation
import qrcode  # Import qrcode library for generating QR codes

# Function to generate and save the QR code
def generate():
    name = title.get()  # Get the title from the input field
    text = entry.get()  # Get the text to encode from the input field
    qr = qrcode.make(text)  # Create a QR code from the input text
    qr.save("Qrcode/" + str(name) + ".png")  # Save the QR code as a PNG file with the title as the name

    global Image  # Declare the Image variable as global to update the label
    Image = PhotoImage(file="Qrcode/" + str(name) + ".png")  # Load the saved QR code image
    Image_view.config(image=Image)  # Update the label to display the generated QR code

# Set up the main window
root = Tk()
root.title("QR Generator")  # Set the window title
root.geometry("1000x550")  # Set the window size
root.config(bg="#5c6f73")  # Set the background color
root.resizable(False, False)  # Disable window resizing

# Label to display the generated QR code
Image_view = Label(root, bg="#5c6f73")
Image_view.pack(padx=50, pady=10, side=RIGHT)  # Position the label on the right side

# Label and entry for the QR code title
Label(root, text="Title", fg="white", bg="#5c6f73", font=15).place(x=50, y=170)  # Label for title input
title = Entry(root, width=13, font="arial 15")  # Input field for the title
title.place(x=50, y=200)  # Position the title input field

# Entry field for the text to encode in the QR code
entry = Entry(root, width=28, font="arial 15")  # Input field for the text to be converted into a QR code
entry.place(x=50, y=250)  # Position the text input field

# Button to generate the QR code
Button(root, text="Generate QR", width=20, height=2, bg="black", fg="white", command=generate).place(x=50, y=300)

# Start the main event loop
root.mainloop()
