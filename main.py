# main.py
from agents import Runner,SQLiteSession,set_tracing_export_api_key
from simple_agents.agents import Triage_Agent
from openai.types.responses import ResponseTextDeltaEvent
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()

KEY = os.getenv('KEY')
Tracing_key = os.getenv('Tracing_key')
session = SQLiteSession("Multi_Agent01", "multi_agent.db")
async def main():
    set_tracing_export_api_key(Tracing_key)
    # output = await Runner.run(starting_agent=Triage_Agent, input=input("User: "))      # Runner.Run
    output =  Runner.run_streamed(starting_agent=Triage_Agent, input=input("User: "),session=session)
    async for event in output.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
         print(event.data.delta, end="", flush=True)

asyncio.run(main())
