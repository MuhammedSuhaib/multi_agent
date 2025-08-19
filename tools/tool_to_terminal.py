import asyncio
from agents import (
    Agent,
    Runner,
    function_tool,
    FunctionToolResult,
    RunContextWrapper,
    set_tracing_export_api_key,
    trace,
)
from agents.agent import ToolsToFinalOutputResult
from typing import List, Any
from agents import OpenAIChatCompletionsModel, AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
external_client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
model_config = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash", openai_client=external_client
)
Tracing_key = os.getenv("Tracing_key")


@function_tool
def get_weather(city: str) -> str:
    """Returns weather info for the specified city."""
    return f"The weather in {city} is sunny"


def custom_tool_handler(
    context: RunContextWrapper[Any], tool_results: List[FunctionToolResult]
) -> ToolsToFinalOutputResult:
    """Processes tool results to decide final output."""
    for result in tool_results:
        if result.output and "sunny" in result.output:
            return ToolsToFinalOutputResult(
                is_final_output=True, final_output=f"Final weather: {result.output}"
            )
    return ToolsToFinalOutputResult(is_final_output=False, final_output=None)


agent = Agent(
    Name="Weather Agent",
    instructions="Retrieve weather details.",
    tools=[get_weather],
    tool_use_behavior=custom_tool_handler,
    model=model_config,
)


async def main():
    set_tracing_export_api_key(Tracing_key)
    with trace(workflow_name="ToolsToFinalOutputResult", disabled=False):
        res = await Runner.run(
            agent, input="weather in karachi", context="Sheikhani Group", max_turns=1
        )
        print("⚡", res.final_output)


if __name__ == "__main__":
    asyncio.run(main())
