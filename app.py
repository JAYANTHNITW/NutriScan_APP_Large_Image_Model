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


As a nutritionist expert, your task is to analyze food items from the provided image and create a detailed table for each item, including information on total : calories, proteins, carbohydrates, fibers, and other relevant nutritional components.
in the below format
 

Output Table Format:
| Item         | Calories | Proteins | Carbohydrates | Fibers |
|--------------|----------|----------|---------------|--------|
| Item 1       | [Value]  | [Value]  | [Value]       | [Value]|
| Item 2       | [Value]  | [Value]  | [Value]       | [Value]|
| ...          | ...      | ...      | ...           | ...    |

Finally you can also mention whether the food is healthy or not and also mention the 
percentage split of the ratio of carbohydrates,fats,fibers,sugera and other relevant things required inour diet.
and finally say whether food is nutrious or not

"""

## If submit button is clicked

if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data)
    st.subheader("The Response is")
    st.write(response)
