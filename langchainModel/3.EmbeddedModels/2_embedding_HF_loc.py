from langchain_huggingface import HuggingFaceEmbeddings


embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

document = [
    "delhi is capital of india",
    "london is capital of UK",
    "moscow is capital of russia",
    ]
vector = embedding.embed_documents(document)

print(str(vector))