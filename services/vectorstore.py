from langchain_community.vectorstores import Chroma

from config.settings import CHROMA_PATH



def create_vectorstore(
        chunks,
        embeddings
):

    vectorstore = Chroma.from_documents(

        documents=chunks,

        embedding=embeddings,

        persist_directory=CHROMA_PATH

    )


    vectorstore.persist()


    return vectorstore





def load_vectorstore(
        embeddings
):

    vectorstore = Chroma(

        persist_directory=CHROMA_PATH,

        embedding_function=embeddings

    )


    return vectorstore