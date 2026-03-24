from langchain_core.messages import SystemMessage , HumanMessage , AIMessage
from langchain_huggingface import ChatHuggingFace , HuggingFacePipeline
from transformers import AutoModelForCausalLM , AutoTokenizer , pipeline    
import torch 

def get_model():
    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    tokenizer = AutoTokenizer.from_pretrained(model_id)

    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype = torch.float32,
        low_cpu_mem_usage = True,
        device_map = "cpu"
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

model = get_model()

messages = [
    SystemMessage(content="you are a helpfull assistant"),
    HumanMessage(content="tell me about langchain")
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)