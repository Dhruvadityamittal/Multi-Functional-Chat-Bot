import google.generativeai as genai
import os
from dotenv import load_dotenv  # Used to load key value pairs from .env file
import numpy as np
from PIL import Image

load_dotenv() 

API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

import streamlit as st




st.title("Chat GPT")
st.write("Hi I am Chat GPT using Google Gemini Model to help you!!")
# prompt = st.chat_input("Say something")
input = st.text_input("Input", key = 'input')
submit = st.button("Ask")

if(submit and input):

    if('chat_history' not in st.session_state):
        st.session_state['chat_history'] = []
    # response = model.generate_content(prompt)
    
    response =chat.send_message(input,stream=True)
    for chunk in response:

        
        st.session_state['chat_history'].append(("User",input))
        st.session_state['chat_history'].append(("Bot",chunk.text))
        
        print("_"*80)

    print("Length -?>>",len(st.session_state['chat_history'][-2:]))
    for role,text in st.session_state['chat_history']:
        print(f"{role} {text}")
        st.write(f"{role} -> {text}")
    st.write("_"*80)
    

    # print(chat.history)
    # st.write(chat.histor)
    # st.write(response.text)
    
    # if prompt:
    #     st.write(f"User: {prompt}")
    #     st.write(f"Chat Bot: {response.text}")

# st.write(chat.history)
# print("Print History ",chat.history)
    


# img_file_buffer = st.file_uploader('Upload a PNG image', type='jpg')

# if img_file_buffer is not None:
#     image = Image.open(img_file_buffer)
#     img_array = np.array(image)
#     print("Image",image)
#     st.image(image, caption='Uploaded Image')


#     if(prompt):
#         model = genai.GenerativeModel('gemini-1.5-flash')
#         response = model.generate_content([prompt, image])
#         st.write(f"Chat Bot GF: {response.text}")
#         print(response.text)

