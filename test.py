from flask import Flask, render_template, request
from dotenv import load_dotenv
from PIL import Image
import os
import google.generativeai as genai


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
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
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
You are an expert in nutritionist where you need to see the food items from the image
               and calculate the total calories, also provide the details of every food items with calories intake
               is below format

               1. Item 1 - no of calories
               2. Item 2 - no of calories
               ----
               ----


"""
    
    return render_template('index.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
