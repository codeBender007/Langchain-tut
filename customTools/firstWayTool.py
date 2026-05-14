from langchain_core.tools import tool


# 1) create function
def multiplication1(a,b):
    """multiplication two numbers"""
    return a*b


# 2) create function or isme type hints bi add kra hai 
def multiplication2(a:int ,b:int) ->int:
    """Mulitplicaiton two numbers"""
    return a*b


# 3) create function with @tool(decorator) isse LLM is function se interect kr skta hai
@tool
def multiplication3(a:int ,b:int) ->int:
    """Mulitplicaiton two numbers"""
    return a*b

    # isko call ese isliya kra jata hai qki ya tool hai to runnable bi hoga hi 
result = multiplication3.invoke({'a':10,'b':30})
print(result)
# ***************