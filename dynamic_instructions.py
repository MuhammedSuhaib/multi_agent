from agents import Agent, RunContextWrapper
from schemas.schemas import HotelContext

# Extract hotel name from query
def extract_hotel_name(user_input: str) -> str | None:
    words = user_input.lower().split()
    for i, w in enumerate(words):
        if "hotel" in w and i > 0:
            return words[i - 1].capitalize() + " Hotel"
    return None


def dynamic_instructions(ctx: RunContextWrapper[HotelContext], agent: Agent) -> str:
    hotel_name = ctx.context.hotel_name or "Unknown Hotel"
    return f"""
    You are a helpful hotel assistant.
    - There are 99 rooms in our hotel.
    - Hotel name is {hotel_name}.
    - Hotel owner name is "Ali Sheikhani".
    - 9 of those rooms are luxury rooms (high cost).
    - 10 of those are basic rooms (low cost).
    - The rest are standard rooms (medium cost).
    """
