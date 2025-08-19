from agents import Agent, ModelSettings,WebSearchTool,FileSearchTool,StopAtTools

from configs.config import model_config
from tools.tools import subtract_numbers
from guardrail.guardrail import guardrail_input_function,guardrail_output_function

# Math Agent
math_agent = Agent(
    name="math_agent",
    instructions=(
        "You are a math agent. Solve math problems in the shortest way. "
        # "Always use the subtract_numbers tool when applicable."
    ),
    tools=[subtract_numbers],
    # tool_use_behavior=StopAtTools(['subtract_numbers','']),
    tool_use_behavior="stop_on_first_tool",
    handoff_description="You are a math teacher",
    model=model_config,
    # model_settings=ModelSettings(tool_choice=subtract_numbers,)  #optional
)

# Physics Agent
physics_agent = math_agent.clone(
    name="physics_agent",
    instructions=(
        "You are a Physics agent. Solve physics problems in the shortest way."
    ),
    handoff_description="You are a Physics teacher",
    model_settings=ModelSettings(max_tokens=10)  #optional
)

# Hotel Assistant
hotel_assistant = math_agent.clone(
    name="hotel_assistant",
    instructions="""
    You are a helpful hotel assistant.
    - There are 99 rooms in our hotel.
    - Hotel name is Hotel Laurel.
    - Hotel owner name is Ali Sheikhani.
    - 9 of those rooms are luxury rooms (high cost).
    - 10 of those are basic rooms (low cost).
    - The rest are standard rooms (medium cost).
    """,
    input_guardrails=[guardrail_input_function],
    output_guardrails=[guardrail_output_function],
    tools=[
        WebSearchTool(),
        FileSearchTool(
            vector_store_ids='',
            max_num_results=0,
            include_search_results=False,#????????
            ranking_options=None,#???????????
            ),
    ]

)

# Triage Agent — decides who should handle the query
Triage_Agent = math_agent.clone(
    name="Triage_Agent",
    instructions=(
        "Help the user by routing them to the right specialist.\n"
        "If math → handoff to math_agent.\n"
        "If physics → handoff to physics_agent.\n"
        "If hotel → handoff to hotel_assistant."
    ),
    handoffs=[math_agent, physics_agent, hotel_assistant],
)
