from langchain_ollama import OllamaLLM
import streamlit as st
from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Define CDP-related keywords
cdp_keywords = ["Segment", "mParticle", "Lytics", "Zeotap", "customer data", "tracking", "event", "API", "SDK", "identity resolution", "audience segmentation"]

# Initialize the Ollama model
model = OllamaLLM(model="llama3.1")

st.title("Ask me anything about CDPs!")

if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input
prompt = st.chat_input("Ask about Segment, mParticle, Lytics, or Zeotap!")

if prompt:
    # Handle extremely long questions (truncate after 500 characters)
    if len(prompt) > 500:
        truncated_prompt = prompt[:500] + "..."
        warning_msg = "**Your question was too long, so it was truncated.**"
        st.session_state.messages.append({"role": "system", "content": warning_msg})
        with st.chat_message("system"):
            st.markdown(warning_msg)
    else:
        truncated_prompt = prompt

    # Display user message
    st.session_state.messages.append({"role": "user", "content": truncated_prompt})
    with st.chat_message("user"):
        st.markdown(truncated_prompt)

    # Check if the question is related to CDPs
    user_embedding = embedding_model.encode(truncated_prompt)
    relevant = any(keyword.lower() in truncated_prompt.lower() for keyword in cdp_keywords)

    if not relevant:
        response = "**I can only answer questions related to Customer Data Platforms (Segment, mParticle, Lytics, Zeotap).**"
    
        with st.chat_message("assistant"):
            st.markdown(response) 

       
        st.session_state.messages.append({"role": "assistant", "content": response})

    else:
        with st.chat_message("assistant"):
            response_placeholder = st.empty()  
            full_response = ""  

            for chunk in model.stream(truncated_prompt):
                full_response += chunk  
                response_placeholder.markdown(full_response) 

            response = full_response

    st.session_state.messages.append({"role": "assistant", "content": response})
