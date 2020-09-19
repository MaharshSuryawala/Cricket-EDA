import pandas as pd
import requests


# To get CSV file of a particular match
def get_data(league_id, event_id):
    # Columns of the csv
    data_final = pd.DataFrame(columns=['id', 'ball', 'over', 'runs', 'shortText', 'text', 'preText', 'postText',
                                       'isWide', 'isNoball', 'isRetiredHurt', 'isBoundary', 'currentBatsmen',
                                       'currentBowlers', 'currentInning.id', 'currentInning.balls',
                                       'currentInning.runs', 'currentInning.wickets', 'matchOver.maiden',
                                       'matchOver.runs', 'matchOver.wickets', 'matchOver.totalRuns',
                                       'matchOver.totalWicket', 'matchOver.runRate', 'matchOver.requiredRunRate',
                                       'matchOver.batsmen', 'matchOver.bowlers', 'matchOver.teamShortName',
                                       'matchOver.remainingOvers', 'matchOver.remainingBalls',
                                       'matchOver.remainingRuns'])
    for inning in range(1, 3):
        print(inning)
        page = 1
        while True:
            url = "https://hsapi.espncricinfo.com/v1/pages/match/comments?lang=en&leagueId=" + str(league_id) + \
                  "&eventId=" + str(event_id) + "&period=" + str(inning) + "&page=" + str(page)
            response = requests.get(url)
            data = response.json()
            if data["comments"] == []:
                break
            flatten_json = pd.json_normalize(data["comments"])
            data_final = data_final.append(flatten_json)
            page = page + 1

    data_final = data_final.reset_index(drop=True)
    data_final = data_final.to_csv(f"{league_id}_{event_id}.csv")

    return data_final
