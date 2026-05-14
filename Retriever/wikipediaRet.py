from langchain_community.retrievers import WikipediaRetriever


# Initialize the retriever (optional: set language and top_k)
retriever = WikipediaRetriever(top_k_results=2, lang="en")


# Define your query
query = "can tell me salman khan"

# Get relevant Wikipedia documents
docs = retriever.invoke(query)

print(docs)