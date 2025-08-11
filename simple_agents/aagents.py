# simple_agents/agents.py
from agents import Agent
from configs.config import model_config
from tools.tools import subtract_numbers

math_agent = Agent(
    name="Math Agent",
    instructions=(
        "You are a math agent. Your task is to solve math problems. "
        "Respond with the solution in the shortest way, and you must use the tool."
    ),
    tools=[subtract_numbers],
    tool_use_behavior="stop_on_first_tool",
    handoff_description="You are a math teacher",
    model=model_config
)  # Agent level config

physics_agent = Agent(
    name="Physics Agent",
    instructions=(
        "You are a Physics agent. Your task is to solve physics problems. "
        "Respond with the solution in the shortest way."
    ),
    handoff_description="You are a Physics teacher",
    model=model_config
)  # Agent level config

hotel_assistant = Agent(
    name="Hotel Assistant",
    instructions="""
    You are a helpful hotel assistant.
        - There are 99 rooms in our hotel.
        - Hotel name is Hotel Laurel.
        - Hotel owner name is Ali Sheikhani.
        - 9 of those rooms are luxury rooms available at high cost.
        - 10 of those are basic rooms available at low cost.
        - The rest of the rooms are standard rooms available at medium cost.
    """,
    model=model_config,
    # input_guardrails=[guardrail_input_function],
    # output_guardrails=[]
)

# Starting Agent
Triage_Agent = Agent(
    name="General Assistant",
    instructions="You just have to hand off.",
    handoffs=[math_agent, physics_agent, hotel_assistant],
    model=model_config
)  # Agent level config
