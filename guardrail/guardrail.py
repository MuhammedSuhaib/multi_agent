from agents import Agent, input_guardrail, RunContextWrapper, GuardrailFunctionOutput, Runner
from schemas.schemas import Guardrail_Output
from configs.config import model_config

@input_guardrail
async def guardrail_input_function(ctx: RunContextWrapper, agent, input):
    #               THIS runner runs the guardrail agent                   ↘       we apply context for futur use if we need it so...
    result = await Runner.run(guardrail_agent,                       input=input, context=ctx.context)
#      ↘____________________________________
#                                            ↘
    return GuardrailFunctionOutput(output_info=result.final_output,
        tripwire_triggered=not result.final_output.is_querry_about_hotel_laurel #it takes either true or false means it only takes boolean values if it get false it will *not* trigger the tripwire
        )
# this is just a normal agent with a structured output
guardrail_agent = Agent(
    name="Guardrail Agent for Hotel Laurel",
    instructions="Check queries for Hotel Laurel.",
    model=model_config,
    output_type=Guardrail_Output,

)
# async function + agent = Guardrail agent
#           |
#   1: use @input_guardrail 2: use 3 params(ctx, agent to apply guardrail_agent, input)
#                                             |
#                                          give type RunContextWrapper