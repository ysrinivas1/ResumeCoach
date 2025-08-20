import streamlit as st

st.title("My Simple Streamlit App")
st.write("Hello, My name is srinivas")

def process_text(text):
    # Add your text processing logic here
    # For example, let's convert text to uppercase
    return text.upper()

st.title("Text Processing App")
text_input = st.text_area("Enter your text")

if st.button("Process Text"):
    processed_text = process_text(text_input)
    st.write("Processed Text:")
    st.write(processed_text)
