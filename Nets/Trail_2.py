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
    # Get the mouse coordinates from the event object
    x, y = event.x, event.y
    
    # Create a drawing context
    draw = ImageDraw.Draw(pil_image)
    
    # Draw an "X" at the mouse coordinates
    draw.line([(x-10, y-10), (x+10, y+10)], fill="red", width=5)  # top-left to bottom-right
    draw.line([(x+10, y-10), (x-10, y+10)], fill="red", width=5)  # top-right to bottom-left
    
    # Update the Tkinter image
    image = ImageTk.PhotoImage(pil_image)
    image_label.config(image=image)
    image_label.image = image  # keep a reference to prevent garbage collection


def on_left_click(event):
    # Get the mouse coordinates from the event object
    x, y = event.x, event.y
    
    # Create a drawing context
    draw = ImageDraw.Draw(pil_image)
    
    # Draw a circle at the mouse coordinates
    draw.ellipse([(x-10, y-10), (x+10, y+10)], fill=None, outline="red", width=5)
    
    # Update the Tkinter image
    image = ImageTk.PhotoImage(pil_image)
    image_label.config(image=image)
    image_label.image = image  # keep a reference to prevent garbage collection


image_label.bind("<Button-3>", on_right_click)
image_label.bind("<Button-3>", on_left_click)

root.mainloop()