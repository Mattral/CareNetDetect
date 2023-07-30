from PIL import Image
from config import PROJECT_BACKGROUND, PROJECT_GOALS, PROJECT_PROBLEM
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Omdena Myanmar", page_icon="🇲🇲", initial_sidebar_state="expanded")
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

css_style = {
    "icon": {"color": "white"},
    "nav-link": {"--hover-color": "grey"},
    "nav-link-selected": {"background-color": "#4ABF7E"},
}

# Loading assets
img_banner = Image.open("assets/images/banner.png")
img_logo = Image.open("assets/images/omdena-logo.png")

selected = option_menu(
    menu_title=None,
    options=["Home", "Models", "About", "Contributors"],
    icons=["Home", "gear", "info-circle", "people"],
    styles=css_style,
    orientation="horizontal")


def models():
    with st.sidebar:
        st.write("<br><br><br>", unsafe_allow_html=True)
        st.image(img_logo)
        st.write("<br><br><br>", unsafe_allow_html=True)
        selected = option_menu(
            menu_title=None,
            # options=["Home", "Covid Detection Model", "About", "Contributors"],
            options=["Covid Detection", "Tuberculosis Detection", "Pneumonia Detection",
                     "Cancer Detection"],
            icons=["virus2", "capsule", "lungs", "prescription2"],
            styles=css_style)

    # ------------------------- MODELS -------------------------
    def covid_model():
        st.write("""<h1>Covid Detection System</h1>""", unsafe_allow_html=True)
        uploaded_image = st.file_uploader(label="Upload chest x-ray image here", type=['jpg', 'png'])
        if uploaded_image:
            st.image(uploaded_image)

    def tuberculosis_model():
        st.write("""<h1>Tuberculosis Detection System</h1>""", unsafe_allow_html=True)
        uploaded_image = st.file_uploader(label="Upload chest x-ray image here", type=['jpg', 'png'])
        if uploaded_image:
            st.image(uploaded_image)

    def pneumonia_model():
        st.write("""<h1>Pneumonia Detection System</h1>""", unsafe_allow_html=True)
        uploaded_image = st.file_uploader(label="Upload chest x-ray image here", type=['jpg', 'png'])
        if uploaded_image:
            st.image(uploaded_image)

    def cancer_model():
        st.write("""<h1>Cancer Detection System</h1>""", unsafe_allow_html=True)
        uploaded_image = st.file_uploader(label="Upload chest x-ray image here", type=['jpg', 'png'])
        if uploaded_image:
            st.image(uploaded_image)

    if selected == "Covid Detection":
        covid_model()
    elif selected == "Tuberculosis Detection":
        tuberculosis_model()
    elif selected == "Pneumonia Detection":
        pneumonia_model()
    elif selected == "Cancer Detection":
        cancer_model()


def home_page():
    st.write(f"""# Detection from Chest X-ray Images using Deep Learning""", unsafe_allow_html=True)
    st.image(img_banner)

    st.write(PROJECT_PROBLEM, unsafe_allow_html=True)
    st.write(PROJECT_GOALS, unsafe_allow_html=True)


def about_page():
    st.write(PROJECT_BACKGROUND, unsafe_allow_html=True)


def contributors_page():
    st.success("""Thankyou everyone""")


if selected == "Home":
    home_page()

elif selected == "Models":
    models()

elif selected == "About":
    about_page()

elif selected == "Contributors":
    contributors_page()
