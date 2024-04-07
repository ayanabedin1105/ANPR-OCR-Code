from IPython.display import Image, display
import matplotlib.pyplot as plt
import os
import easyocr
#link firebase to collab
import firebase_admin
from firebase_admin import credentials, db
import datetime

# Initialize firebase admin SDK with your Firebase project credentials
cred = credentials.Certificate(r"C:\Users\abedi\Downloads\College TU856 DT228\College Year 4\Final Year Project\Codes\Parking-Management\anpr-data-firebase-adminsdk-w26xb-2441736885.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://anpr-data-default-rtdb.europe-west1.firebasedatabase.app'
})


#directory containing images
images_directory = r"C:\Users\abedi\Downloads\College TU856 DT228\College Year 4\Final Year Project\Codes\UI_code\plate_folder"

#list all the files in the directory
image_files = os.listdir(images_directory)

# Filter out only the image files
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
image_files = [file for file in image_files if os.path.splitext(file)[1].lower() in image_extensions]

# Display all the images
for image_file in image_files:
    image_path = os.path.join(images_directory, image_file)
    display(Image(filename=image_path))

reader = easyocr.Reader(['en'])

# Loop through each image file
for image_file in image_files:
    if image_file.endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp')):  # Check if the file is an image
        image_path = os.path.join(images_directory, image_file)

        # Perform OCR on the image
        result = reader.readtext(image_path)

        # Display the results
        print(f"Text detected in {image_file}:")
        for detection in result:
            print(detection[1])  # Display the detected text
        print("-" * 20)  # Separator between images

#Firebase Database
# Get a reference to the Realtime Database
db_ref = db.reference('image_text_output')

# Loop through each image file
for image_file in image_files:
    if image_file.endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp')):  # Check if the file is an image
        image_path = os.path.join(images_directory, image_file)

        # Perform OCR on the image
        result = reader.readtext(image_path)

        # Store the detected text in a list
        detected_text = [detection[1] for detection in result]

        # Push the detected text to the Firebase Realtime Database
        db_ref.push({
            'image_file': image_file,
            'detected_text': detected_text
        })