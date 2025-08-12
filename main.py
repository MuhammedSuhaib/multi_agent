from agents import Runner, set_tracing_export_api_key
from simple_agents.aagents import Triage_Agent
from openai.types.responses import ResponseTextDeltaEvent
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
Tracing_key = os.getenv('Tracing_key')

async def main():
    set_tracing_export_api_key(Tracing_key)

    with trace(workflow_name="Multi_Agents"): 
        while True:
            try:
                user_query = input("\nUser: ")
            except EOFError:
                break

            # Now triage_agent already knows its handoff targets
            output = Runner.run_streamed(starting_agent=Triage_Agent, input=user_query)
            async for event in output.stream_events():
                if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
                    print(event.data.delta, end="", flush=True)

asyncio.run(main())
