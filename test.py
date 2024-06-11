from flask import Flask, render_template, request
from dotenv import load_dotenv
from PIL import Image
import os
import google.generativeai as genai
import warnings
# warnings.filterwarnings("ignore")

# import streamlit

# streamlit._is_running_with_streamlit = False

# Load environment variables
load_dotenv()

# Configure Flask app
app = Flask(__name__)

# Function to load Google Gemini Pro Vision API and get response
def get_gemini_response(input, image, prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input,image[0],prompt])
    return response.text

# Function to process uploaded image
def input_image_setup(uploaded_file):
   
     # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.read()

        image_parts = [
            {
                "mime_type": uploaded_file.content_type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Route for home page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_prompt = request.form['input_prompt']
        uploaded_file = request.files['file']
        if uploaded_file:
            image = Image.open(uploaded_file)
            image_data = input_image_setup(uploaded_file)
            response = get_gemini_response(input_prompt, image_data, input)
            return render_template('result.html', response=response)
    input_prompt="""
Your task is to analyze an image of a vehicle and determine the number of stickers present. Consider the following:

Image:

Quality: The image may be high or low resolution, with varying lighting conditions (bright sunlight, shadows, low light).
Perspective: The vehicle might be captured from different angles (front, back, side, angled).
Occlusions: Stickers may be partially or fully obstructed by other objects (dirt, reflections, people, other vehicles).
Types of Stickers: There could be a variety of sticker types:
Shape: Rectangular, circular, oval, irregular
Size: Tiny bumper stickers to large decals
Material: Paper, vinyl, reflective
Location: Windows, bumpers, body panels, license plates
Stickers:

Definition: A sticker is a piece of adhesive paper or plastic with a design or message attached to a surface. Consider all of these as stickers:
Bumper stickers
Decals (including custom designs, logos, etc.)
Promotional stickers
Parking permits
Warning labels
Inspection stickers
Reflective tape (if it forms a deliberate design or pattern)
Ambiguous Cases:
Not Stickers:
Painted graphics (not separate, applied elements)
Permanent markings (e.g., model designations, license plate numbers)
Dirt or debris that might resemble a sticker
Difficult to Count:
Overlapping stickers where it's hard to distinguish individual ones
Extremely small or faded stickers that are barely visible
Instructions:

Examine the Image: Carefully scrutinize the entire image, paying close attention to all visible surfaces of the vehicle.
Identify Stickers: Look for any distinct shapes, colors, or text that might indicate the presence of a sticker.
Differentiate: Distinguish stickers from painted graphics, markings, and other non-sticker elements.
Handle Occlusions: If a sticker is partially hidden, try to estimate its full shape and count it if you're reasonably confident it's a sticker.
Count Stickers: Count each individual sticker you can confidently identify. If stickers overlap significantly, try your best to estimate the count, noting the uncertainty.
Report Results: Provide the following information:
Total Sticker Count: The estimated number of stickers.
Confidence Level: Indicate your level of confidence in the count (e.g., "high confidence," "medium confidence," "low confidence").
Uncertainty: If there's any uncertainty due to occlusions or overlaps, describe the areas where the count is less certain.
Examples: If possible, provide examples of stickers you found (e.g., "a rectangular bumper sticker on the rear bumper," "a small circular sticker on the side window").
"""
    
    return render_template('index.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
