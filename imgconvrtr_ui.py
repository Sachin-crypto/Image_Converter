import streamlit as st
from imgconvrtr import convert_img_format
from PIL import Image

st.title("Image Converter")
st.write("Convert your images in one _click_")

# File uploader
uploaded_file = st.file_uploader(
    "Upload an image",
    type=["png", "jpg", "jpeg", "jfif", "bmp"]
)

if uploaded_file is not None:
    # Show the uploaded image
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Detect the image format
    st.write(f"Original format: {img.format}")

    # Selecting the output format
    format_options = ["PNG", "JPEG", "BMP", "JFIF"]
    output_format = st.selectbox(
        "Choose output format",
        format_options
    )

    if img.format != output_format:

        # Convert and save the image in-memory
        if st.button("Convert"):
            # Convert image and get the output in-memory file
            converted_img = convert_img_format(
                uploaded_file,
                output_format.lower()
            )
            st.write(f"Image converted to {output_format}")

            # Show the download button for the converted image
            st.download_button(
                label=f"Download as {output_format}",
                data=converted_img,
                file_name=f"image.{output_format.lower()}",
                mime=f"image/{output_format.lower()}"
            )

    else:
        st.write("Select a different format... Yo!")