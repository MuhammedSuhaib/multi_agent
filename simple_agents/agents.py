# simple_agents\agents.py
from agents import Agent,input_guardrail,RunContextWrapper,GuardrailFunctionOutput,Runner
from configs.config import model_config
from tools.tools import subtract_numbers
from schemas.schemas import Guardrail_Output
math_agent = Agent(
name="Math Agent", 
instructions=
"You are a math agent. Your task is to solve math problems. Respond with the solution in shortest way,must use tool",
tools=[subtract_numbers], tool_use_behavior="stop_on_first_tool",
handoff_description="You are a math teacher",
model=model_config )#Agent level config

physics_agent = Agent(
name="Physics Agent",instructions="You are a Physics agent. Your task is to solve Physics problems. Respond with the solution in shortest way ", handoff_description="You are a Physics teacher",model=model_config )#Agent level config

hotel_assistant = Agent(
    name="Hotel Assistant",
    instructions="""
    You are helpful hotel assistant.
        - There are 99 rooms in our hotel
        - Hotel name is Hotel laurel.
        - Hotel Owner name is Ali sheikhani.
        - 9 of those rooms are luxury available at high cost.
        - 10 of those are basic rooms available at low cost.
        - reset of the rooms are standard rooms available at medium cost.
""",
    model=model_config,
    input_guardrails=[guardrial_input_function],
    output_guardrails=[]
)

# Starting Agent
Triage_Agent = Agent(
name="General Assistant",
instructions="You just ve to handoff",
handoffs=[math_agent, physics_agent , hotel_assistant],
model=model_config )#Agent level config

@input_guardrail
async def guardrial_input_function(ctx:RunContextWrapper,hotel_assistant,input):
    result = await Runner.run(guardrial_agent, input=input, context=ctx.context )

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=not result.final_output.is_query_about_hotel_laurel
    )

guardrial_agent = Agent(
    name="Guradrial Agent for Hotel laurel",
    instructions="Check queries for hotel laurel",
    model=model_config,
    output_type=Guardrail_Output

)
