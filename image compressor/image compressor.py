import PIL  # Import the Python Imaging Library (Pillow) for image processing
from PIL import Image  # Import the Image module from Pillow
from tkinter.filedialog import *  # Import file dialog functions from tkinter for opening and saving files

# Open a file dialog to select an image file
file_path = askopenfilename()

# Open the selected image using Pillow
img = PIL.Image.open(file_path)

# Get the current dimensions (height and width) of the image
myHeight, myWidth = img.size

# Resize the image to its original dimensions (this line effectively keeps the image the same size)
img = img.resize((myHeight, myWidth), PIL.Image.ANTIALIAS)  # Use ANTIALIAS to improve the quality of the resized image

# Open a save file dialog to specify where to save the compressed image
save_path = asksaveasfilename()

# Save the resized image with "compressed.jpg" added to the filename
img.save(save_path + "compressed.jpg")
