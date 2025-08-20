import streamlit as st

st.title("Resume Coach Web Application")
st.write("Hello, My name is Srinivasa Yanaparti")

def process_text(text):
    # Add your text processing logic here
    # For example, let's convert text to uppercase
    return text.upper()

#st.title("Text Processing App")
text_input = st.text_area("Enter your Resume in text format")

if st.button("Process Text"):
    processed_text = process_text(text_input)
    st.write("Processed Text:")
    st.write(processed_text)
