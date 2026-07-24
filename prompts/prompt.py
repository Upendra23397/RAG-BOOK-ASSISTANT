from langchain_core.prompts import ChatPromptTemplate


rag_prompt = ChatPromptTemplate.from_messages(
    [

        (
            "system",
            """
You are a helpful AI assistant.

Answer ONLY from the provided context.

If the answer is not present in the context,
say:

"I could not find the answer in the document."
"""
        ),

        (
            "human",
            """
Context:

{context}


Question:

{question}
"""
        )

    ]
)