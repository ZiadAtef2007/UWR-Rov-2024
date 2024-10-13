import cv2
import numpy as np

def detect_shapes(image_path):
    """
    Attempts to detect circles, crosses, squares, and triangles in an image.

    Args:
        image_path (str): Path to the image file.
    """

    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150) 

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    circles = 0
    crosses = 0
    squares = 0
    triangles = 0

    for contour in contours:
        # Approximate the shape of the contour
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.04 * perimeter, True) 

        # Analyze the number of sides
        sides = len(approx)

        if sides == 3:
            triangles += 1
        elif sides == 4:
            # Differentiate between squares and rectangles (crude check)
            x, y, w, h = cv2.boundingRect(approx)
            aspectRatio = float(w) / h
            if 0.95 <= aspectRatio <= 1.05: 
                squares += 1
        elif 4 <= sides <= 8:  # Adjust threshold for crosses
            # Additional logic to detect crosses more reliably (e.g., line intersection)
            # This is a placeholder, you'll need more sophisticated checks
            crosses += 1 
        elif sides >= 8:  # Adjust threshold for circles
            circles += 1

    print("Circles:", circles)
    print("Crosses:", crosses)
    print("Squares:", squares)
    print("Triangles:", triangles)


# Example usage:
image_path = "E:\Competitions\Rov\Python\Shapes\Shapes.png" 
detect_shapes(image_path) 