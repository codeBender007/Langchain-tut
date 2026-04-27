from langchain_community.document_loaders import TextLoader
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task='text-generation'
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

prompt = PromptTemplate(
    template = 'write a summary for the following poem \n {poem}',
    input_variables=['poem']
)


loader = TextLoader('cricket.txt',encoding='utf-8')

docs = loader.load()

# print(docs)
# print(docs[0])

chain = prompt | model | parser 


result = chain.invoke({'poem':docs[0].page_content})
print(result)