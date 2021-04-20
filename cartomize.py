import cv2
import numpy as np
import streamlit as st
from PIL import Image
import os


def cartomize():

    st.header("= Turn Photo into Cartoon =")
    st.write("------------------------------")

    def read_file(filename):
        img = cv2.imread(filename)
        # cv2_imshow(img)
        return img

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
        #img_file2 = "D:/cartoomize/uploaded_image/kiese12.jpg"

        # img = st.file_uploader("Upload image : ", type=['jpg', 'png', 'jpg'])
        st.image(image_file, use_column_width=True)
        st.write(img_file)

        def edge_mask(img, line_size, blur_value):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray_blur = cv2.medianBlur(gray, blur_value)
            edges = cv2.adaptiveThreshold(
                gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, line_size, blur_value)
            return edges

        def color_quantization(img, k):
            # Transform the image
            data = np.float32(img).reshape((-1, 3))

            # Determine criteria
            criteria = (cv2.TERM_CRITERIA_EPS +
                        cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)

            # Implementing K-Means
            ret, label, center = cv2.kmeans(
                data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
            center = np.uint8(center)
            result = center[label.flatten()]
            result = result.reshape(img.shape)
            return result

        img = read_file(img_file)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        if st.checkbox("Set Edge Mask"):
            line_size = st.sidebar.slider('line_size', 3, 15)
            blur_value = st.sidebar.slider('blur_value', 3, 15)
            edges = edge_mask(img, line_size, blur_value)
            # cv2_imshow(edges)
            st.image(edges, use_column_width=True)

        if st.checkbox("Set Color Quantization"):
            total_color = st.sidebar.slider('total_color', 1, 15)
            img = color_quantization(img, total_color)
            st.image(img, use_column_width=True)

        if st.checkbox("Blur Catoonize Image"):
            blurred = cv2.bilateralFilter(
                img, d=7, sigmaColor=200, sigmaSpace=200)
            st.image(blurred, use_column_width=True)
        if st.button("Save Cartoonize Image"):
            PIL_image = Image.fromarray(blurred.astype('uint8'), 'RGB')
            imd_save = "rlt_"+file_details['FileName']
            PIL_image.save("result/"+imd_save)
            st.write('cartoonize image saved !!!')
            st.balloons()
