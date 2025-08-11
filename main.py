from agents import Runner, set_tracing_export_api_key, trace
from simple_agents.aagents import Triage_Agent, math_agent, physics_agent, hotel_assistant
from openai.types.responses import ResponseTextDeltaEvent
import asyncio
import os
import json
from dotenv import load_dotenv

load_dotenv()

Tracing_key = os.getenv('Tracing_key')

agents_map = {
    "math_agent": math_agent,
    "physics_agent": physics_agent,
    "hotel_assistant": hotel_assistant
}

async def run_agent(agent, query):
    output = Runner.run_streamed(starting_agent=agent, input=query)
    async for event in output.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)

async def main():
    set_tracing_export_api_key(Tracing_key)
    with trace(workflow_name="Multi_Agents"): 
        while True:
            try:
                user_query = input("\nUser: ")
            except EOFError:
                break

            # Step 1 — run triage agent
            triage_output = Runner.run_streamed(starting_agent=Triage_Agent, input=user_query)
            collected_text = ""
            async for event in triage_output.stream_events():
                if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
                    collected_text += event.data.delta

            # Step 2 — parse JSON output from triage
            try:
                handoff_data = json.loads(collected_text)
                target_name = handoff_data.get("handoff_target")
            except json.JSONDecodeError:
                print(f"\n❌ Triage failed — unexpected output: {collected_text}")
                continue

            # Step 3 — run chosen agent
            if target_name in agents_map:
                print(f"\n➡ Handoff to {target_name}:\n")
                await run_agent(agents_map[target_name], user_query)
            else:
                print(f"\n❌ Unknown agent: {target_name}")

asyncio.run(main())
