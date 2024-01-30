# Health Management Web App

## Overview

This web app is designed to provide information about the ingredients in a given food item based on an image. It uses the Google Gemini Pro Vision API to analyze the image and generate relevant details about the food items.

## Features

- Accepts an input prompt to guide the analysis.
- Allows users to upload an image (JPEG, JPG, or PNG) for processing.
- Provides information on the total calories and details of each food item recognized in the image.
- Recognizes ingredients used in packaged food items and provides their effects on human health, along with potential side effects.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/health-management-app.git
   cd health-management-app

## Install the required dependencies

pip install -r requirements.txt

## Set up environment variables

1. Create a .env file in the project root directory.
2. Add your Google API key to the .env file:
GOOGLE_API_KEY=your_api_key_here

## Usage

1. Run the Streamlit app:
 streamlit run app.py

2. Access the app in your browser at http://localhost:8501.
3. Input a prompt, choose an image, and click the "Submit" button to get information about the ingredients and calorie details

## Dependencies

Streamlit
Pillow (PIL)
Google GenerativeAI Gemine Pro
python-dotenv
