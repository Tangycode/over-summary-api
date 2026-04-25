from pydantic import BaseModel, Field
from typing import List, Optional

class BallEvent(BaseModel):
    over: int = Field(..., ge=0)
    ball_in_over: int = Field(..., ge=1, le=6)
    over_ball: str
    striker: str
    bowler: str
    runs: int = Field(..., ge=0)
    extras: int = Field(..., ge=0)
    wicket: int = Field(..., ge=0, le=1)

class OverSummaryRequest(BaseModel):
    innings_id: str
    ball_events: List[BallEvent]
