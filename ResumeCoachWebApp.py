import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import openai
import os

st.title("Resume Coach Web Application")
st.write("Hello, Srinivasa Yanaparti")

openai.api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model_name="gpt-4", temperature=0.5)

def process_text(text):
    # Add your text processing logic here
    # For example, let's convert text to uppercase
    return text.upper()

#st.title("Text Processing App")
#text_input = st.text_area("Enter your Resume in text format")
resume_input = st.text_area("Enter your Resume in text format")
job_posting_input = st.text_area("Enter your job posting")
# user_input = st.text_input("Enter your text for the LLM:")

# def summarize_resume(resume_text):
#     # Add your text processing logic here
#     # For example, let's convert text to uppercase
#     resume_summary_prompt = PromptTemplate(
#     input_variables=["topic"],
#     template="Your task is to provide 10  line summary of : {topic}"
#     )

#     resume_summary_chain = LLMChain(llm=llm, prompt=resume_summary_prompt)
#     resume_summary_response = resume_summary_chain.run(resume_text)

#     return resume_summary_response

summary_prompt = PromptTemplate(
     input_variables=["topic"],
     template="Your task is to provide 10  line summary of : {topic}"
)

summary_chain = LLMChain(llm=llm, prompt=summary_prompt)
resume_summary_response = summary_chain.run(resume_input)
job_posting_summary_response = summary_chain.run(job_posting_input)

resume_coach_prompt = PromptTemplate(
    input_variables=["topic", "job_posting_summary_response"],
    template="Review the provided resume : {topic} and the job description: {job_posting_summary_response}. is this resume best fit for the job description answer in yes or no?"
)

resume_coach_chain = LLMChain(llm=llm, prompt=resume_coach_prompt)
# resume_coach_response = resume_coach_chain.run(resume_input)
resume_coach_response = resume_coach_chain.invoke({"topic": resume_summary_response, "job_posting_summary_response": job_posting_summary_response})

if st.button("Generate Resume Coaching"):
    coaching_report = process_text(resume_input)
    st.write("Coaching Report:")
    st.write(coaching_report)


resume_question_input = st.text_input("If you have any question? Enter Here")
if st.button("Click for Answer"):
    ans_report = process_text(resume_question_input)
    st.write(f"Q:{resume_question_input}")
    st.write(ans_report)

# if st.button("resume summary"):
#     st.write("Resume Summary:")
#     st.write(resume_summary_response)

# if st.button("Job Posting Summary"):
#     st.write("Job Posting Summary:")
#     st.write(job_posting_summary_response)

if st.button("Resume Advice"):
    st.write("Resume Advice:")
    st.write(resume_coach_response)

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