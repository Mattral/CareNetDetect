import numpy as np
import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image

# Constants for model paths
CANCER_MODEL_PATH = 'models/cancer_model.h5'
TUBERCULOSIS_MODEL_PATH = 'models/tuberculosis_model.hdf5'
PNEUMONIA_MODEL_PATH = 'models/pneumonia_model.h5'
COVID_MODEL_PATH = 'models/covid_model.h5'

# Constants for class labels
CANCER_CLASS_LABELS = ['Benign', 'Malignant', 'Normal']
TUBERCULOSIS_CLASS_LABELS = ['Normal', 'Tuberculosis']
PNEUMONIA_CLASS_LABELS = ['Normal', 'Pneumonia']
COVID_CLASS_LABELS = ['Covid', 'Normal']

# Common preprocessing and prediction function
def preprocess_and_predict(model, class_labels, image_file, target_size, color_mode=None, scale_factor=1.0):
    try: 
        img = image.load_img(image_file, target_size=target_size, color_mode=color_mode)
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / scale_factor
        pred = model.predict(img_array)
        predicted_class = class_labels[np.argmax(pred)]
        confidence = round(100 * np.max(pred), 2)
        return predicted_class, confidence
    
    except ValueError:
        img = image.load_img(image_file, target_size=(150, 150))
        img = image.img_to_array(img)
        img = img / 255.0
        img = np.expand_dims(img, axis=0)

        prediction = model.predict(img)
        predicted_class = class_labels[int(np.round(prediction[0][0]))]
        confidence = ""

        return predicted_class, confidence

def cancer_page():
    st.title("Cancer Detection System")
    uploaded_file = st.file_uploader("Upload chest x-ray image here...", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        model = tf.keras.models.load_model(CANCER_MODEL_PATH)
        predict_button = st.button("ㅤㅤPredictㅤㅤ")
        if predict_button:
            predicted_class, confidence = preprocess_and_predict(model, CANCER_CLASS_LABELS, uploaded_file, (256, 256), 'grayscale', 255.0)
            st.info(f"""
                    ##### Predicted Class: **{predicted_class}**
                    ##### Confidence: {confidence}%
                    """)


def covid_page():
    st.title("Covid Detection System")
    uploaded_file = st.file_uploader("Upload chest x-ray image here...", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        model = tf.keras.models.load_model(COVID_MODEL_PATH)
        predict_button = st.button("ㅤㅤPredictㅤㅤ")
        if predict_button:
            predicted_class, confidence = preprocess_and_predict(model, COVID_CLASS_LABELS, uploaded_file, (150, 150), 'grayscale', 255.0)
            st.info(f"""
                    ##### Predicted Class: **{predicted_class}**
                    ##### Confidence: {confidence}%
                    """)


def pneumonia_page():
    st.title("Pneumonia Detection System")
    uploaded_file = st.file_uploader("Upload chest x-ray image here...", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        model = tf.keras.models.load_model(PNEUMONIA_MODEL_PATH)
        predict_button = st.button("ㅤㅤPredictㅤㅤ")
        if predict_button:
            predicted_class, confidence = preprocess_and_predict(model, PNEUMONIA_CLASS_LABELS, uploaded_file, (256, 256), 'grayscale', 259.0)
            st.info(f"""
                    ##### Predicted Class: **{predicted_class}**
                    ##### Confidence: {confidence*2}%
                    """)

def tuberculosis_page():
    st.title("Tuberculosis Detection System")
    uploaded_file = st.file_uploader("Upload chest x-ray image here...", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        model = tf.keras.models.load_model(TUBERCULOSIS_MODEL_PATH)
        predict_button = st.button("ㅤㅤPredictㅤㅤ")
        if predict_button:
            predicted_class, confidence = preprocess_and_predict(model, TUBERCULOSIS_CLASS_LABELS, uploaded_file, (224, 224), 'grayscale', 255.0)
            st.info(f"""
                    ##### Predicted Class: **{predicted_class}**
                    ##### Confidence: {confidence}%
                    """)
