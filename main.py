from agents import RunConfig, Runner, set_tracing_export_api_key,trace
from schemas.schemas import HotelContext
from simple_agents.aagents import Triage_Agent
# from openai.types.responses import ResponseTextDeltaEvent
from agents.exceptions import InputGuardrailTripwireTriggered,OutputGuardrailTripwireTriggered
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
Tracing_key = os.getenv('Tracing_key')

async def main():
    set_tracing_export_api_key(Tracing_key)
    with trace(workflow_name="Assi9",disabled=False): 
        try:
            while True:
                try:
                    user_query = input("\nUser: ")
                except EOFError:
                    break

                # Now triage_agent already knows its handoff targets
                output = await Runner.run(starting_agent=Triage_Agent, input=user_query,run_config=RunConfig())
                print(output.final_output)
                # async for event in output.stream_events():
                #     if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
                #         print(event.data.delta, end="", flush=True)
        except InputGuardrailTripwireTriggered as e:
            print("Guardrail blocked this input:🔺", e)
        
        except OutputGuardrailTripwireTriggered as e:
            print("Guardrail blocked this output:🔺", e)




asyncio.run(main())
