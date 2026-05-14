from langchain_core.tools import tool



@tool
def multiplication(a:int ,b:int) ->int:
    """Mulitplicaiton two numbers"""
    return a*b



@tool
def add(a:int ,b:int) ->int:
    """addition two numbers"""
    return a+b


class MathToolKit:
    def get_tools(self):
        return[add,multiplication]

# create object of MathToolKit class
mathObj = MathToolKit()
Tools = mathObj.get_tools()

for tool in Tools:
    print(tool.name , "=>" , tool.description)