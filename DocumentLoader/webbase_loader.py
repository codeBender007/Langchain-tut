from langchain_community.document_loaders import WebBaseLoader
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
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)

url = 'https://www.amazon.in/Apple-2026-MacBook-Laptop-chip/dp/B0GR1HPR1W/ref=sr_1_1_sspa?crid=2B91WJGOOPYZM&dib=eyJ2IjoiMSJ9.cVZmuypfCHaeYDIrkQeofMWjqz93HKYMoe7stKWd2abhKFTtclc7I6AJA1CSzzCO3TA_d0rR1fkt0mqWGJxQDszbP3H0MPkNSoHrJmJfmvjZ-XP-UeYBxJF2eYQhdShFWJc2GPhn182BEqGZtpHA_ZL_r65T0_PiCPlmFCpEtk74noyMBQhpY0NtHFYgfZogq08cqdnrTgzBOzOddias1XfzRhfrXVFTO1Ly0lVKEkE.BVA5S6pCFOagh3xj4efCe9EJFzL6YRq8GBbXlCde9pQ&dib_tag=se&keywords=amazon+macbook+air&qid=1777291103&sprefix=amazon+macbo%2Caps%2C560&sr=8-1-spons&aref=6acDS3uetE&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1'

loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

result = chain.invoke({'question':'What is the prodcut that we are talking about?','text':docs[0].page_content})

print(result)