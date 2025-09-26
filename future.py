
import os
import asyncio
from dataclasses import dataclass
from agents import Agent, Runner, function_tool, RunContextWrapper
from configs.config import model_config

@dataclass
class UserContext:
    username: str
    email: str | None = None


@function_tool()
async def search(local_context: RunContextWrapper[UserContext], query: str) -> str:
    import time
    time.sleep(30)  # Simulating a delay for the search operation
    return "No results found."

# Dynamic instructions
async def special_prompt(
    special_context: RunContextWrapper[UserContext], agent: Agent[UserContext]
) -> str:
    # who is user?
    # which agent
    print(f"\nUser: {special_context.context},\n Agent: {agent.name}\n")
    return f"You are a math expert. User: {special_context.context.username}, Agent: {agent.name}. Please assist with math-related queries."


math_agent: Agent = Agent(
    name="Genius", instructions=special_prompt, model=model_config, tools=[search]
)
# [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]


async def call_agent():
    # Call the agent with a specific input
    user_context = UserContext(username="abdullah")

    output = await Runner.run(
        starting_agent=math_agent,
        input="search for the best math tutor in my area",
        context=user_context,
    )
    print(f"\n\nOutput: {output.final_output}\n\n")


asyncio.run(call_agent())
