import time
import numpy as np
import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image

# Load the model outside the main function to load it only once
model = tf.keras.models.load_model("models/tuberculosis.hdf5")
class_names = ['Normal', 'Tuberculosis']


@st.cache_data()
def preprocess_and_predict(image_file):
    img = image.load_img(image_file, target_size=(224, 224))
    img = image.img_to_array(img)
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    prediction = model.predict(img)
    predicted_class = class_names[np.argmax(prediction)]
    confidence = round(100 * np.max(prediction), 2)
    return predicted_class, confidence


def tuberculosis_page():
    st.title("Tuberculosis Detection System")

    uploaded_file = st.file_uploader("Upload chest x-ray image here...", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
        st.write("")

        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.022)
            my_bar.progress(percent_complete + 1, text=progress_text)

        predicted_class, confidence = preprocess_and_predict(uploaded_file)

        st.write(f"Predicted Class: **{predicted_class}**")
        st.write(f"Confidence: {confidence}%")


