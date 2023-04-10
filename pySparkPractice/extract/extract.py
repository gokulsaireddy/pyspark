'''

fact.player_performance
-player_id (FK):dim.player_details
-match_id (FK): dim.match_details
RunsScored: The total runs scored by the player in the match.
WicketsTaken: The total number of wickets taken by the player in the match.
CatchesTaken: The total number of catches taken by the player in the match.
StumpingsMade: The total number of stumpings made by the player in the match.
InningsBatted: The number of innings batted by the player in the match.
InningsBowled: The number of innings bowled by the player in the match.
100s: The number of centuries (100 runs or more in a single innings) scored by the player in the match.
50s: The number of half-centuries (50 runs or more in a single innings) scored by the player in the match.
4s: The total number of fours hit by the player in the match.
6s: The total number of sixes hit by the player in the match.
BattingAVG: The batting average of the player in the match.
BattingS/R: The batting strike rate of the player in the match.
BowlingAVG: The bowling average of the player in the match.
EconomyRate: The economy rate of the player in the match.

dim.player_info
- id
- player_name
- player_url
- full_name
- date_id
- national_side
- matches_played

dim.date
- id
- day
- month
- year
- age
- birth_place
- state
- country
- continent

dim.batting
- player_id

'''
file_name = r'C:\Users\GokulReddy\PycharmProjects\pySparkPractice\data\ICRISAT-crops.csv'

