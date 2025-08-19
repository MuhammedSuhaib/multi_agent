# tools\tools.py
from agents import (
    FunctionTool,
    RunContextWrapper,
    function_tool,
    ToolsToFinalOutputFunction,
)
from schemas.schemas import SubtractInput


@function_tool(
    name_override="subtract_numbers", description_override="Subtract two numbers"
)
def subtract_numbers(Sub: SubtractInput) -> int:
    """Subtract two numbers."""
    print("Subtracting tool fired 🔥")
    return ("Sub.a - Sub.b: ", Sub.a - Sub.b)


@function_tool(name_override="WebSearchTool", description_override="Search the web")
def WebSearchTool(query: str) -> str:
    """Search the web."""
    print("WebSearchTool fired ==🔥")
    return f"Results for '{query}': ..."


# async def subtract_numbers(ctx:RunContextWrapper[SubtractInput], args: str) -> int:
#     """Subtract two numbers."""
#     print('Subtracting tool fired 🔥')
#     params = SubtractInput.model_validate_json(args)
#     return params.a - params.b

# tool = FunctionTool(
#     name="subtract_numbers",
#     description="Subtract two numbers",
#     params_json_schema=FunctionArgs.model_json_schema(),
#     on_invoke_tool=subtract_numbers,
#     is_enabled=False,     # make the tool invisible and save tokens  we can also pass a callable here which return a boolen value so using context write such a logic which which will return true at certain condition and false at certain conditions
# )
