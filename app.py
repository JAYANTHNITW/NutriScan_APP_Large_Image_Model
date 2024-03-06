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
Think your a expert nutritionalist.

1. Detailed Nutritional Table:

Provide a detailed breakdown of the nutritional content for each food item in the provided image, including calories, proteins, carbohydrates, fibers, and fats.
| Item | Calories | Proteins | Carbohydrates | Fibers | Fats |
|------|----------|----------|---------------|--------|------|
| Item 1 | [Value] | [Value] | [Value] | [Value]| [Value] |
| Item 2 | [Value] | [Value] | [Value] | [Value]| [Value] |
| ... | ... | ... | ... | ... | ... |

2. Ideal Macronutrient Ratio vs. Analyzed Ratio:

Compare the ideal macronutrient ratio for a healthy diet (based on ICMR or other suitable guidelines) with the approximate ratio analyzed from the food image. Highlight potential areas of imbalance.
| Macronutrient | Ideal Ratio | Analyzed Ratio |
|----------------|-------------|----------------|
| Proteins | [Value] | [Value] |
| Carbohydrates | [Value] | [Value] |
| Fibers | [Value] | [Value] |
| Fats | [Value] | [Value] |

3. Actionable Guidance:

Provide actionable guidance based on the analysis, focusing on excess macronutrients and suggestions for balance.


Excess Macronutrients:
Identify any macronutrients (carbs, fats, etc.) consumed in excess compared to the ideal ratio. 
praticularly when the carbohydrates analyzed ratio and ideal one, don't make mistake
that if the analyzed ratio is in the range of ideal, don't say Carbohydrates are consumed in excess compared to the ideal ratio
Suggestions for reducing excess intake.
Suggestions for Balance:

Give guidance regarding the importance of balance and recommend healthy sources of other macronutrients if any are lacking.
"""

## If submit button is clicked

if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data)
    st.subheader("The Response is")
    st.write(response)
