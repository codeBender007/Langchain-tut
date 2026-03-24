from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

# llm1 = HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task='text-generation'
# )
llm1 = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation",
    max_new_tokens=50,
)

model = ChatHuggingFace(llm=llm1)

result = model.invoke("russia ki capital ka name ka kya hai.")
print("asnwer : "+result.content)

