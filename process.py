import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
from load_dict import load_dict
def menu_model(data):
    model = st.selectbox('Select the Model', ['English', 'Tamil', 'Telugu'])
    if model == 'English':
        # Load the model
        st.subheader('English Model')
        model = tf.keras.models.load_model('./models/model_weights-english.h5')
        label = np.load('./labels/labelsCorrect.npy')
        label_dict = load_dict(label)
        st.divider()
        if st.button('Predict'):
            with st.spinner('Predicting...'):
                # Predict   
                pred = model.predict(np.expand_dims(data, axis=0))
                pred = np.argmax(pred, axis=1)
                pred = label_dict[pred[0]]
            st.success('Predicted word : '+ pred)
    elif model == 'Tamil':
        # Load the model
        st.subheader('Tamil Model')
        model = tf.keras.models.load_model('./models/model_weights-tamil.h5')
        label = np.load('./labels/labelsCorrect-tamil.npy')
        label_dict = load_dict(label)
        st.divider()
        if st.button('Predict'):
            with st.spinner('Predicting...'):
                # Predict   
                pred = model.predict(np.expand_dims(data, axis=0))
                pred = np.argmax(pred, axis=1)
                pred = label_dict[pred[0]]
            st.success('Predicted word : '+ pred)

    else:
        # Load the model
        st.subheader('Telugu Model')
        model = tf.keras.models.load_model('./models/model_weights-telugu.h5')
        label = np.load('./labels/labelsCorrect-telugu.npy')
        label_dict = load_dict(label)
        st.divider()
        if st.button('Predict'):
            with st.spinner('Predicting...'):
                # Predict   
                pred = model.predict(np.expand_dims(data, axis=0))
                pred = np.argmax(pred, axis=1)
                pred = label_dict[pred[0]]
            st.success('Predicted word : '+ pred)