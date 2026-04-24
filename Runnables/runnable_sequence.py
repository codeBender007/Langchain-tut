# from langchain_Huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


prompt1 = PromptTemplate(
    template = "write a joke about {topic}",
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = "Explain the following joke - {text}",
    input_variables = ['text']
)

llm1 = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task='text-generation'
)

model = ChatHuggingFace(llm=llm1)

parser = StrOutputParser()



chain  = RunnableSequence(prompt1 , model , parser , prompt2 , model , parser)

result = chain.invoke({'topic':'AI'})

print("result : ",result)