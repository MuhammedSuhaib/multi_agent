from agents import Runner, set_tracing_export_api_key,trace
from simple_agents.aagents import BotAgent
from agents.exceptions import InputGuardrailTripwireTriggered,OutputGuardrailTripwireTriggered
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
Tracing_key = os.getenv('Tracing_key')

async def main():
    set_tracing_export_api_key(Tracing_key)

    with trace(workflow_name="Assignment6",disabled=False): 
        try:
            while True:
                try:
                    user_query = input("\nUser: ")
                except EOFError:
                    break

                # Now triage_agent already knows its handoff targets
                output = await Runner.run(starting_agent=BotAgent, input=user_query)
                # Logging tool invocations and handoffs
                if hasattr(output, 'tool_invocations'):
                    print("[LOG] Tool invocations:", output.tool_invocations)
                if hasattr(output, 'handoff') and output.handoff:
                    print(f"[LOG] Handoff to: {output.handoff}")
                print(output.final_output)
                # async for event in output.stream_events():
                #     if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
                #         print(event.data.delta, end="", flush=True)
        except InputGuardrailTripwireTriggered as e:
            print("Guardrail blocked this input:🔺", e)
        
        except OutputGuardrailTripwireTriggered as e:
            print("Guardrail blocked this output:🔺", e)




asyncio.run(main())
