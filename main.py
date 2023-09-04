import base64
from PIL import Image
from config import PROJECT_BACKGROUND, PROJECT_GOALS, PROJECT_PROBLEM
import streamlit as st
from streamlit_option_menu import option_menu
from models import tuberculosis_page, cancer_page, pneumonia_page


st.set_page_config(page_title="Omdena Myanmar", page_icon="🇲🇲", initial_sidebar_state="expanded")


def change_bg():
    @st.cache_data()
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    def set_png_as_page_bg(png_file):
        bin_str = get_base64_of_bin_file(png_file)
        page_bg_img = '''
        <style>
        .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: scroll; # doesn't work
        }
        </style>
        ''' % bin_str

        st.markdown(page_bg_img, unsafe_allow_html=True)

    set_png_as_page_bg('assets/background.webp')


change_bg()

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
img_banner = Image.open("assets/banner.png")
img_logo = Image.open("assets/logo.png")

selected = option_menu(
    menu_title=None,
    options=["Home", "Models", "About", "Contributors"],
    icons=["house", "gear", "info-circle", "people"],
    styles=css_style,
    orientation="horizontal")


def models():
    with st.sidebar:
        l_padding, mid, r_padding = st.columns((1, 8, 2))
        with l_padding:
            st.empty()
        with mid:
            st.image(img_logo)
        with r_padding:
            st.empty()

        st.write("<br><br>", unsafe_allow_html=True)
        selected = option_menu(
            menu_title=None,
            options=["Covid", "Tuberculosis", "Pneumonia", "Cancer"],
            icons=["virus2", "capsule", "lungs", "prescription2"],
            styles=css_style)

    # ------------------------- MODELS -------------------------
    def covid_page():
        st.write("""<h1>Covid Detection System</h1>""", unsafe_allow_html=True)
        uploaded_image = st.file_uploader(label="Upload chest x-ray image here", type=['jpg', 'png'])
        if uploaded_image:
            st.image(uploaded_image)

    if selected == "Covid":
        covid_page()
    elif selected == "Tuberculosis":
        tuberculosis_page()
    elif selected == "Pneumonia":
        pneumonia_page()
    elif selected == "Cancer":
        cancer_page()


def home_page():
    st.write(f"""# Detection Chest X-ray Images using Deep Learning""", unsafe_allow_html=True)
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
