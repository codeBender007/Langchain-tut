from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace
from langchain_core.tools import tool
import requests
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_react_agent , AgentExecutor
from langchain import hub

# process = setup for model 
llm1 = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm1)
# **************

searchTool = DuckDuckGoSearchRun()


prompt = hub.pull("hwchase17/react")

agent = create_react_agent(
    llm=llm1,
    tools=[searchTool],
    prompt=prompt
)