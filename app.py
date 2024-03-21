import streamlit as st
import pandas as pd
import numpy as np
import ast
import os

import tensorflow as tf
from process import menu_model
def parse_uploaded_file_to_np_array(uploaded_file):
    if uploaded_file is not None:
        # Save the uploaded file locally
        with open("temp_file.txt", "wb") as f:
            f.write(uploaded_file.getvalue())

        # Read the local file
        with open("temp_file.txt", "r") as f:
            content = f.read()
            matrix = ast.literal_eval(content)
        
        # Remove the temporary file
        os.remove("temp_file.txt")

        # Convert to NumPy array
        np_array = np.array(matrix)
        return np_array
    else:
        return None
st.title('Lipreading App') 
st.divider()
st.write('Welcome to the Lipreading App! This app is designed to help you understand how to read lips. ')
st.write('Please upload the preprocessed text file and the corresponding video file. The app will show you the lip movements and the corresponding text. ')
text_file = st.file_uploader("Upload Text File", type=['txt'])
if text_file is not None:
    st.write('Text file uploaded successfully!')
    data = parse_uploaded_file_to_np_array(text_file)
    print(data.shape)
    tensor = tf.convert_to_tensor(data, dtype=tf.float32)
    menu_model(tensor)

