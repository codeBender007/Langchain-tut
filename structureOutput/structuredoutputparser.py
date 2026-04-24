from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser , ResponseSchema
# from langchain.output_parsers import StructuredOutputParser, ResponseSchema
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

# schema = (
#     ResponseSchema(name='name',description='name of the person'),
#     ResponseSchema(name='age',description='age of the person'),
#     ResponseSchema(name='city',description='city of the person')
# )


schema = (
    ResponseSchema(name='fact_1',description='fact 1 about the topic'),
    ResponseSchema(name='fact_2',description='fact 2 about the topic'),
    ResponseSchema(name='fact_3',description='fact 3 about the topic')
)
# ya hai formate ke mjhe model se is formate me data chahia 


parser = StructuredOutputParser.from_response_schemas(schema )


template = PromptTemplate(
    template="Give me 3 fact about {topic} \n {format_instruction}",
    input_variables=['topic'],
    partial_variables={"format_instruction":parser.get_format_instructions()}
)

prompt = template.invoke({"topic":"black hole"})

result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)