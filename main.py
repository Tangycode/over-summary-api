from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schemas import OverSummaryRequest
from services import build_over_summary, validate_ball_events

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Over Summary API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/overs/summary")
def over_summary(request: OverSummaryRequest):
    if not request.innings_id:
        raise HTTPException(status_code=400, detail="Missing innings_id")

    if not request.ball_events:
        raise HTTPException(status_code=400, detail="ball_events cannot be empty")

    try:
        validate_ball_events(request.ball_events)
        overs = build_over_summary(request.ball_events)

        return {
            "innings_id": request.innings_id,
            "overs": overs
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
