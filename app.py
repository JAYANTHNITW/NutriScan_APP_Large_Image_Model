import streamlit as st
import google.generativeai as genai 
import os
from dotenv import load_dotenv
load_dotenv() # loading all the envinorment variables
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_prompt,image):
    model = genai.GenerativeModel("gemini-pro-vision")
    responses = model.generate_content([input_prompt,image[0]])
    return responses.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [

            {
                "mime_type": uploaded_file.type, # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

## Intialize our streamlit app
    
st.set_page_config(page_title="NutriScan APP")

st.header("NutriScan APP")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])
image =""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the Nutritional Content ")

input_prompt = """


As a nutritionist expert, your task is to analyze food items from the provided image and perform the following:

Provide a Detailed Nutritional Table:

Format: | Item | Calories | Proteins | Carbohydrates | Fibers | Fats | |--------------|----------|----------|---------------|--------|----------| | Item 1 | [Value] | [Value] | [Value] | [Value]| [Value] | | Item 2 | [Value] | [Value] | [Value] | [Value]| [Value] | | ... | ... | ... | ... | ... | ... |
Ideal Macronutrient Ratio vs. Analyzed Ratio:

Display a table comparing the ideal macronutrient ratio for a healthy diet (based on ICMR or other suitable guidelines) alongside the approximate ratio analyzed from the food image. This highlights potential areas of imbalance in the user's meal.
Actionable Guidance:  

Focus on Excess: Identify the macronutrients (carbs, fats, etc.) that seem to be consumed in excess compared to the ideal ratio.
Suggestions: Provide specific suggestions for reducing the excessive macronutrient. Example: "It seems carbohydrates are a bit high in this meal. Try swapping a portion of [carb-heavy food] for a green salad or other vegetables."
Balance: Emphasize the importance of balance and direct the user towards healthy sources of other macronutrients if any are lacking.

"""

## If submit button is clicked

if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data)
    st.subheader("The Response is")
    st.write(response)
