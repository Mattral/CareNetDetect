import streamlit as st
import easyocr
from huggingface_hub import InferenceClient
import random
import time
from PIL import Image

# Initialize EasyOCR and Huggingface InferenceClient
reader = easyocr.Reader(['en'])
model = "mistralai/Mixtral-8x7B-Instruct-v0.1"
access_token = "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"
client = InferenceClient(model=model, token=access_token)

# Embedded system prompt for AI
system_prompt_text = (
    "You are Doctor's Assistant reporting to patient"
)

# Function to process and send OCR extracted text to AI
def get_medical_ai_response(ocr_text):
    prompt = f"This information is the OCR extracted from Medical Document or Report: {ocr_text}\n\nPlease identify if this is medical related, if it is medical explain in details and if it's not, provide a summary of the content in less than 50 words."
    
    # Send the OCR text to the AI model
    history = []
    history, output = chat_inf(prompt, history, random.randint(1, 1111111111111111), 0.9, 3840, 0.9, 1.0)
    return output

# Function to generate AI responses
def chat_inf(prompt, history, seed, temp, tokens, top_p, rep_p):
    generate_kwargs = dict(
        temperature=temp,
        max_new_tokens=tokens,
        top_p=top_p,
        repetition_penalty=rep_p,
        do_sample=True,
        seed=seed,
    )

    formatted_prompt = format_prompt_mixtral(prompt, history)

    for attempt in range(5):
        try:
            stream = client.text_generation(formatted_prompt, **generate_kwargs, stream=True, details=True, return_full_text=False)
            output = ""
            for response in stream:
                output += response.token.text

            if not output:
                return history, "No response."

            history.append((prompt, output))
            return history, output
            
        except Exception as e:
            print(f"Error: {str(e)}")
            return history, "An error occurred during processing."

# Function to format the prompt for Mixtral model
def format_prompt_mixtral(message, history):
    prompt = "<s>"
    prompt += f"{system_prompt_text}\n\n"  # Add the system prompt

    if history:
        for user_prompt, bot_response in history:
            prompt += f"[INST] {user_prompt} [/INST] {bot_response}</s> "
    prompt += f"[INST] {message} [/INST]"
    return prompt

# Function to process and display OCR text and image
def process_image(uploaded_image):
    image = Image.open(uploaded_image)
    img_array = np.array(image)

    # Perform OCR on the image
    result = reader.readtext(img_array)

    # Extract text
    extracted_text = ""
    for detection in result:
        extracted_text += detection[1] + "\n"

    # Display extracted text and send to AI
    st.subheader("Extracted Text:")
    st.text(extracted_text)

    # Get AI response based on the extracted text
    ai_response = get_medical_ai_response(extracted_text)
    
    # Display AI response
    st.subheader("AI Response:")
    st.text(ai_response)

    # Simply display the image without annotations (no OpenCV)
    st.subheader("Original Image:")
    st.image(image, caption='Uploaded Image', use_column_width=True)

# Main page with Streamlit interface
def contributors_page():
    st.balloons()
    st.write("""<h1 style="text-align: center; color:#FFF6F4;">Ask me about your Medical Documents</h1><hr>
                <p style="text-align:center;">Upload an image to extract text and analyze if it relates to medical documents.</p>
            """, unsafe_allow_html=True)

    uploaded_image = st.file_uploader("Upload an Image", type=['png', 'jpg', 'jpeg'])

    if uploaded_image is not None:
        process_image(uploaded_image)
