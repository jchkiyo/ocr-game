import easyocr

# Initialize the reader with the languages you need (e.g., English)
reader = easyocr.Reader(['en'], gpu=True)  # Set gpu=True if you have a compatible GPU

# Read text from the image
results = reader.readtext('samples\photo_2024-09-23_15-00-26.jpg')

# Print detected text
for (bbox, text, confidence) in results:
    print(f'Text: {text}, Confidence: {confidence}')
