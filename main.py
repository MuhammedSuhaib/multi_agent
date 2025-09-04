from agents import Runner, Agent, ModelSettings
import asyncio
import os
from dotenv import load_dotenv
from configs.config import model_config

load_dotenv()
Tracing_key = os.getenv("Tracing_key")


# Triage Agent — decides who should handle the query
Triage_Agent = Agent(
    name="Triage_Agent", instructions="reply in 1 word", model=model_config
)

new_agent = Triage_Agent.clone(name="NewAgent")
print(id(Triage_Agent))
print(id(new_agent))
#  ----------------------- Agents

print("old_agent : ", Triage_Agent)
print("\n\n====================================\n\n")
print("new Agent : ", new_agent)

#  ----------------------- Prints
print(Triage_Agent.model_settings)
print("====================================")


#  ----------------------- Runner
async def main():
    output = await Runner.run(
        starting_agent=Triage_Agent,
        input="hi",
    )
    print(output.final_output)


asyncio.run(main())
