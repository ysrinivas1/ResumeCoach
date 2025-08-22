import streamlit as st
import openai
import os

st.title("Resume Coach Web Application")
st.write("Hello, Srinivasa Yanaparti")

openai.api_key = os.getenv("OPENAI_API_KEY")

def process_text(text):
    # Add your text processing logic here
    # For example, let's convert text to uppercase
    return text.upper()

#st.title("Text Processing App")
#text_input = st.text_area("Enter your Resume in text format")
resume_input = st.text_area("Enter your Resume in text format")
job_posting_input = st.text_area("Enter your job posting")
# user_input = st.text_input("Enter your text for the LLM:")

def summarize_resume(resume):
    # Add your text processing logic here
    # For example, let's convert text to uppercase
    return resume.upper()

if st.button("Generate Resume Coaching"):
    coaching_report = process_text(resume_input)
    st.write("Coaching Report:")
    st.write(coaching_report)


resume_question_input = st.text_input("If you have any question? Enter Here")
if st.button("Click for Answer"):
    ans_report = process_text(resume_question_input)
    st.write(f"Q:{resume_question_input}")
    st.write(ans_report)

if st.button("resume summary"):
    resume_summary = summarize_resume(resume_input)
    st.write("Resume Summary:")
    st.write(resume_summary)

# if st.button("Process Text"):
#     processed_text = process_text(user_input)
#     st.write("Processed Text:")
#     st.write(processed_text)

# if st.button("Get LLM Response"):
#     if user_input:
#         response = openai.chat.completions.create(
#             model="gpt-4",  # Specify the GPT-4 model
#             messages=messages,
#             temperature=0.7,  # Adjust creativity (0.0 to 1.0)
#             max_tokens=150,   # Set the maximum number of tokens in the response
#             frequency_penalty=0.0 # Adjust repetition
#         )
# #        chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": user_input}])
# #        llm_response = chat_completion.choices[0].message.content
#         llm_response = response.choices[0].message.content

#         st.write("LLM Response:")
#         st.write(llm_response)
#     else:
#         st.warning("Please enter some text.")