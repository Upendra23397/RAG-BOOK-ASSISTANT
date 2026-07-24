import streamlit as st

import os


from utils.file_handler import save_uploaded_file

from ingestion.ingest import create_database

from services.rag import ask_question



st.set_page_config(

    page_title="RAG Book Assistant"

)


st.title(
    "📚 RAG Book Assistant"
)


st.write(
    "Upload PDF and ask questions"
)



uploaded_file = st.file_uploader(

    "Upload PDF",

    type="pdf"

)



if uploaded_file:


    file_path = save_uploaded_file(

        uploaded_file

    )


    st.success(
        "PDF uploaded"
    )


    if st.button(
        "Create Vector Database"
    ):


        with st.spinner(
            "Creating database..."
        ):


            create_database(

                file_path

            )


        st.success(
            "Vector database created"
        )



if os.path.exists(
    "data/chroma_db"
):


    st.divider()


    st.subheader(
        "Ask your book"
    )


    question = st.text_input(
        "Question"
    )


    if question:


        with st.spinner(
            "Thinking..."
        ):


            answer = ask_question(

                question

            )


        st.write(
            "### AI Answer"
        )


        st.write(
            answer
        )