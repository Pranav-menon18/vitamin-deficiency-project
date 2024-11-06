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
    
    /* Add this to ensure text is visible */
    .main .block-container {{
        padding: 1em;
        margin: 0 auto;
        max-width: 1200px;
        text-align: center;
        color: white; /* Change text color if needed */
    }}
    
    /* Optional: Make sidebar transparent */
    .sidebar .sidebar-content {{
        background-color: transparent;
    }}
    
    /* Optional: Adjust header styles */
    .main .block-container h1 {{
        font-size: 2em; /* Adjust font size */
    }}
    
    .main .block-container h2 {{
        font-size: 1.5em; /* Adjust font size */
    }}
    
    </style>
    """
    
    st.markdown(css, unsafe_allow_html=True)

# Load the background image
set_background("backgroundimage.jpg")

# Create a custom header
st.markdown("<h1 style='text-align: center; color: white;'>VitaVision</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: white;'>Automated Detection of Vitamin Deficiencies through Image Analysis</h2>", unsafe_allow_html=True)

# Sidebar configuration
sb = st.sidebar
sb.subheader('Upload your Image')
img = sb.file_uploader('Upload Skin, Nail, Tongue, or Eye Image', type=['png','jpg','jpeg'])
sb.write('Powered by AI and Streamlit')

if img:
    st.image(img,'Uploaded Image')
    btn = st.button("Find Deficiency")
    if btn:
        gray_image = Image.open(img).convert("L")
        st.image(gray_image,'Processed Image')