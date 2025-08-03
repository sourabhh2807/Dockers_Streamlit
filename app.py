import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# Title and Markdown
st.title("Sourabh's Streamlit App")
st.markdown("**Streamlit** is an awesome framework for building interactive apps.")

# Text Input
name = st.text_input('Enter your name')
st.write(f'Hello!')

# Display an image
image = Image.open('a35d584c28c6f5a03536b1ffc3783994.jpg')
st.image(image, caption='Streamlit Example', use_container_width=True)

# Display a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
st.dataframe(df)

# Display a Plotly Chart
fig = px.line(df, x='Name', y='Age', title='Age of Individuals')
st.plotly_chart(fig)

# Display a Matplotlib Plot
x = np.linspace(0, 10, 100)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)

# File uploader
uploaded_file = st.file_uploader("Upload an image")
if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Image', use_container_width=True)

# Slider for selecting age
age = st.slider('Select your age', 18, 100, 25)
st.write(f'Your age is {age}')

