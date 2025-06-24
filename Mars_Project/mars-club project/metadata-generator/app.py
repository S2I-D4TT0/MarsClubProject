import streamlit as st
from extractor import extract_text_from_file
from metadata_gen import llm_generate_metadata, summarize_text


st.title("📄 Structured Document Extractor + Metadata + Summary")


uploaded_file = st.file_uploader("Upload your document", type=["pdf", "docx", "txt"])


if uploaded_file:
    with st.spinner("📤 Extracting document..."):
        st.subheader("If you're not Satisfied, Click again . It may give better results")
        result = extract_text_from_file(uploaded_file)
    
    flg=1
    cnt=0
    for c in result["text"]:
        
        if (c=='.' and cnt<1):
            flg=0
            break
        cnt+=1


    # --- If no meaningful text or links or tables ---
    if (not result["text"].strip() and not result["tables"] and not result["links"]) or flg==0:
        st.warning("⚠️ No readable text found. Try another file or format.")
    else:
        st.success("✅ Extracted Successfully!")

        # --- Display main text ---
        st.subheader("📜 Combined Raw Text")
        st.text_area("Document Text", result["text"][:2000] + ("..." if len(result["text"]) > 2500 else ""), height=200)

        # --- Display tables ---
        if result["tables"]:
            st.subheader("📊 Table-like Data")
            for i, table in enumerate(result["tables"][:50]):
                st.code(table)


        # --- Display links ---
        if result["links"]:
            st.subheader("🔗 Links")
            for link in result["links"]:
                st.write(f"- [{link}]({link})")

        # --- Metadata button ---
        if st.button("🧠 Generate Metadata"):
            with st.spinner("Analyzing..."):
                st.subheader("If you're not Satisfied, Click again . It may give better results")
                metadata = llm_generate_metadata(result["text"])
                pdf_metadata= result["doc_metadata"]
            st.subheader("📋 Metadata")
            st.markdown(metadata)

            st.subheader("📋Document  Metadata")
            st.markdown(pdf_metadata)

        # --- Summary button ---
        if st.button("📝 Summarize Document"):
            with st.spinner("Summarizing..."):

                summary = summarize_text(result["text"][:2500])
            st.subheader("🧾 Summary")
            st.subheader("If you're not Satisfied, Click again . It may give better results")
            st.write(summary)
