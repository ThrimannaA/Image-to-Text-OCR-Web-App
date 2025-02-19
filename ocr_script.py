import streamlit as st
import pytesseract
from PIL import Image

# Set Tesseract-OCR path 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

st.title("🖼️ Image to Text OCR Web App")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)  

    text = pytesseract.image_to_string(image)
    
    st.subheader("Extracted Text:")
    st.text_area("", text, height=300)

    st.download_button(label="Download Text", data=text, file_name="extracted_text.txt")









