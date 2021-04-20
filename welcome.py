import streamlit as st


def welcome():

    st.markdown("Computer Vision App with Streamlit")
    st.write('-------')

    st.subheader('A simple app that shows different image processing algorithms. You can choose the options'
                 + ' from the left. I have implemented only a few to show how it works on Streamlit. ' +
                 'You are free to add stuff to this app.')
