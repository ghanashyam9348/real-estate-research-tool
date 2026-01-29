# � Real Estate Research Tool

A sophisticated AI-powered research tool that leverages **Retrieval Augmented Generation (RAG)** with modern **LangChain 1.x (LCEL)** to extract insights from real estate documents and websites. Users can input article URLs and ask questions to receive relevant answers with cited sources.

## 📸 Application Screenshot

![Real Estate Research Tool](resources/image.png)

## ✨ Features

- **🔗 URL Processing**: Load and process multiple URLs to fetch article content
- **📄 Document Splitting**: Intelligent text chunking using RecursiveCharacterTextSplitter
- **🧠 Vector Embeddings**: Generate embeddings using HuggingFace's sentence transformers
- **💾 Vector Database**: Store and retrieve documents efficiently using ChromaDB
- **🤖 LLM Integration**: Query using Llama 3.3 70B via Groq API for accurate responses
- **🔄 Modern LCEL Chains**: Built with LangChain Expression Language (LCEL) for composable, flexible chains
- **📚 Source Attribution**: Automatically cite sources for all generated answers
- **🎨 Beautiful UI**: Interactive Streamlit interface with real-time feedback

## 🏗️ Architecture

```
User Input (URLs/Query)
    ↓
URL Loader (UnstructuredURLLoader)
    ↓
Text Splitter (RecursiveCharacterTextSplitter)
    ↓
Vector Store (ChromaDB with HuggingFace Embeddings)
    ↓
Retriever (Vector Search)
    ↓
LCEL Chain (Prompt → LLM → Output Parser)
    ↓
Answer with Sources
```

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Frontend** | Streamlit |
| **LLM Framework** | LangChain 1.x (LCEL) |
| **Language Model** | Llama 3.3 70B (via Groq) |
| **Embeddings** | HuggingFace Sentence Transformers |
| **Vector Database** | ChromaDB |
| **Document Loader** | UnstructuredURLLoader |
| **Language** | Python 3.11+ |

## 📋 Prerequisites

- Python 3.11 or higher
- Groq API Key ([Get one here](https://console.groq.com))
- Internet connection for URL processing

## 🚀 Installation

1. **Clone or download** the project directory

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Create a `.env` file** in the project root with your Groq credentials:
    ```env
    GROQ_API_KEY=your_groq_api_key_here
    ```

4. **Verify installation**:
    ```bash
    python -c "import streamlit; print('Streamlit installed!')"
    ```

## 💻 Usage

1. **Start the Streamlit app**:
    ```bash
    streamlit run main.py
    ```

2. **Open your browser** (Usually opens at `http://localhost:8501`)

3. **Input URLs** in the sidebar:
   - Enter up to 3 URLs in the input fields
   - URLs can be from news sites, research papers, or any web content

4. **Process URLs**:
   - Click the "🔄 Process URLs" button
   - Wait for the processing to complete (you'll see status updates)
   - The system will:
     - Load and parse the content
     - Split text into chunks
     - Generate embeddings
     - Store in vector database

5. **Ask Questions**:
   - Type your question in the "❓ Ask a Question" field
   - Press Enter or click outside the input
   - Get an AI-generated answer with source citations

## 📝 Example Queries

- "What is the current growth rate of the real estate market?"
- "Which regions are showing the highest growth?"
- "What are the investment opportunities mentioned?"
- "What are the key market trends?"

## 🧬 Project Structure

```
real-estate-tool/
├── main.py                 # Streamlit web application
├── rag.py                  # RAG implementation with LCEL chains
├── prompt.py               # Customized prompt templates for RAG
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (create this)
├── resources/
│   ├── vectorstore/       # ChromaDB storage (auto-created)
│   └── image.png          # Application screenshot
└── README.md              # This file
```

## 🔧 Configuration

### Custom Prompt Templates (prompt.py)

The application uses customized prompt templates to guide the LLM behavior:

**PROMPT** - Main QA template:
```python
PROMPT = PromptTemplate(
    template="""You are a helpful real estate assistant. Use the provided context to answer questions accurately.
If the answer is not in the context, say "I don't have information about that in the provided documents."

Context:
{summaries}

Question: {question}

Answer:""",
    input_variables=["summaries", "question"],
)
```

**EXAMPLE_PROMPT** - Document formatting template:
```python
EXAMPLE_PROMPT = PromptTemplate(
    template="Content: {page_content}\nSource: {source}",
    input_variables=["page_content", "source"],
)
```

These custom prompts ensure:
- Domain-specific behavior (real estate assistant)
- Accurate context usage (answers only from provided documents)
- Responsible AI (admits when information is missing)

### Other Configuration

Key constants in `rag.py`:

```python
CHUNK_SIZE = 1000                    # Size of text chunks
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
VECTORSTORE_DIR = "resources/vectorstore"
COLLECTION_NAME = "real_estate"
```

## 🎯 How It Works

1. **LCEL Chain Construction**: The app uses LangChain's modern LCEL syntax to build composable chains
2. **Custom Prompts**: Leverages `prompt.py` templates to customize LLM behavior for real estate domain
3. **Retrieval**: Documents are retrieved based on semantic similarity to the query
4. **Prompt Engineering**: Retrieved context is formatted with the query using custom prompt templates
5. **LLM Generation**: Llama 3.3 70B generates contextual answers with domain-aware instructions
6. **Source Tracking**: Unique sources are extracted and displayed

## 🔐 API Usage

The tool uses the **Groq API** for LLM inference. Free tier includes generous limits for development and testing.

## 📄 License

This project is licensed under the MIT License. However, commercial use requires prior written permission from the author. See the LICENSE file for details.

---

**Made with ❤️ using LangChain LCEL, Streamlit, and Groq**
