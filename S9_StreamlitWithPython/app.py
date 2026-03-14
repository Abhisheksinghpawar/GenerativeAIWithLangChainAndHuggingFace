import streamlit as st
import pandas
import numpy as np

##Title of the application
st.title("Hello Streamlit")

##Display a simple text
st.write("This is a simple text")

##Create a dataframe
df = pandas.DataFrame({
    "Column 1": [1, 2, 3, 4],
    "Column 2": [10, 20, 30, 40]})

##Display the dataframe
st.write("This is a dataframe:")
st.write(df)

##Create a line chart
st.write("This is a line chart:")
chart_data = pandas.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.line_chart(chart_data)