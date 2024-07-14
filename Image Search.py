import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv  # Used to load key value pairs from .env file
import numpy as np
from PIL import Image
import streamlit as st

load_dotenv() 

API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])



st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)

st.title("Image Search")
st.sidebar.success("Select a page above.")

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Input a text here", st.session_state["my_input"])
submit = st.button("Submit")

if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered: ", my_input)


img_file_buffer = st.file_uploader('Upload a PNG image', type='jpg')


if img_file_buffer is not None:
    image = Image.open(img_file_buffer)
    img_array = np.array(image)
    print("Image",image)
    st.image(image, caption='Uploaded Image')


    if(my_input and submit):
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content([my_input, image])
        st.write(f"Chat Bot GF: {response.text}")
        print(response.text)