# from langchain_Huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence , RunnableParallel
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm1 = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task='text-generation'
)

model = ChatHuggingFace(llm=llm1)


prompt1 = PromptTemplate(
    template="generate a tweet about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a LinkedIn post about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

chain = RunnableParallel({
    'tweet':RunnableSequence(prompt1 , model , parser),
    'LinkedIn':RunnableSequence(prompt2 , model , parser)
})


result = chain.invoke({'topic':'AI'})

print(result)


