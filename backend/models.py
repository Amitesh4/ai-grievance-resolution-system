from pydantic import BaseModel
from typing import Optional


class Grievance(BaseModel):
    title: str
    description: str
    location: Optional[str] = None
