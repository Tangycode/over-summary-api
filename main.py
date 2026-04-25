from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schemas import OverSummaryRequest
from services import build_over_summary

app = FastAPI()

# CORS (required for frontend)
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
def get_over_summary(request: OverSummaryRequest):
    if not request.innings_id:
        raise HTTPException(status_code=400, detail="innings_id is required")

    if not request.ball_events or len(request.ball_events) == 0:
        raise HTTPException(status_code=400, detail="ball_events cannot be empty")

    try:
        result = build_over_summary(request.ball_events)
        return {
            "innings_id": request.innings_id,
            "overs": result
        }
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
