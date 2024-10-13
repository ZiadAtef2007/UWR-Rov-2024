import cv2
import numpy as np

# Load the reference image
ref_image = cv2.imread('Shapes.png')

# Load the image
image = cv2.imread('Shapes.png')

# Check if the image was loaded successfully
if image is None:
    print("Error: Unable to load image 'Shapes.jpg'.")
else:
    # Pre-process the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Detect triangles
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    triangles = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        x, y, w, h = cv2.boundingRect(contour)
        aspect_ratio = float(w)/h
        if area > 100 and aspect_ratio > 0.5 and aspect_ratio < 2:
            triangles += 1

    # Detect squares
    squares = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        x, y, w, h = cv2.boundingRect(contour)
        aspect_ratio = float(w)/h
        if area > 100 and abs(aspect_ratio - 1) < 0.2:  # aspect ratio close to 1
            squares += 1

    # Detect crosses
    crosses = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        x, y, w, h = cv2.boundingRect(contour)
        aspect_ratio = float(w)/h
        if area > 100 and (aspect_ratio > 2 or aspect_ratio < 0.5):  # aspect ratio far from 1
            crosses += 1

    # Detect circles
    circles = cv2.HoughCircles(thresh, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        circle_count = len(circles)
    else:
        circle_count = 0

    # Print the results
    print("Triangles:", triangles)
    print("Squares:", squares)
    print("Crosses:", crosses)
    print("Circles:", circle_count)

    # Display the reference image
    cv2.imshow('Reference Image', ref_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()