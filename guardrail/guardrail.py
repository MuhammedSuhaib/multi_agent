from agents import (
    Agent,
    input_guardrail,
    output_guardrail,
    RunContextWrapper,
    GuardrailFunctionOutput,
    Runner,
    TResponseInputItem,
)
from schemas.schemas import Guardrail_Output
from configs.config import model_config


@input_guardrail
async def guardrail_input_function(
    ctx: RunContextWrapper[None], agent: Agent, input: str | list[TResponseInputItem]
) -> GuardrailFunctionOutput:
    # THIS runner runs the guardrail agent                               ⬇           ⬇               ↙For future use
    result = await Runner.run(guardrail_agent, input=input, context=ctx.context)
    #      ↘____________________________________
    #                                            ↘
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=not result.final_output.is_querry_about_hotel,  # it takes either true or false means it only takes boolean values if it get false it will *not* trigger the tripwire
    )


# this is just a normal agent with a structured output
guardrail_agent = Agent(
    name="Guardrail Agent for Hotel",
  instructions="""
    Classify the query:
    - If about Hotel (booking, rooms, services): is_querry_about_hotel=True
    - If about accounts/taxes: is_querry_related_to_account_and_tax=True
    - Otherwise: both False
    """,
    model=model_config,
    output_type=Guardrail_Output,
)
# async function + agent = Guardrail agent
#           |
#   1: use @input_guardrail 2: use 3 params(ctx, agent to apply guardrail_agent, input)
#                                             |
#                                          give type RunContextWrapper


@output_guardrail
async def guardrail_output_function(
    ctx: RunContextWrapper, agent: Agent, output
) -> GuardrailFunctionOutput:
    result = await Runner.run(guardrail_agent, output, context=ctx.context)

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_querry_related_to_account_and_tax,
    )
