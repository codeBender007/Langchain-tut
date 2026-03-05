# from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
# import torch


# def get_model():
#     llm = HuggingFacePipeline.from_model_id(
#         model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#         task="text-generation",
#         pipeline_kwargs=dict(
#             temperature=0.5,
#             # max_new_tokens=500,
#         ),

#     )

#     model = ChatHuggingFace(llm=llm)
#     return model
















from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch

def get_model():
    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    
    # torch_dtype ko torch.float32 ya float16 rakhein CPU ke liye
    # device_map="auto" ya "cpu" ke liye 'accelerate' zaroori hai
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype=torch.float32, 
        low_cpu_mem_usage=True,
        device_map="cpu" 
    )
    
    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=256,
        temperature=0.5,
        do_sample=True
    )
    
    llm = HuggingFacePipeline(pipeline=pipe)
    return ChatHuggingFace(llm=llm)