import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as plt
import time
import requests
from streamlit_lottie import st_lottie

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
anim_placeholder = st.empty()     
uploaded_file = st.file_uploader("Choose Your File", type=['csv', 'xlsx', 'txt'])
        
if uploaded_file is not None:
    # Progress Bar...
        st.session_state.uploaded_file = uploaded_file 
        progress_container = st.empty()
        bar = progress_container.progress(0)

        for percent_complete in range(100):
            time.sleep(0.03)  # 3-second delay in total
            bar.progress(percent_complete + 1)

        st.success("File Uploaded")
        anim_placeholder.empty()
        anim = load_lottie_url("https://lottie.host/a9bdf4d8-ce93-46e7-85dd-01937e872f64/rBFm9SBGgF.json")
        st_lottie(anim, height=100, key="done") 
        progress_container.empty()  # Clear the progress bar