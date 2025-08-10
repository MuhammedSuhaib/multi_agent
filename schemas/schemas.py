# schemas\schemas.py

# ✅ Pydantic is used for input validation and schema generation.
from pydantic import BaseModel

class SubtractInput(BaseModel):
    a: int
    b: int

class MathOutput(BaseModel):
    isMath:bool
    reason:str

class Guardrail_Output(BaseModel):
    is_querry_about_hotel_laurel:bool
    reason:str
# 🔸 Pydantic validates input data at runtime and throws clear errors.
# 🔸 It can also serialize/deserialize and generate OpenAPI/JSON schema — required by tools.

# Dataclass provides basic structure but no validation.
# from dataclasses import dataclass
# @dataclass
# class SubtractInput:
#     a: int
#     b: int

# 🔸 Dataclass is lightweight and useful for plain data containers,
#     but it does not validate types at runtime or generate JSON schema.
# 🔸 You'd have to manually check data types if using dataclass.