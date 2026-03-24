from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder
# from langchain_core.messages import HumanMessage

chat_template = ChatPromptTemplate([
    ('system','You are a helpfull customer support Agent.'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])


chat_history=[]

with open('chat_history.txt') as f:
    chat_history.append(f.readline())

print(chat_history)

# chat_template.invoke({'chat_history':chat_history , "query":HumanMessage(content='Where is my refund')})
# niche wale tareeke me humanMessage import krna pad rha th lkn unki koi zzrurt ni 
# qki 7 line me hamne already likhdiya ke koi bi message ayga wo human hoga.

final_prompt = chat_template.invoke({'chat_history':chat_history , "query":'Where is my refund'})

print(final_prompt)