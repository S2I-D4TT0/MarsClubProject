import fitz  # PyMuPDF for PDF
import docx  # python-docx for DOCX
import os
import re

def extract_text_from_file(file):
    filename = file.name.lower()

    if filename.endswith(".pdf"):
        return extract_text_from_pdf(file)

    elif filename.endswith(".docx"):
        return extract_text_from_docx(file)

    elif filename.endswith(".txt"):
        return extract_text_from_txt(file)

    else:
        return {"text": "", "tables": [], "links": [], "doc_metadata": "Unknown format"}

def extract_text_from_pdf(file):
    import fitz  # PyMuPDF
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    tables = []
    links = []
    for page in doc:
        text += page.get_text()
        links.extend([link["uri"] for link in page.get_links() if "uri" in link])
        tables.append(page.get_text("dict")) 

    return {
        "text": text,
        "tables": [],  # Implementing table extraction
        "links": links,
        "doc_metadata": doc.metadata
    }

def extract_text_from_docx(file):
    doc = docx.Document(file)
    links=[]
    for rel in doc.part._rels:
        rel_obj = doc.part._rels[rel]
        if "hyperlink" in rel_obj.reltype:
            links.append(rel_obj.target_ref)
            
    text = "\n".join([p.text for p in doc.paragraphs])
    # Also catch raw URLs in text (fallback)
    links += re.findall(r'https?://\S+', text)
    links = list(set(links))  # Remove duplicates
    
    return {
        "text": text,
        "tables": [],  
        "links": links,
        "doc_metadata": "No metadata for DOCX"
    }

def extract_text_from_txt(file):
    text = file.read().decode("utf-8")
    # Extract links using regex
    links = re.findall(r'https?://\S+', text)
    return {
        "text": text,
        "tables": [],
        "links": links,
        "doc_metadata": "No metadata for TXT"
    }
