from groq import Groq
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()  # Load from .env

api_Key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_Key)

def llm_generate_metadata(text):
    prompt = f"""
You're an intelligent metadata parser.

Extract structured metadata from the following academic/technical document:

**Return in Markdown Format with fields:**
- **Title:**
- **Subject:**
- **Language:**
- **Author :(if present)**
- **Topic Keywords:**
-**Important Named Entities:**
- **Outline  (at least 3 lines and atmax 6 lines)**

Text:
\"\"\"{text[:500]}\"\"\"
"""
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


def summarize_text(text):
    max_length = max(int(0.8 * len(text)),900)
    prompt = f"""
Summarize the following academic/technical document. Summary must be concise and clear. Should cover each and every point and give result in key 
points and structured way

Document:
\"\"\"{text}\"\"\"

Summary (max {max_length} characters):
"""
    response = client.chat.completions.create(
        model="llama3-70b-8192",
       
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
