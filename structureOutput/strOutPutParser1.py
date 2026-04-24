from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

template1 = PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables=["topic"]
)


template2 = PromptTemplate(
    template="write a 5 line summary on the following text. /n {text}",
    input_variables=["text"]
)


parser = StrOutputParser() 

chain = template1 | model | parser | template2 | model | parser
# first prompt model ke pas jyga jo data ayga usme metadata or content hoga usme se content ka data parser
# nikalega ab detail text dusre prompt me bhejna hai fir model ko jyga 

result = chain.invoke({"topic":"black hole"})

print(result)