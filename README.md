# Image Converter

This is a simple **image converter web app** built using Streamlit. It allows users to upload an image, choose a different format, and download the converted image — all in a few clicks!

## Features

- Supports popular image formats: **PNG, JPEG, JFIF, BMP**.
- Displays the uploaded image and its original format.
- Converts images to the desired format.
- Downloads the converted image directly from the browser.

## Installation

To get started with this app, follow these steps:

### Prerequisites

- Python 3.x installed on your system.
- The following Python packages:
  - `streamlit`
  - `Pillow`

### Install the required packages

Run the following command to install the necessary packages:

```bash
pip install streamlit pillow
```

## Usage
- Clone the repository or download the code.
- Run the following command to start the Streamlit app:

```bash
streamlit run app.py
```
The app will open in your default browser. You can now upload an image, select the desired output format, and download the converted file.

## Code Overview
### Main Code (imgconvrtr_ui.py)
```python
import streamlit as st
from imgconvrtr import convert_img_format
from PIL import Image

# Webpage setup
st.set_page_config(page_title="Image Convrtr")
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

    # Show original image format
    st.write(f"Original format: {img.format}")

    # Output format selection
    format_options = ["PNG", "JPEG", "JFIF", "BMP"]
    output_format = st.selectbox("Choose output format", format_options)

    # Convert the image
    if img.format != output_format:
        if st.button("Convert"):
            converted_img = convert_img_format(uploaded_file, output_format.lower())
            st.write(f"Image converted to {output_format}")

            # Download button
            st.download_button(
                label=f"Download as {output_format}",
                data=converted_img,
                file_name=f"image.{output_format.lower()}",
                mime=f"image/{output_format.lower()}"
            )
    else:
        st.write("Select a different format... Yo!")
```
### Image Conversion Function (imgconvrtr.py)
```python
from PIL import Image
import io

# Function to convert image format
def convert_img_format(image_file, frmat):
    with Image.open(image_file) as img:
        output_img = io.BytesIO()
        img.save(output_img, format=frmat.upper())
        output_img.seek(0)
        return output_img
```
