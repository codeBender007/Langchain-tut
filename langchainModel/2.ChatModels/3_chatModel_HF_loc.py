import torch
from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
# from dotenv from load_dotenv

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    device=0,  # <--- Ye line model ko aapke NVIDIA GPU par load karegi 
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=30,
    )
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("what is capital of india.")

print(result.content)

# import torch
# print(torch.cuda.is_available())