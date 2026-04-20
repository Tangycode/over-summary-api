from typing import Dict, Any, List

# ----------------------------------------
# Core Business Logic Layer
# ----------------------------------------

def generate_over_summary(over_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Converts raw ball events into an over summary.
    
    This function is completely decoupled from FastAPI routes,
    making it reusable for:
    - Django backend calls
    - Batch processing pipelines
    - Future analytics modules
    """

    balls: List[Dict[str, Any]] = over_data["balls"]

    total_runs = 0
    total_wickets = 0
    legal_deliveries = 0

    extras_breakdown = {
        "wides": 0,
        "no_balls": 0,
        "byes": 0,
        "leg_byes": 0
    }

    ball_summaries = []

    for ball in balls:
        runs = ball["runs_off_bat"]
        extras = ball["extras"]
        extra_type = ball.get("extra_type")
        wicket = ball.get("wicket", False)

        # Total runs includes bat + extras
        total_runs += runs + extras

        # Wicket tracking
        if wicket:
            total_wickets += 1

        # Extras classification
        if extra_type == "wide":
            extras_breakdown["wides"] += extras
        elif extra_type == "no_ball":
            extras_breakdown["no_balls"] += extras
        elif extra_type == "bye":
            extras_breakdown["byes"] += extras
        elif extra_type == "leg_bye":
            extras_breakdown["leg_byes"] += extras

        # Legal delivery check (wides and no-balls are NOT legal)
        if extra_type not in ["wide", "no_ball"]:
            legal_deliveries += 1

        # Ball-by-ball representation (frontend-friendly)
        ball_summary = {
            "ball": ball["ball"],
            "runs": runs,
            "extras": extras,
            "extra_type": extra_type,
            "wicket": wicket,
            "total": runs + extras
        }

        ball_summaries.append(ball_summary)

    return {
        "match_id": over_data["match_id"],
        "innings": over_data["innings"],
        "over_number": over_data["over_number"],
        "total_runs": total_runs,
        "wickets": total_wickets,
        "legal_deliveries": legal_deliveries,
        "extras": extras_breakdown,
        "balls": ball_summaries
    }
