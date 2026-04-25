from typing import List, Dict

def validate_ball_events(ball_events: List[Dict]):
    seen = set()

    for ball in ball_events:
        key = (ball["over"], ball["ball_in_over"])

        # Duplicate check
        if key in seen:
            raise ValueError(f"Duplicate ball detected: over {ball['over']} ball {ball['ball_in_over']}")
        seen.add(key)

        # Over-ball consistency check
        expected = f"{ball['over']}.{ball['ball_in_over']}"
        if ball["over_ball"] != expected:
            raise ValueError(f"Mismatch in over_ball format: expected {expected}")

        # Logical constraints
        if ball["runs"] < 0 or ball["extras"] < 0:
            raise ValueError("Runs or extras cannot be negative")

        if ball["ball_in_over"] > 6:
            raise ValueError(f"Invalid ball number: {ball['ball_in_over']} in over {ball['over']}")

    # Ensure sorted sequence
    sorted_events = sorted(ball_events, key=lambda x: (x["over"], x["ball_in_over"]))
    if ball_events != sorted_events:
        raise ValueError("Ball events must be in chronological order")


def build_label(ball: Dict) -> str:
    label = f"{ball['over_ball']} - {ball['striker']} vs {ball['bowler']} : {ball['runs']} run(s)"
    if ball["extras"] > 0:
        label += f" + {ball['extras']} extra(s)"
    if ball["wicket"] == 1:
        label += " | WICKET"
    return label


def build_over_summary(ball_events: List[Dict]) -> List[Dict]:
    overs = {}

    for ball in ball_events:
        over = ball["over"]

        if over not in overs:
            overs[over] = {
                "over_number": over,
                "runs_in_over": 0,
                "wickets_in_over": 0,
                "extras_in_over": 0,
                "balls": []
            }

        overs[over]["runs_in_over"] += ball["runs"]
        overs[over]["wickets_in_over"] += ball["wicket"]
        overs[over]["extras_in_over"] += ball["extras"]

        overs[over]["balls"].append({
            "over_ball": ball["over_ball"],
            "striker": ball["striker"],
            "bowler": ball["bowler"],
            "runs": ball["runs"],
            "extras": ball["extras"],
            "wicket": ball["wicket"],
            "label": build_label(ball)
        })

    return sorted(overs.values(), key=lambda x: x["over_number"])
