import asyncio
from agents import Agent, Runner,RunContextWrapper,set_tracing_disabled
from agents.lifecycle import AgentHooks
from configs.config import model_config
from tools.tools import subtract_numbers
from typing import Any

set_tracing_disabled(True)

# Agent Hooks
class MyHooks(AgentHooks):
    
    async def on_start(self, context: RunContextWrapper, agent: Agent) -> None:
        """Called before the agent is invoked. Called each time the running agent is changed to this
        agent."""
        print("Agent started:", agent.name)

    async def on_end(
        self,
        context: RunContextWrapper,
        agent: Agent,
        output: Any,
    ) -> None:
        """Called when the agent produces a final output."""
        print("Agent ended:", agent.name)

    async def on_tool_start(
        self,
        context: RunContextWrapper,
        agent: Agent,
        tool: subtract_numbers,
    ) -> None:
        """Called concurrently with tool invocation."""
        print("Tool started:", tool.name)

    async def on_tool_end(
        self,
        context: RunContextWrapper,
        agent: Agent,
        tool: subtract_numbers,
        result: str,
    ) -> None:
        """Called after a tool is invoked."""
        print("Tool ended:", tool.name)

# Runner Hooks
class My_Runner_Hooks(AgentHooks):
    
    async def on_agent_start(self, context: RunContextWrapper, agent: Agent) -> None:
        """Called before the agent is invoked. Called each time the current agent changes."""
        print("[Runner] : Agent started:", agent.name)


    async def on_agent_end(
        self,
        context: RunContextWrapper,
        agent: Agent,
        output: Any,
    ) -> None:
        """Called when the agent produces a final output."""
        print("[Runner] : Agent ended:", agent.name)
        
    async def on_tool_start(
        self,
        context: RunContextWrapper,
        agent: Agent,
        tool: subtract_numbers,
    ) -> None:
        """Called concurrently with tool invocation."""
        print("[Runner] : Tool started:", tool.name)

    async def on_tool_end(
        self,
        context: RunContextWrapper,
        agent: Agent,
        tool: subtract_numbers,
        result: str,
    ) -> None:
        """Called after a tool is invoked."""
        print("[Runner] : Tool ended",tool.description)

#  Both regular and async functions are accepted.
# Runner will call this so Runner only knows that first param is context and second is agent and thats it if change the order so things will still work but be mindfull of the outcomes
# if i dont pass context and also not use it in return so its ok
# it can work with any DT bcz evrything is obj but to mk our life easy we create a class so we can get 
#   1) structure Data if we are getting some data from api/dp etc 
#   2) easy access to type hints

def dynamic_instructions(context: RunContextWrapper, agent: Agent) -> str:
    # print("\n Context",context)
    # print("\n Agent",agent)
    return f"The user's name is {context}. Always greet the user with their name."

agent = Agent(
    name="Test_Agent",
    instructions=dynamic_instructions,
    tools=[subtract_numbers],
    hooks=MyHooks(),
    model=model_config,
    tool_use_behavior="stop_on_first_tool",
)

async def main():
   res = await Runner.run(agent, input="hi",hooks=My_Runner_Hooks(),context="Sheikhani Group",max_turns=1)
   print("⚡",res.final_output)
if __name__ == "__main__":
    asyncio.run(main())
