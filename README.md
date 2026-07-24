# 📚 RAG Book Assistant

A Retrieval Augmented Generation (RAG) based AI application that allows users to upload PDF books/documents and ask questions from them. The application uses document processing, embeddings, vector search, and Large Language Models (LLMs) to generate accurate answers based only on the uploaded documents.

---

# 🚀 Features

- 📄 Upload PDF documents
- 🔍 Extract text from PDF files
- ✂️ Split documents into smaller chunks
- 🧠 Generate text embeddings
- 🗄️ Store embeddings in Chroma Vector Database
- 🔎 Semantic search using vector similarity
- 🤖 Generate answers using Mistral AI
- 💬 Ask questions from your own documents
- 🌐 Streamlit based user interface

---

# 🏗️ Architecture

```
                 USER
                   |
                   |
            Streamlit UI
                   |
                   |
        Upload PDF / Ask Question
                   |
                   |
          PDF Document Loader
                   |
                   |
          Text Chunking
                   |
                   |
          Embedding Model
                   |
                   |
             ChromaDB
                   |
                   |
             Retriever
                   |
                   |
          Prompt Template
                   |
                   |
            Mistral LLM
                   |
                   |
                Answer
```

---

# 🛠️ Tech Stack

## Programming Language

- Python

## Frontend

- Streamlit

## Framework

- LangChain

## Document Processing

- PyPDFLoader
- RecursiveCharacterTextSplitter

## Embedding Models

- Google Gemini Embeddings
- HuggingFace Embeddings
- OpenAI Embeddings

## Vector Database

- ChromaDB

## Large Language Model

- Mistral AI

---

# 📂 Project Structure

```
rag-book-assistant/

│
├── app.py
│
├── .env
│
├── requirements.txt
│
├── chroma_db/
│
├── config/
│   └── settings.py
│
├── ingestion/
│   ├── loader.py
│   ├── splitter.py
│   └── ingest.py
│
├── services/
│   ├── embeddings.py
│   ├── vectorstore.py
│   ├── llm.py
│   └── rag.py
│
└── README.md
```

---

# ⚙️ Installation

## Step 1: Clone Repository

```bash
git clone <repository-url>

cd rag-book-assistant
```

---

## Step 2: Create Virtual Environment

### Windows

```bash
python -m venv rag-book
```

Activate:

```bash
rag-book\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv rag-book

source rag-book/bin/activate
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

Example:

```env
MISTRAL_API_KEY=your_mistral_api_key

GOOGLE_API_KEY=your_google_api_key
```

---

# ▶️ Run Application

Start Streamlit:

```bash
streamlit run app.py
```

Open browser:

```
http://localhost:8501
```

---

# 🔄 How RAG Pipeline Works

## 1. Upload PDF

User uploads a PDF document.

Example:

```
Machine_Learning.pdf
```

---

## 2. PDF Loading

The PDF loader extracts text from the document.

```
PDF
 |
 ↓
Documents
```

---

## 3. Text Splitting

Large documents are divided into smaller chunks.

Example:

```
Document

↓

Chunk 1
Chunk 2
Chunk 3
```

This helps the model process information efficiently.

---

## 4. Embedding Generation

Each text chunk is converted into numerical vectors.

Example:

```
Text

↓

[0.234, 0.567, 0.891]
```

These vectors represent the meaning of the text.

---

## 5. Store in Vector Database

The embeddings are stored inside ChromaDB.

```
ChromaDB

Text + Vector
```

---

## 6. User Question

Example:

```
What is supervised learning?
```

The question is converted into an embedding.

---

## 7. Similarity Search

Retriever searches the most relevant document chunks.

```
Question

↓

Relevant Context
```

---

## 8. Answer Generation

The retrieved context and user question are sent to Mistral AI.

```
Context
+
Question

↓

Mistral LLM

↓

Final Answer
```

---

# 🧠 RAG Architecture

```
              Retrieval

User Question
       |
       |
       ↓

Embedding Search

       |
       |
       ↓

Relevant Documents


              Generation

Documents
    +
Question

       |
       |
       ↓

      LLM

       |
       |
       ↓

     Answer
```

---

# 📦 Requirements

Example `requirements.txt`

```
streamlit
langchain
langchain-community
langchain-mistralai
langchain-google-genai
langchain-chroma
chromadb
pypdf
python-dotenv
sentence-transformers
```

---

# 🌟 Future Improvements

- Multiple PDF upload support
- Chat history
- Conversation memory
- User authentication
- Streaming responses
- Better embedding models
- Qdrant vector database integration
- Pinecone integration
- Docker deployment
- Cloud deployment
- Voice input support

---

# 🚀 Deployment Architecture

Production architecture:

```
             Frontend
            Streamlit

                |

                |

             Backend
             FastAPI

                |

                |

          Vector Database
          Qdrant/Pinecone

                |

                |

              LLM API
          Mistral/Gemini
```

---

# 📚 Concepts Covered

This project demonstrates:

- Retrieval Augmented Generation (RAG)
- Large Language Models (LLMs)
- Vector Databases
- Embeddings
- Semantic Search
- LangChain
- Prompt Engineering
- AI Application Development

---

# 👨‍💻 Author

Your Name

---

# 📜 License

MIT License
