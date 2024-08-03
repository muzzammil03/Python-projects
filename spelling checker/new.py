from tkinter import *  # Importing all components from tkinter library for GUI creation
from textblob import TextBlob  # Importing TextBlob for spelling correction

# Initialize the main window
root = Tk()
root.title("Spelling Checker")  # Set the title of the window
root.geometry("700x400")  # Set the size of the window (width x height)
root.config(background="#dae6f6")  # Set the background color of the window
root.iconbitmap("favicon.ico")  # Set the icon of the window (make sure 'favicon.ico' exists)

# Define constants for styling
FONT = ("Poppins", 20)  # Font style for text
BG_COLOR = "#dae6f6"  # Background color for labels and window
FG_COLOR = "#364971"  # Foreground color for text
BUTTON_COLOR = "green"  # Background color for the button
BUTTON_TEXT_COLOR = "white"  # Text color for the button

# Function to check spelling
def check_spelling():
    # Get the text entered by the user
    word = enter_text.get()
    
    # Check if the user has entered text
    if not word.strip():
        # If no text is entered, show a message asking the user to enter some text
        spell.config(text="Please enter some text.")
        return

    try:
        # Create a TextBlob object with the entered text
        blob = TextBlob(word)
        # Get the corrected text
        corrected_text = str(blob.correct())
        # Display the corrected text on the label
        spell.config(text=f"Correct text is: {corrected_text}")
    except Exception as e:
        # If there's an error, display the error message
        spell.config(text=f"Error: {str(e)}")

# Create a label to display the heading
heading = Label(root, text="Spelling Checker", font=("Trebuchet MS", 30, "bold"), bg=BG_COLOR, fg=FG_COLOR)
heading.pack(pady=(50, 0))  # Place the label with some vertical padding

# Create an entry widget where the user can type text
enter_text = Entry(root, justify="center", width=30, font=("Poppins", 25), bg="white", border=2)
enter_text.pack(pady=10)  # Place the entry widget with some vertical padding
enter_text.focus()  # Set focus on the entry widget so the user can start typing immediately

# Create a button that the user can click to check the spelling
button = Button(root, text="Check", font=("Poppins", 20, "bold"), fg=BUTTON_TEXT_COLOR, bg=BUTTON_COLOR, command=check_spelling)
button.pack(pady=10)  # Place the button with some vertical padding

# Create a label to display the corrected text
spell = Label(root, font=FONT, bg=BG_COLOR, fg=FG_COLOR)
spell.place(x=100, y=250)  # Place the label at a specific position (x, y)

# Start the Tkinter event loop to run the application
root.mainloop()
