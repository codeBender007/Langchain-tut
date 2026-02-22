from langchain_google_genai import ChatGoogleGenerativeAI
# Import "langchain_google_genai" could not be resolved
from dotenv import load_dotenv
# Import "dotenv" could not be resolved

load_dotenv()
print("1")
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')
print("2")
question="what is capital of india."
result = model.invoke(question)
print("3")
print("questin : "+question)
print("Answer : "+result.content)
