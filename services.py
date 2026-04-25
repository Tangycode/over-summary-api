from typing import List, Dict

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

    return list(sorted(overs.values(), key=lambda x: x["over_number"]))
