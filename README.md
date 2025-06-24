# MarsClubProject
Mars Club GenAI Project
# 🧠 Document Metadata & Summary Extractor

This Streamlit app extracts text, tables, and links from uploaded documents (PDF, DOCX, TXT), and uses a Language Model (Groq API) to generate structured metadata and a concise summary.

---

## 🚀 Features

- 📄 Upload and parse `.pdf`, `.docx`, `.txt` files
- 📜 Extract raw text, links, and tables
- 🧠 Generate metadata using Groq API
- 📝 Summarize the document content
- 🔐 Uses `.env` for secure API key management

---

## 🧰 Tech Stack

- [Streamlit](https://streamlit.io)
- Python 3.8+
- `pymupdf` for PDF parsing
- `python-docx` for DOCX parsing
- `re`, `os`, `dotenv` for environment handling
- Groq LLM API for metadata and summary

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/S2I-D4TT0/MetadataGenerator.git
cd MetadataGenerator
## For Installing dependencies 
pip install -r requirements.txt
## use your own  groq api key here in .env file 
GROQ_API_KEY=your_groq_api_key_here

and then run python -m streamlit run app.py


