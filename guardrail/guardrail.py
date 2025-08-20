from agents import Agent, input_guardrail, output_guardrail, RunContextWrapper, GuardrailFunctionOutput, Runner, TResponseInputItem
from schemas.schemas import Guardrail_Output
from configs.config import model_config

# --- Guardrail Agent ---
# Enforce a simple guardrail: block or rephrase negative/offensive user input

guardrail_agent = Agent(
    name="Offensive/Negative Guardrail Agent",
    instructions="""
    Check if the input contains offensive, rude, or negative language.
    If detected, rephrase politely or return a warning.
    """,
    model=model_config,
    output_type=Guardrail_Output,
)

# --- Input Guardrail ---
@input_guardrail
async def guardrail_input_function(
    ctx: RunContextWrapper[None],
    agent: Agent,
    input: str | list[TResponseInputItem],
) -> GuardrailFunctionOutput:
    result = await Runner.run(guardrail_agent, input=input, context=ctx.context)
    
    # tripwire triggered if offensive/negative content detected
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.contains_offensive_language  # must be boolean
    )

# --- Output Guardrail ---
@output_guardrail
async def guardrail_output_function(ctx: RunContextWrapper, agent: Agent, output) -> GuardrailFunctionOutput:
    result = await Runner.run(guardrail_agent, output, context=ctx.context)
    
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.contains_offensive_language  # must be boolean
    )
