import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct", 
    task="text-generation",
    max_new_tokens=512,
    do_sample=False # Keep it deterministic for better parsing
)

model = ChatHuggingFace(llm=llm)

# Define your schema
class Person(BaseModel):
    name: str = Field(description='Name of the person')
    age: int = Field(gt=18, description='Age of the person (must be older than 18)')
    city: str = Field(description='Name of the city the person belongs to')

# Initialize the parser
parser = PydanticOutputParser(pydantic_object=Person)

# Create the prompt template
template = PromptTemplate(
    template='Generate the name, age (over 18), and city of a fictional {place} person.\n{format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# Build the chain
chain = template | model | parser


final_result = chain.invoke({'place': 'Sri Lankan'})
print("\nSUCCESS! Result as Python Object:")
print(f"Name: {final_result.name}")
print(f"Age:  {final_result.age}")
print(f"City: {final_result.city}")

# try:
#     # Run the chain

# except Exception as e:
#     print(f"\nAn error occurred: {e}")
#     # If the parser fails, it's often because the model added extra text.
#     # We can debug by seeing the raw model output if we didn't use a chain.