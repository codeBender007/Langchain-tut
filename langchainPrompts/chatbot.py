from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain_core.messages import AIMessage , HumanMessage , SystemMessage
import torch


def get_model():
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0"

    tokenizer = AutoTokenizer.from_pretrained(model_id)

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


model = get_model()
chat_history = [
    SystemMessage(content="you are a helpfull AI Assistant")
]
        
while True:
    user_input = input("you : ")
    chat_history.append(HumanMessage(content = "user_input"))
    if user_input == "exit":
        break
    result = model.invoke(user_input)
    chat_history.append(AIMessage(content = "result"))
    print("AI : ",result.content)

print("History : ",chat_history)


# you : which one is greater 2 or 0 
# AI :  <|user|>
# which one is greater 2 or 0</s>
# <|assistant|>
# The greater of two numbers is the first one. In this case, the greater of two numbers is 2 since 0 is less than 2.
# you : now multiply the bigger number with 10 