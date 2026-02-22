from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
import torch


def get_model():
    llm = HuggingFacePipeline.from_model_id(
        model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        task="text-generation",
        pipeline_kwargs=dict(
            temperature=0.5,
            # max_new_tokens=500,
        ),

    )

    model = ChatHuggingFace(llm=llm)
    return model

