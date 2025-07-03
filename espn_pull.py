from espn_api.football import League

# === REPLACE THESE WITH YOUR INFO ===
league_id = 384948  # Example: 1234567
year = 2025
espn_s2 = "AEBV2pEC40S8ozcxRHG0fEaLLikALabRclK9R75zjgMV0YfSBaSsV%2FQr1jAYef8hqaR7FV4BwFN6MbmiLkbJGGRwe%2BSzabJpWCmqV6WigWV8PMp%2F5qkIeNVdjW0Ql%2BBmQtShHOzIYkB2I4p%2BOaSj4cCsvmj6Oy74jCgnv6wl04gMtuLhxwjKuAZ3gGa3Tv5qmGCAum%2FErh7KwbTyJzM2IIzZyYVd828taoDN6jMgeDFM2OstZRYJdQukxBYnsKxov37w7bvgxqcbp7fAkCxdswIAH4%2BwHV%2BOEe3qpk1reFpVJg%3D%3D"
swid = "{25227FB2-135C-4A96-BD59-DE4C3B2CB182}"  # includes the curly braces

# === Connect to your ESPN league ===
league = League(league_id=league_id, year=year, espn_s2=espn_s2, swid=swid)

# === Print current standings ===
print("\n🏆 STANDINGS:")
for team in league.teams:
    print(f"{team.team_name}: {team.wins}-{team.losses} ({team.points_for:.1f} pts)")
