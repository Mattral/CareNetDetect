import streamlit as st
import torch
from fastai.vision.all import *
from PIL import Image

# Load the model
# model_path = 'models/pneumonia.pth'
#
# # Define the path to your test data
# test_data_path = '/content/drive/MyDrive/split_data_balanced/test'
#
# # Create DataLoaders
# dls = ImageDataLoaders.from_folder(test_data_path, train='normal', valid_pct=0.2, item_tfms=Resize(224))
#
# learn = cnn_learner(dls, resnet34)
# learn.load(model_path)

# Set up Streamlit
st.title("Pneumonia Classification")
st.write("Upload a lung X-ray image to classify whether it has pneumonia or not.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)

    # Preprocess the image
    img = PILImage.create(uploaded_file)

    # Make a prediction
    pred, pred_idx, probs = learn.predict(img)
    prediction_class = learn.dls.vocab[pred_idx]

    # Display the prediction
    st.write(f"Prediction: {prediction_class} (Probability: {probs[pred_idx]:.2%})")
