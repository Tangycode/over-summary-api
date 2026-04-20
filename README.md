# over-summary-api
The Over Summary API processes ball-by-ball cricket data for a single over and returns a structured summary including total runs, wickets, extras breakdown, legal deliveries, and a ball-level breakdown. The API is designed to be integration-ready for the Khel AI MVP, accepting real payloads from backend systems and returning frontend-consumable JSON without any transformation.

Features
Accepts structured ball-by-ball input
Calculates:
Total runs
Wickets
Legal deliveries
Extras breakdown (wides, no-balls, byes, leg byes)
Provides ball-level breakdown for UI rendering
Stateless and integration-ready design
Clean separation of route and service logic
Endpoint

POST /over-summary

Request
{
  "match_id": "match_123",
  "innings": 1,
  "over_number": 5,
  "balls": [
    {
      "ball": 5.1,
      "runs_off_bat": 4,
      "extras": 0,
      "extra_type": null,
      "wicket": false
    }
  ]
}
Response
{
  "status": "success",
  "data": {
    "match_id": "match_123",
    "innings": 1,
    "over_number": 5,
    "total_runs": 10,
    "wickets": 1,
    "legal_deliveries": 6,
    "extras": {
      "wides": 1,
      "no_balls": 0,
      "byes": 0,
      "leg_byes": 0
    },
    "balls": []
  }
}
