# ChatPromptTemplate is tool ka use SystemMessage , HumanMessage , AIMessage ko jod kr ek list bnana hai 

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage , HumanMessage 

chat_template = ChatPromptTemplate([ 
    ('system', 'You are a Helpfull {domain} expert.'),
    ('human', 'Explain in simple terms, what is {topic}')

    # SystemMessage(content='You are a Helpfull {domain} expert.'),
    # HumanMessage(content='Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket','topic':'dursa'})

print(prompt)