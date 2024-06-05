# import streamlit as st
# from PIL import Image
# from ocr_tamil.ocr import OCR

# # Initialize the OCR model
# ocr = OCR(detect=True)

# def predict_text(image):
#     """
#     Predict text from the given image using the OCR model.
#     """
#     text_list = ocr.predict(image)
#     return text_list

# def main():
#     st.title("Tamil OCR")

#     # Upload image
#     uploaded_image = st.file_uploader("Upload Image", type=['jpg', 'jpeg', 'png'])

#     if uploaded_image is not None:
#         # Display the uploaded image
#         image = Image.open(uploaded_image)
#         st.image(image, caption='Uploaded Image', use_column_width=True)

#         # Predict text
#         if st.button("Predict Text"):
#             text_list = predict_text(image)

#             # Display the predicted text
#             for item in text_list:
#                 st.write(" ".join(item))

# if __name__ == '__main__':
#     main()

import streamlit as st
from PIL import Image
from ocr_tamil.ocr import OCR
import io

def predict_text(image):
    ocr = OCR(detect=True)
    # Predict text
    text_list = ocr.predict(image)
    return text_list

def main():
    st.title("Tamil OCR App")
    st.write("Upload an image containing Tamil text and click the 'Predict' button.")

    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Predict"):
            # Convert PIL image to bytes
            image_bytes = io.BytesIO()
            image.save(image_bytes, format='JPEG')
            image_bytes = image_bytes.getvalue()

            # Pass image bytes to the predict_text function
            text_list = predict_text(image_bytes)
            for item in text_list:
                st.write(" ".join(item))

if __name__ == "__main__":
    main()

