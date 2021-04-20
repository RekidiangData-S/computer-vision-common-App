import streamlit as st
from PIL import Image
import cv2
import numpy as np
from welcome import welcome
from cartomize import cartomize
from face_detection import face_detection
from face_mask_detection import face_mask_detection


def main():
    st.header('Computer Vision App with Streamlit')
    st.image('logo_resized.png', use_column_width=True)

    selected_box = st.sidebar.selectbox(
        'Choose one of the following',
        ('About', 'Turn Photo into Cartoon', 'Age and Genre Recognition', 'Face Detection',
         'Face Mask Detection', 'Object Detection')
    )

    if selected_box == 'About':
        welcome()
    if selected_box == 'Turn Photo into Cartoon':
        cartomize()

    if selected_box == 'Age and Genre Recognition':
        age_and_genre_rec()
    if selected_box == 'Face Detection':
        face_detection()
    if selected_box == 'Face Mask Detection':
        face_mask_detection()
    if selected_box == 'Object Detection':
        object_detection()


if __name__ == "__main__":
    main()
