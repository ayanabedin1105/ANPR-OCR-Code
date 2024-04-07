# imports
import cv2
import easyocr
import os
import numpy as np
from matplotlib import pyplot as plt

# Function to preprocess the image and enhance license plate regions
def preprocess_image(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply edge detection to highlight edges
    edges = cv2.Canny(blurred, 50, 150)

    # Perform dilation to close gaps between edges
    kernel = np.ones((3, 3), np.uint8)
    dilated = cv2.dilate(edges, kernel, iterations=1)

    return dilated

# Function to extract text using EasyOCR
def extract_text(image):
    # Initialize EasyOCR reader with English language
    reader = easyocr.Reader(['en'])

    # Read text from the image using EasyOCR
    result = reader.readtext(image)

    # Extract and return the detected text
    extracted_text = ' '.join([text[1] for text in result])
    return extracted_text

# Path to the folder containing input images
input_folder = r"C:\Users\abedi\Downloads\College TU856 DT228\College Year 4\Final Year Project\Codes\UI_code\plate_folder"

# List all image files in the input folder
image_files = [os.path.join(input_folder, file) for file in os.listdir(input_folder) if file.endswith(('.jpg', '.jpeg', '.png'))]

# Process each image file
for image_file in image_files:
    # Load the image
    image = cv2.imread(image_file)

    # Preprocess the image
    processed_image = preprocess_image(image)

    # Extract text from the processed image
    extracted_text = extract_text(processed_image)

    # # Print the extracted text
    # print(f"Extracted Text ({image_file}):", extracted_text)

    # print the text only
    print(f"Extracted Text:", extracted_text)

    # # Display the processed image
    # plt.imshow(processed_image, cmap='gray')
    # plt.title("Processed Image")
    # plt.axis('off')
    # plt.show()