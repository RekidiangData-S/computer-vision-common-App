import streamlit as st
from PIL import Image, ImageEnhance
import numpy as np
import cv2
import os


def read_file(filename):
    img = cv2.imread(filename)
    # cv2_imshow(img)
    return img


def face_mask_detection():
    pass
