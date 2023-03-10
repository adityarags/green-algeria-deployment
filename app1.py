import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


def app():
    st.title("π± Omdena Algeria Chapter π±")
    img=Image.open("images/omdena_algeria.png")
#     newsize=(280,300)
#     img1=img.resize(newsize)
    st.write("\n")
    st.write("\n")
    st.markdown("""Collaborate, Learn, Build, Grow """)
    st.subheader("Omdena Algeria Local Chapter for both Part: 1 and Part: 2.")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.image(img,use_column_width='always')
    st.write("\n")
    st.header("π€Project Background")
    st.markdown(""" 
                    Located in North Africa, Algeria has sought to support agriculture because of its potential in this sector. Indeed, it has put in place several agricultural policies and the objective was to achieve food security by substituting local production for imported products. One of the most important goals is the development of modern and sustainable protected greenhouse cultivation in Algeria. Managing greenhouses by means of AI technologies allows growers to be more focused on their crops and provides control at their fingertips. 
                    Proposed by the University of Ain Temouchent, Algeria, this project aims to develop ML models for the management of intelligent greenhouses.""")
    st.write("\n")
    st.header("πRepository")
    st.markdown("""
        This repository is divided into Part 1 and Part 2 respectively.
        - Languages : Python
        - Domains : Machine Learning, Deep Learning, Computer Vision, Web Development & Frameworks, Internet Of Things
        """)
    st.write("\n")
    st.header("πDirectory Structure")
    st.code("""
        βββ main
        β   βββ Part 1
        β     βββ Team-1 Water Level Forecasting
        β     βββ Team-2 Crop Recommendation System
        β     βββ Team-3 Wheat Detection
        β     βββ Team-4 Pest Detection
        β     βββ Team-5-Indoor Temperature and Humidity Prediction
        β     βββ Team-6-Plant Species Identification
        β   βββ Part 2 
        β     βββ Subproject1- Indoor Climate Factors
        β     βββ Subproject2- Diseases and Pests Detection
        β     βββ Subproject3- Recommendation Systems
        β     βββ README.md
        βββ License
        βββ README.md
        βββ .gitignore
        """)
    st.write("\n")
    st.header("πWebsite")
    link='check out this [link](https://omdena.com/local-chapters/algeria-local-chapter/)'
    st.markdown(link,unsafe_allow_html=True)
    st.markdown("Β© 2022 Omdena")

    
