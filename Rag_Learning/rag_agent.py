from groq import Groq
from dotenv import load_dotenv
import os
from pinecone import pinecone
import streamlit as st
from vector import embed_text,vector_index

load_dotenv()

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("A very cool Rag app to answer your Question for students")
st.subheader("Ask me anything about datascience")

user_query =st.text_input("Enter your question here")
submit_button = st.button("Submit")

if submit_button and user_query:
    vector =embed_text(user_query)
    query_response = vector_index.query(
        vector=vector,
        top_k = 1,
        include_metadata = True
    )
    
    similar_documents =""
    for match in query_response["matches"]:
        similar_documents += match["metadata"]["text"]+"\n\n"
        
        
system_prompt = {
    "role":"system",
    "content":f"""you are a helpful assistant for student.
use the following context to answer the question.
Context:{similar_documents}
for general question not related to datascience student,polietly infrorm them  that you don't have information."""
}
user_promt = {
    "role":"user",
    "content":user_query
}

llm_response =groq_client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[system_prompt,user_promt],
    max_tokens=1024,
    temperature=0.2,
)
llm_answer =llm_response.choices[0].message.content
st.write("Answer")
st.write(llm_answer)