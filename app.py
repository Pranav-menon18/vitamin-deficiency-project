import streamlit as st
from PIL import Image

st.header("Vitamin Deficiency Detection")

st.sidebar.subheader('Upload your Image')
img = st.sidebar.file_uploader('Upload Skin, Nail, Toungue, or Eye Image',type=['png','jpg','jpeg'])
st.sidebar.write('Powered by AI and Streamlit')

if img:
    st.image(img,'Uploaded Image')

    if st.button("Find Deficiency"):
        gray_image = Image.open(img).convert("L")
        st.image(gray_image,'Processed Image')

