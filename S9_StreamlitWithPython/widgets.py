import streamlit as st
import pandas as pd

st.title("Streamlit Text Input Example")

name = st.text_input("Enter your name:")

age = st.slider("Select your age:", 0, 100, 25)

st.write(f"Your age is: {age}")

options = ["Python", "JavaScript", "Java", "C++"]
choice = st.selectbox("Select your favorite programming language:", options)
st.write(f"You selected: {choice}")

if name:
    st.write(f"Hello, {name}!") 
    
data = {
    "Name": [name],
    "Age": [age],
    "Favorite Language": [choice]
}

df = pd.DataFrame(data)
df.to_csv("user_data.csv")
st.write(df)

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
    
if st.button("Click me"):
    #https://streamlit.io/
    st.write("Button clicked!")
