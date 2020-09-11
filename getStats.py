import pandas as pd
import matplotlib.pyplot as plt


def runs_filter(cricket):
  # runs dictionary will store data of the form
  # {batsman name: [runs, balls]}
  runs_innings1 = {}
  runs_innings2 = {}


  count_innings1 = 0
  count_innings2 = 0
  for i in range(len(cricket.index)):

    #Innings 1 Batsman scores
    if(cricket.loc[i].at["Innings"] == 1):
      count_innings1 += 1
      if(cricket.loc[i].at["Batsman"] not in runs_innings1):
        runs_innings1[cricket.loc[i].at["Batsman"]] = [0, 1]
        runs_innings1[cricket.loc[i].at["Batsman"]][0] += cricket.loc[i].at["Runs-off-bat"]
      else:
        runs_innings1[cricket.loc[i].at["Batsman"]][0] += cricket.loc[i].at["Runs-off-bat"]
        runs_innings1[cricket.loc[i].at["Batsman"]][1] += 1

    #Innings 2 Batsman scores
    elif(cricket.loc[i].at["Innings"] == 2):
      count_innings2 += 1
      if(cricket.loc[i].at["Batsman"] not in runs_innings2):
        runs_innings2[cricket.loc[i].at["Batsman"]] = [0, 1]
        runs_innings2[cricket.loc[i].at["Batsman"]][0] += cricket.loc[i].at["Runs-off-bat"]
      else:
        runs_innings2[cricket.loc[i].at["Batsman"]][0] += cricket.loc[i].at["Runs-off-bat"]
        runs_innings2[cricket.loc[i].at["Batsman"]][1] += 1

  return (runs_innings1, runs_innings2)

def two_top_scorers_in_each_innings(cricket):
  runs1, runs2 = runs_filter(cricket)
  top_2_run_1 = sorted(runs1.items(), key=lambda kv: (kv[1],kv[0]), reverse=True)[0:2]
  top_2_run_2 = sorted(runs2.items(), key=lambda kv: (kv[1],kv[0]), reverse=True)[0:2]
  return (top_2_run_1, top_2_run_2)

def bowlers_data(cricket):
  # bowling_figures dictionary will store data of the form
  # {Bowler: [wickets, runs, balls]}
  bowling_figures1 = {}
  bowling_figures2 = {}
  for i in range(len(cricket.index)):

    # Innings 1 Bowlers
    if (cricket.loc[i].at["Innings"] == 1):

      if (cricket.loc[i].at["Bowler"] not in bowling_figures1):
        bowling_figures1[cricket.loc[i].at["Bowler"]] = [0, 0, 0]
        bowling_figures1[cricket.loc[i].at["Bowler"]][1] += cricket.loc[i].at["Runs-off-bat"]
        bowling_figures1[cricket.loc[i].at["Bowler"]][2] += 1
        if (pd.notna(cricket.loc[i].at["Kind of wicket"]) and cricket.loc[i].at["Kind of wicket"] != "run out"):
          bowling_figures1[cricket.loc[i].at["Bowler"]][0] += 1
      else:
        bowling_figures1[cricket.loc[i].at["Bowler"]][1] += cricket.loc[i].at["Runs-off-bat"]
        bowling_figures1[cricket.loc[i].at["Bowler"]][2] += 1
        if (pd.notna(cricket.loc[i].at["Kind of wicket"]) and cricket.loc[i].at["Kind of wicket"] != "run out"):
          bowling_figures1[cricket.loc[i].at["Bowler"]][0] += 1


    elif (cricket.loc[i].at["Innings"] == 2):

      if (cricket.loc[i].at["Bowler"] not in bowling_figures2):
        bowling_figures2[cricket.loc[i].at["Bowler"]] = [0, 0, 0]
        bowling_figures2[cricket.loc[i].at["Bowler"]][1] += cricket.loc[i].at["Runs-off-bat"]
        bowling_figures2[cricket.loc[i].at["Bowler"]][2] += 1
        if (pd.notna(cricket.loc[i].at["Kind of wicket"]) and cricket.loc[i].at["Kind of wicket"] != "run out"):
          bowling_figures2[cricket.loc[i].at["Bowler"]][0] += 1
      else:
        bowling_figures2[cricket.loc[i].at["Bowler"]][1] += cricket.loc[i].at["Runs-off-bat"]
        bowling_figures2[cricket.loc[i].at["Bowler"]][2] += 1
        if (pd.notna(cricket.loc[i].at["Kind of wicket"]) and cricket.loc[i].at["Kind of wicket"] != "run out"):
          bowling_figures2[cricket.loc[i].at["Bowler"]][0] += 1


  return (bowling_figures1, bowling_figures2)


def cumulative_runs_per_ball(cricket):
  cumulative_runs_1 = []
  runs1 = 0

  cumulative_runs_2 = []
  runs2 = 0
  for i in range(len(cricket.index)):
    if(cricket.loc[i].at["Innings"] == 1):
      runs1 += cricket.loc[i].at["Runs-off-bat"] + cricket.loc[i].at["Extras"]
      cumulative_runs_1.append(runs1)

    if(cricket.loc[i].at["Innings"] == 2):
      runs2 += cricket.loc[i].at["Runs-off-bat"] + cricket.loc[i].at["Extras"]
      cumulative_runs_2.append(runs2)
  return (cumulative_runs_1, cumulative_runs_2)

# Upgradation of runs_filter() function
def batsman_scorecard_inning(cricket):
    # inning1_runs, inning2_runs = runs_filter(cricket)
    runs_innings1 = {}
    runs_innings2 = {}


    count_innings1 = 0
    count_innings2 = 0
    for i in range(len(cricket.index)):
        runs_off_bat = cricket.loc[i].at["Runs-off-bat"]

        #Innings 1 Batsman scores
        if (cricket.loc[i].at["Innings"] == 1):
            count_innings1 += 1

            if (cricket.loc[i].at["Batsman"] not in runs_innings1):
                runs_innings1[cricket.loc[i].at["Batsman"]] = [0, 1, 0, 0, 0.0]
                # Scorecard format : {batsman : [runs, balls, fours, sixes, SR]}

            else:
                runs_innings1[cricket.loc[i].at["Batsman"]][1] += 1

            runs_innings1[cricket.loc[i].at["Batsman"]][0] += runs_off_bat # Adding runs to dict
            sr = (runs_innings1[cricket.loc[i].at["Batsman"]][0]/runs_innings1[cricket.loc[i].at["Batsman"]][1])*100
            runs_innings1[cricket.loc[i].at["Batsman"]][4] = round(sr,2) # Updating strike rate in dict
            if runs_off_bat == 4:
                runs_innings1[cricket.loc[i].at["Batsman"]][2] += 1 # Updating no. of fours
            elif runs_off_bat == 6:
                runs_innings1[cricket.loc[i].at["Batsman"]][3] += 1 # Updating no. of sixes

        # Innings 2 Batsman scores
        elif (cricket.loc[i].at["Innings"] == 2):
            count_innings2 += 1

            if (cricket.loc[i].at["Batsman"] not in runs_innings2):
                runs_innings2[cricket.loc[i].at["Batsman"]] = [0, 1, 0, 0, 0.0]
                # Scorecard format : {batsman : [runs, balls, fours, sixes, SR]}

            else:
                runs_innings2[cricket.loc[i].at["Batsman"]][1] += 1

            runs_innings2[cricket.loc[i].at["Batsman"]][0] += runs_off_bat # Adding runs to dict
            sr = (runs_innings2[cricket.loc[i].at["Batsman"]][0]/runs_innings2[cricket.loc[i].at["Batsman"]][1])*100
            runs_innings2[cricket.loc[i].at["Batsman"]][4] = round(sr,2) # Updating strike rate in dict
            if runs_off_bat == 4:
                runs_innings2[cricket.loc[i].at["Batsman"]][2] += 1 # Updating no. of fours
            elif runs_off_bat == 6:
                runs_innings2[cricket.loc[i].at["Batsman"]][3] += 1 # Updating no. of sixes

    return runs_innings1, runs_innings2

# To get partnership runs data of each batsmen pair
def partnerships(cricket):
    partnerships_1 = {}
    partnerships_2 = {}
    # Format: {(batsman1, batsman2): [runs, balls]}
    for i in range(len(cricket.index)):
        runs_off_bat_and_extras = cricket.loc[i].at["Runs-off-bat"] + cricket.loc[i].at["Extras"]

        if cricket.loc[i].at["Innings"] == 1:
            batsmen = tuple(sorted([cricket.loc[i].at["Batsman"], cricket.loc[i].at["Non-striker"]]))

            if batsmen not in partnerships_1:
                partnerships_1[batsmen] = [0, 1]

            else:
                partnerships_1[batsmen][1] += 1

            partnerships_1[batsmen][0] += runs_off_bat

        elif cricket.loc[i].at["Innings"] == 2:
            batsmen = tuple(sorted([cricket.loc[i].at["Batsman"], cricket.loc[i].at["Non-striker"]]))

            if batsmen not in partnerships_2:
                partnerships_2[batsmen] = [0, 1]

            else:
                partnerships_2[batsmen][1] += 1

            partnerships_2[batsmen][0] += runs_off_bat

    return partnerships_1, partnerships_2

def runs_per_over(cricket):
    runs1 = [[0, i] for i in range(1,51)]
    runs2 = [[0, i] for i in range(1,51)]

    # Format : [runs, over]
    for i in range(len(cricket.index)):
        runs_off_bat_and_extras = cricket.loc[i].at["Runs-off-bat"] + cricket.loc[i].at["Extras"]

        if cricket.loc[i].at["Innings"] == 1:
            over = int(str(cricket.loc[i].at["Over.ball"]).split(".")[0])
            runs1[over][0] += runs_off_bat_and_extras

        elif cricket.loc[i].at["Innings"] == 2:
            over = int(str(cricket.loc[i].at["Over.ball"]).split(".")[0])
            runs2[over][0] += runs_off_bat_and_extras

    return runs1, runs2

def match_manhattan(cricket):
    runs1, runs2 = runs_per_over(cricket)
    import numpy as np
    import matplotlib.pyplot as plt

    # innings 1
    height1 = [runs1[i][0] for i in range(50)]
    bars1 = [runs1[i][1] for i in range(50)]
    # print(height)
    # print(bars)
    y_pos = np.arange(len(bars))

    # Create bars
    plt.bar(y_pos, height)

    # Create names on the x-axis
    # plt.xticks(y_pos, bars)

    plt.xlabel('overs')
    plt.ylabel('runs')
    plt.title('plotted overs and runs')

    plt.savefig("plot.png", dpi= 300, bbox_inches = "tight")
    # Show graphic
    plt.show()
