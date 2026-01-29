from langchain_core.prompts import PromptTemplate

# Main prompt template for QA with sources
# This prompt is designed for retrieval-augmented question answering
PROMPT = PromptTemplate(
    template="""You are a helpful real estate assistant. Use the provided context to answer questions accurately.
If the answer is not in the context, say "I don't have information about that in the provided documents."

Context:
{summaries}

Question: {question}

Answer:""",
    input_variables=["summaries", "question"],
)

# Prompt template for formatting individual documents
EXAMPLE_PROMPT = PromptTemplate(
    template="Content: {page_content}\nSource: {source}",
    input_variables=["page_content", "source"],
)
