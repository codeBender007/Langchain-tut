from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests



load_dotenv()

# process = huggingface ke model ka setup krna 
llm1 = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task='text-generation'
)
model = ChatHuggingFace(llm=llm1)
# ********************************


# 1process = create tool 
@tool 
def multiply(a:int , b:int) -> int:
    """multiply two numbers"""
    return (a*b)

# print(result)
# ******************


# 2process = tool bind connect tool with model ab is model se hmne apna ek custom tool connect krdiya
LLMWithTools = model.bind_tools([multiply])
# ****ab ya variable me model + tool dono hai**********


query = HumanMessage("can you multiply 3 with 10")
message = [query]

result = LLMWithTools.invoke(message)

message.append(result)

tool_result = multiply.invoke(result.tool_calls[0])

message.append(tool_result)

# 3process = tool execution
# res = LLMWithTools.invoke("hi how are you")
# res = LLMWithTools.invoke("can you multiply 3 with 10").tool_calls[0]['args']
# result1 = LLMWithTools.invoke("can you multiply 3 with 10").tool_calls[0]
# res = LLMWithTools.invoke("can you multiply 3 with 10")
# print(response)
# print(res)
# ***********


# process 
# message.append(res)
# print(message)

# toolResult = multiply.invoke(result)

# result2 = message.append(toolResult)
result3 = LLMWithTools.invoke(message)
print(result3.content)