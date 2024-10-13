import tkinter as tk
from PIL import Image, ImageDraw, ImageTk

root = tk.Tk()
root.title("Image Clicker")

# Load the image using Pillow
pil_image = Image.open("Net.png")

# Create a Tkinter-compatible image
image = ImageTk.PhotoImage(pil_image)

image_label = tk.Label(root, image=image)
image_label.pack()

# Initialize counters for left and right clicks
left_clicks = 0
right_clicks = 0

# Initialize counters for left and right clicks in each quarter
top_left_left_clicks = 0
top_left_right_clicks = 0
top_right_left_clicks = 0
top_right_right_clicks = 0
bottom_left_left_clicks = 0
bottom_left_right_clicks = 0
bottom_right_left_clicks = 0
bottom_right_right_clicks = 0

def get_quarter(x, y, image_width, image_height):
    if x < image_width / 2 and y < image_height / 2:
        return "Top-Left"
    elif x >= image_width / 2 and y < image_height / 2:
        return "Top-Right"
    elif x < image_width / 2 and y >= image_height / 2:
        return "Bottom-Left"
    else:
        return "Bottom-Right"

def on_left_click(event):
    global left_clicks
    global top_left_left_clicks
    global top_right_left_clicks
    global bottom_left_left_clicks
    global bottom_right_left_clicks
    left_clicks += 1
    
    # Get the mouse coordinates from the event object
    x, y = event.x, event.y
    
    # Create a drawing context
    draw = ImageDraw.Draw(pil_image)
    
    # Draw a circle at the mouse coordinates
    draw.ellipse([(x-10, y-10), (x+10, y+10)], fill=None, outline="blue", width=5)
    
    # Update the Tkinter image
    image = ImageTk.PhotoImage(pil_image)
    image_label.config(image=image)
    image_label.image = image  # keep a reference to prevent garbage collection
    
    # Get the quarter of the image
    quarter = get_quarter(x, y, pil_image.width, pil_image.height)
    
    # Update the click counters
    if quarter == "Top-Left":
        top_left_left_clicks += 1
    elif quarter == "Top-Right":
        top_right_left_clicks += 1
    elif quarter == "Bottom-Left":
        bottom_left_left_clicks += 1
    else:
        bottom_right_left_clicks += 1
    
    # Update the click counters label
    click_counter_label.config(text=f"Left clicks: {left_clicks}, Right clicks: {right_clicks}\n"
                                 f"Top-Left: {top_left_left_clicks} left, {top_left_right_clicks} right\n"
                                 f"Top-Right: {top_right_left_clicks} left, {top_right_right_clicks} right\n"
                                 f"Bottom-Left: {bottom_left_left_clicks} left, {bottom_left_right_clicks} right\n"
                                 f"Bottom-Right: {bottom_right_left_clicks} left, {bottom_right_right_clicks} right")

def on_right_click(event):
    global right_clicks
    global top_left_right_clicks
    global top_right_right_clicks
    global bottom_left_right_clicks
    global bottom_right_right_clicks
    right_clicks += 1
    
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
    
    # Get the quarter of the image
    quarter = get_quarter(x, y, pil_image.width, pil_image.height)
    
    # Update the click counters
    if quarter == "Top-Left":
        top_left_right_clicks += 1
    elif quarter == "Top-Right":
        top_right_right_clicks += 1
    elif quarter == "Bottom-Left":
        bottom_left_right_clicks += 1
    else:
        bottom_right_right_clicks += 1
    
    # Update the click counters label
    click_counter_label.config(text=f"Left clicks: {left_clicks}, Right clicks: {right_clicks}\n"
                                 f"Top-Left: {top_left_left_clicks} left, {top_left_right_clicks} right\n"
                                 f"Top-Right: {top_right_left_clicks} left, {top_right_right_clicks} right\n"
                                 f"Bottom-Left: {bottom_left_left_clicks} left, {bottom_left_right_clicks} right\n"
                                 f"Bottom-Right: {bottom_right_left_clicks} left, {bottom_right_right_clicks} right")

# Create a label to display the click counters
click_counter_label = tk.Label(root, text="Left clicks: 0, Right clicks: 0\n"
                                        "Top-Left: 0 left, 0 right\n"
                                        "Top-Right: 0 left, 0 right\n"
                                        "Bottom-Left: 0 left, 0 right\n"
                                        "Bottom-Right: 0 left, 0 right")
click_counter_label.pack()

image_label.bind("<Button-1>", on_left_click)  # left-click
image_label.bind("<Button-3>", on_right_click)  # right-click

root.mainloop()