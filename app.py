import streamlit as st
from PIL import Image
import base64
import os

# Function to set background image
def set_background(img_file):
    if not os.path.exists(img_file):
        st.error(f"File {img_file} does not exist.")
        return
    
    with open(img_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        
    # Determine MIME type based on file extension
    if img_file.endswith('.jpg') or img_file.endswith('.jpeg'):
        mime_type = 'image/jpeg'
    elif img_file.endswith('.png'):
        mime_type = 'image/png'
    else:
        st.error(f"Unsupported image format for {img_file}.")
        return
    
    css = f"""
    <style>
    .stApp {{
        background-image: url(data:{mime_type};base64,{encoded_string});
        background-size: cover;
        background-position: center;
    }}
    
    /* Ensuring text is visible */
    .main .block-container {{
        padding: 1em;
        margin: 0 auto;
        max-width: 1200px;
        text-align: center;
        color: white;
    }}
    
    /* Optional: Make sidebar transparent */
    .sidebar .sidebar-content {{
        background-color: transparent;
    }}

    /* Heading font and size adjustments */
    .custom-header h1 {{
        font-size: 3em; /* Increase main heading size */
        font-family: 'Arial Black', sans-serif; /* Use a different font */
        font-weight: bold;
        color: #f1f1f1;
    }}
    
    .custom-header h2 {{
        font-size: 2em; /* Increase subheading size */
        font-family: 'Georgia', serif; /* Use a different font */
        color: #f1f1f1;
    }}
    </style>
    """
    
    st.markdown(css, unsafe_allow_html=True)

# Load the background image
set_background("backgroundimage2.jpg")

# Custom header with increased font size and different font styles
st.markdown("<div class='custom-header'><h1>VitaVision</h1></div>", unsafe_allow_html=True)
st.markdown("<div class='custom-header'><h2>Automated Detection of Vitamin Deficiencies through Image Analysis</h2></div>", unsafe_allow_html=True)

# Sidebar configuration
sb = st.sidebar
sb.subheader('Upload your Image')
img = sb.file_uploader('Upload Skin, Nail, Tongue, or Eye Image', type=['png','jpg','jpeg'])


if img:
    st.image(img, caption='Uploaded Image')
    btn = st.button("Find Deficiency")
    if btn:
        gray_image = Image.open(img).convert("L")
        st.image(gray_image, caption='Processed Image')
