import streamlit as st
from PIL import Image

st.header("Vitamin Deficiency Detection")
sb = st.sidebar
sb.subheader('Upload your Image')
img = sb.file_uploader('Upload Skin, Nail, Toungue, or Eye Image',type=['png','jpg','jpeg'])
sb.write('Powered by AI and Streamlit')

if img:
    st.image(img,'Uploaded Image')
    btn = st.button("Find Deficiency")
    if btn:
        gray_image = Image.open(img).convert("L")
        st.image(gray_image,'Processed Image')

