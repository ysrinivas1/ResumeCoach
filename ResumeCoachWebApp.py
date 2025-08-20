import streamlit as st
import openai

st.title("Resume Coach Web Application")
st.write("Hello, My name is Srinivasa Yanaparti")

def process_text(text):
    # Add your text processing logic here
    # For example, let's convert text to uppercase
    return text.upper()

#st.title("Text Processing App")
#text_input = st.text_area("Enter your Resume in text format")
user_input = st.text_input("Enter your text for the LLM:")

if st.button("Process Text"):
    processed_text = process_text(user_input)
    st.write("Processed Text:")
    st.write(processed_text)

if st.button("Get LLM Response"):
    if user_input:
        # Replace with your specific LLM API call
        # Example using OpenAI ChatCompletion:
        chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": user_input}])
        llm_response = chat_completion.choices[0].message.content

        st.write("LLM Response:")
        st.write(llm_response)
    else:
        st.warning("Please enter some text.")