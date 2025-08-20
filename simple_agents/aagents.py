from agents import Agent, ModelSettings
from configs.config import model_config
from tools.tools import lookup_order, faq_tool
from guardrail.guardrail import guardrail_input_function, guardrail_output_function

# --- Human Agent ---
HumanAgent = Agent(
    name="HumanAgent",
    instructions="Handle cases that BotAgent cannot answer. Provide support personally.",
    model=model_config,
)
# --- Bot Agent ---
BotAgent = Agent(
    name="BotAgent",
    instructions="Handle FAQs and order lookup in the shortest way.",
    tools=[faq_tool, lookup_order],
    tool_use_behavior="stop_on_first_tool",
    # Escalate to a human agent if the query is complex or sentiment is negative (handoff)
    handoff_description="If unable to handle or query is negative, escalate to HumanAgent.",
    handoffs=[HumanAgent],
    input_guardrails=[guardrail_input_function],
    output_guardrails=[guardrail_output_function],
    model=model_config,
    # Showcase usage of model_settings (tool_choice, metadata, etc.)
    model_settings=ModelSettings(tool_choice="auto"),
)