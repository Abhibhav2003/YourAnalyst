import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as plt
import time
import requests
from streamlit_lottie import st_lottie

# Set the page configuration
st.set_page_config(page_title="YourAnalyst", page_icon=None, layout="wide")

def load_lottie_url(url):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()
        
animation = load_lottie_url("https://lottie.host/46d346ba-c57b-452c-ac6f-2b4a34d4d87d/YUWkpeSAFk.json")
left_column, right_column = st.columns(2)

with left_column:
            st_lottie(animation, height=200, key="analyzing")
with right_column:
            st.title("Welcome To One-Of-A Kind Data Analysis WebApp!")
            text_list = [
                "Data is the new oil!",
                "Unlock insights from your data.",
                "Make informed decisions quickly.",
                "Data visualization made easy.",
                "Dive deep into insights.",
                "Your data has a story to tell.",
                "Let us help you uncover it!"
            ]    
            placeholder = st.empty()

            while True:  # Infinite loop
                for text in text_list:
                    # Typing effect (character by character)
                    current_text = ""
                    for char in text:
                        current_text += char  # Append the next character
                        placeholder.markdown(f"<h4 style='text-align: left;'>{current_text}</h4>", unsafe_allow_html=True)
                        time.sleep(0.05)  # Adjust the speed of typing here

                    time.sleep(1)  # Pause before erasing

                    # Erasing effect (character by character)
                    for _ in range(len(text)):  # Iterate over each character in the full text
                        current_text = text[:-_ - 1]  # Erase one character
                        placeholder.markdown(f"<h4 style='text-align: left;'>{current_text}</h4>", unsafe_allow_html=True)
                        time.sleep(0.05)  # Adjust the speed of erasing here

                    time.sleep(1)  # Pause before the next text
