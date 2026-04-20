from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any

from over_summary_service import generate_over_summary

app = FastAPI()

# -------------------------------
# Request Schema (Integration-Ready)
# -------------------------------

class BallEvent(BaseModel):
    ball: float  # e.g., 0.1, 0.2
    runs_off_bat: int
    extras: int
    extra_type: str | None = None  # wide, no_ball, bye, leg_bye, None
    wicket: bool = False

class OverInput(BaseModel):
    match_id: str
    innings: int
    over_number: int
    balls: List[BallEvent]

# -------------------------------
# Route Layer (Thin Controller)
# -------------------------------

@app.post("/over-summary")
def over_summary(input_data: OverInput):
    """
    Integration-ready endpoint:
    - Accepts structured payload (not hardcoded data)
    - Delegates computation to service layer
    - Returns frontend-ready response
    """
    try:
        summary = generate_over_summary(input_data.dict())
        return {
            "status": "success",
            "data": summary
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
