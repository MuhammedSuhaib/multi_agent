# schemas\schemas.py

# ✅ Pydantic is used for input validation and schema generation.
from pydantic import BaseModel

class SubtractInput(BaseModel):
    a: int
    b: int

class Guardrail_Output(BaseModel):
    is_querry_about_hotel:bool
    is_querry_related_to_account_and_tax:bool
    reason:str

class HotelContext(BaseModel):
    hotel_name: str | None = None


class SomeDynamicInfo(BaseModel):
    name: str
    uid: int
    agent: str

# 🔸 Pydantic validates input data at runtime and throws clear errors.
# 🔸 It can also serialize*/deserialize and generate OpenAPI/JSON schema — required by tools.

# Dataclass provides basic structure but no validation.
# from dataclasses import dataclass
# @dataclass
# class SubtractInput:
#     a: int
#     b: int

# 🔸 Dataclass is lightweight and useful for plain data containers,
#     but it does not validate types at runtime or generate JSON schema.
# 🔸 You'd have to manually check data types if using dataclass.

# * converting an object's state or a data structure into a format that can be stored or transmitted.
