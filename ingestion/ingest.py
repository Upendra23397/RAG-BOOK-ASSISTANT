from ingestion.pdf_loader import load_pdf
from ingestion.text_splitter import split_documents

from services.embeddings import get_embeddings
from services.vectorstore import create_vectorstore

def create_database(file_path):


    documents = load_pdf(
        file_path
    )


    chunks = split_documents(
        documents
    )


    embeddings = get_embeddings()


    vectorstore = create_vectorstore(

        chunks,

        embeddings

    )


    return vectorstore