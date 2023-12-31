import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

st.title("🦜🔗 Langchain - Blog Outline Generator App")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")


def blog_outline(topic):
    # Instantiate LLM model
    llm = OpenAI(model_name="text-davinci-003", openai_api_key=openai_api_key)
    # Prompt
    template = "As an experienced data scientist and technical writer, generate an outline for a blog about {topic}."
    prompt = PromptTemplate(input_variables=["topic"], template=template)
    prompt_query = prompt.format(topic=topic)
    # Run LLM model
    response = llm(prompt_query)
    # Print results
    return st.info(response)