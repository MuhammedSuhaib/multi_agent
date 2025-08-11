from agents import Agent, input_guardrail, RunContextWrapper, GuardrailFunctionOutput, Runner
from schemas.schemas import Guardrail_Output
from configs.config import model_config
from simple_agents.aagents import hotel_assistant

@input_guardrail
async def guardrail_input_function(ctx: RunContextWrapper, hotel_assistant, input):
    result = await Runner.run(guardrail_agent, input=input, context=ctx.context)

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=not result.final_output.is_query_about_hotel_laurel
    )


guardrail_agent = Agent(
    name="Guardrail Agent for Hotel Laurel",
    instructions="Check queries for Hotel Laurel.",
    model=model_config,
    output_type=Guardrail_Output

)
