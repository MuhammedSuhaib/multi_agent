import asyncio
from agents import Agent, Runner,RunContextWrapper
from agents.lifecycle import AgentHooks
from configs.config import model_config
from tools.tools import subtract_numbers
from typing import Any
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

agent = Agent(
    name="Test_Agent",
    instructions="",
    tools=[subtract_numbers],
    hooks=MyHooks(),
    model=model_config,
    tool_use_behavior="stop_on_first_tool"
)

async def main():
   res = await Runner.run(agent, input="5-215",hooks=My_Runner_Hooks())
   print("⚡",res.final_output)
if __name__ == "__main__":
    asyncio.run(main())
