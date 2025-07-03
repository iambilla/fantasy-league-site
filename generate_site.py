from espn_api.football import League
from jinja2 import Environment, FileSystemLoader

# Your ESPN league credentials
league = League(
    league_id=384948,  # replace with your league ID
    year=2025,
    espn_s2="AEBV2pEC40S8ozcxRHG0fEaLLikALabRclK9R75zjgMV0YfSBaSsV%2FQr1jAYef8hqaR7FV4BwFN6MbmiLkbJGGRwe%2BSzabJpWCmqV6WigWV8PMp%2F5qkIeNVdjW0Ql%2BBmQtShHOzIYkB2I4p%2BOaSj4cCsvmj6Oy74jCgnv6wl04gMtuLhxwjKuAZ3gGa3Tv5qmGCAum%2FErh7KwbTyJzM2IIzZyYVd828taoDN6jMgeDFM2OstZRYJdQukxBYnsKxov37w7bvgxqcbp7fAkCxdswIAH4%2BwHV%2BOEe3qpk1reFpVJg%3D%3D",
    swid="{25227FB2-135C-4A96-BD59-DE4C3B2CB182}"
)

# Collect team data
teams = []
for team in league.teams:
    teams.append({
        "name": team.team_name,
        "wins": team.wins,
        "losses": team.losses,
        "points": round(team.points_for, 1)
    })

# Setup Jinja2 and render the HTML
env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("standings.html.jinja")
output = template.render(teams=teams)

# Save to index.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(output)

print("✅ Website generated! Open 'index.html' to view your standings.")
