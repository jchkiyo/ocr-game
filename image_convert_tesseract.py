from PIL import Image
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter


def preprocess_image(image_path):
    image = Image.open(image_path)
    image = image.convert('L')  # Convert to grayscale
    image = image.filter(ImageFilter.MedianFilter())  # Remove noise
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)  # Increase contrast
    image = image.point(lambda x: 0 if x < 140 else 255)  # Binarize the image
    return image

# Load an image from file
image_path = 'samples\photo_2024-09-23_15-00-26.jpg'  # Replace with your image file path
image = Image.open(image_path)

# Convert the image to text
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)
