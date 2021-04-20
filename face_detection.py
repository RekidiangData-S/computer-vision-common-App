import streamlit as st
import os
from PIL import Image
import cv2
import numpy as np


def read_file(filename):
    img = cv2.imread(filename)
    # cv2_imshow(img)
    return img


def face_detection():
    st.header("= Face Detection =")
    st.write("------------------------------")

    image_file = st.file_uploader(
        "Upload image : ", type=['jpg', 'png', 'jpg'])
    if image_file is not None:
        file_details = {"FileName": image_file.name,
                        "FileType": image_file.type}
        st.write(file_details)
        st.write(type(file_details))

        # @ save image
        with open(os.path.join("uploaded_image", image_file.name), "wb") as f:
            f.write(image_file.getbuffer())

    img_file = "uploaded_image/" + file_details['FileName']

    if st.button('See Original Image'):

        original = Image.open(img_file)
        st.image(original, use_column_width=True)

    image2 = cv2.imread(img_file)

    face_cascade = cv2.CascadeClassifier(
        "haar-cascade-files/haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(image2)
    print(f"{len(faces)} faces detected in the image.")
    for x, y, width, height in faces:

        cv2.rectangle(image2, (x, y), (x + width, y + height),
                      color=(255, 0, 0), thickness=2)

    cv2.imwrite(img_file, image2)

    st.image(image2, use_column_width=True, clamp=True)
