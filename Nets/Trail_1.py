import tkinter as tk
from PIL import Image, ImageDraw, ImageTk

root = tk.Tk()
root.title("Image Clicker")

# Load the image using Pillow
pil_image = Image.open("net.png")

# Create a Tkinter-compatible image
image = ImageTk.PhotoImage(pil_image)

image_label = tk.Label(root, image=image)
image_label.pack()

def on_right_click(event):
    # Create a drawing context
    draw = ImageDraw.Draw(pil_image)
    
    # Draw an "X" on the image
    draw.line([(10, 10), (50, 50)], fill="red", width=5)  # top-left to bottom-right
    draw.line([(50, 10), (10, 50)], fill="red", width=5)  # top-right to bottom-left
    
    # Update the Tkinter image
    image = ImageTk.PhotoImage(pil_image)
    image_label.config(image=image)
    image_label.image = image  # keep a reference to prevent garbage collection

image_label.bind("<Button-3>", on_right_click)

root.mainloop()