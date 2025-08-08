# simple_agents\agents.py
from agents import Agent
from configs.config import model_config
from tools.tools import subtract_numbers

math_agent = Agent(
name="Math Agent", 
instructions=
"You are a math agent. Your task is to solve math problems. Respond with the solution in shortest way,must use tool",
tools=[subtract_numbers], tool_use_behavior="stop_on_first_tool",
handoff_description="You are a math teacher",
model=model_config )#Agent level config


physics_agent = Agent(
name="Physics Agent",instructions="You are a Physics agent. Your task is to solve Physics problems. Respond with the solution in shortest way ", handoff_description="You are a Physics teacher",model=model_config )#Agent level config

# Starting Agent
Triage_Agent = Agent(
name="General Assistant",
instructions="You just ve to handoff",
handoffs=[math_agent, physics_agent],
model=model_config )#Agent level config
