from PIL import Image
import io


# Function to convert image format and return in-memory binary data
def convert_img_format(image_file, frmat):
    with Image.open(image_file) as img:
        # If converting to JPEG, ensure no transparency
        # if frmat == 'jpeg' and img.mode in ['RGBA', 'P']:
        #     img = img.convert('RGB')

        # Create an in-memory output file (BytesIO) to hold the converted image
        output_img = io.BytesIO()

        # Save the image to this in-memory file
        img.save(output_img, format=frmat.upper())

        # Move the file pointer to the start
        output_img.seek(0)

        return output_img


# if __name__ == "__main__":
#     input_img = "lw.jfif"
#     output_img = "lw1"
#     convert_img_format(input_img, output_img, "png")
