# 2) using pydantic to BaseModel and Field and StructuredTool in sab ka use krke bnaya jata hai 


from langchain_core.tools import StructuredTool
from pydantic import Field , BaseModel

class multiply_input(BaseModel):
    a:int  = Field(required=True , description="The First Number Add")
    b:int  = Field(required=True , description="The second Number Add")


def multiply(a:int ,b:int) ->int:
    """Mulitplicaiton two numbers"""
    return a*b

multipy_tool = StructuredTool.from_function(
    func=multiply,
    name="multiplier",
    description="mulitiplication two numbers",
    args_schema=multiply_input,
)