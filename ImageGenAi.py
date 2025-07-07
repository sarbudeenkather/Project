import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
client = genai.Client(api_key="YOUR API KEY")
custom_css = """
    <style>
.st-emotion-cache-13k62yr{
    background: #3944BC;
}
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)
response =" "
# Create empty space on the left and then 3 small columns for the buttons
spacer1, btn1_col, btn2_col, btn3_col = st.columns([5, 1, 1, 1])

with btn1_col:
    if st.button("Home"):
        st.write("Button 1 clicked!")

with btn2_col:
    if st.button("Log in"):
        st.write("Button 2 clicked!")

with btn3_col:
    if st.button("Sign up"):
        st.write("Button 3 clicked!")
col1,col2 = st.columns(2)
with col1:
    st.title("Describer your Image here")
    contents = st.text_area(" ")
    if st.button("Visualize"):
        response = client.models.generate_content(
            model="gemini-2.0-flash-preview-image-generation",
            contents=contents,
            config=types.GenerateContentConfig(
                response_modalities=['TEXT','IMAGE']
            )
        )
        for part in response.candidates[0].content.parts:
            if part.text is not None:
                print(part.text)
            elif part.inline_data is not None:
                image = Image.open(BytesIO((part.inline_data.data)))
                image.save('gemini-native-image.png')
st.title("Showcase of Image Describer ")
image_path = "Demo.png"  # Make sure this path is correct
st.image(image_path, use_container_width=True)

with col2:
    if st.image("gemini-native-image.png"):
        st.write("Your image..")
    else:
        st.write("Waiting for your response..")



