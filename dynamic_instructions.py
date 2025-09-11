from agents import Agent, RunContextWrapper, Runner, function_tool
from configs.config import model_config
from schemas.schemas import UserInfo

user_info = UserInfo(name="stucked", uid=4334)


@function_tool
def info(ctx: RunContextWrapper[UserInfo]) -> str:
    """Get the info of the user from the context."""
    return f"{ctx.context.name}, 47 , {ctx.context.uid}"

agent = Agent[UserInfo](
    name="Assistant",
    instructions="You are a helpful assistant. use the user_info tool to get information about the user.",
    tools=[info],
    model=model_config,
)
result = Runner.run_sync(
    agent,
    "give me user info: name",
    context=user_info,
)

print(result.final_output)
