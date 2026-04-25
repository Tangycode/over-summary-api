Purpose

Groups innings ball-by-ball data into over-wise summaries.

Endpoint

POST /overs/summary

Input Schema
innings_id (string)
ball_events (array of structured ball objects)

Output Schema
innings_id
overs[] with:
over_number
runs_in_over
wickets_in_over
extras_in_over
balls[]

Validation Errors
Missing innings_id → 400
Empty ball_events → 400
Invalid schema → 400

Integration Notes
Follows Khel AI data shape
Frontend-ready JSON
Supports live match pipelines
