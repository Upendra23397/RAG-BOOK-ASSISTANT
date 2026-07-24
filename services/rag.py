from services.embeddings import get_embeddings
from services.vectorstore import load_vectorstore
from services.retriever import get_retriever
from services.llm import get_llm

from prompts.prompt import rag_prompt



def ask_question(question):


    embeddings = get_embeddings()


    vectorstore = load_vectorstore(

        embeddings

    )


    retriever = get_retriever(

        vectorstore

    )


    docs = retriever.invoke(

        question

    )


    context = "\n\n".join(

        [
            doc.page_content
            for doc in docs
        ]

    )


    prompt = rag_prompt.invoke(

        {

        "context":context,

        "question":question

        }

    )


    llm = get_llm()


    response = llm.invoke(

        prompt

    )


    return response.content