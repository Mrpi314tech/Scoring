import time
import random
def update_data():
    file1 = open("/root/Scoring/database.py", "w")
    file1.write("team1="+str(team1)+"\nteam2="+str(team2)+"\nswitch="+str(switch)+"\nrounds="+str(rounds)+'\ntitle="'+title+'"'+'\nad1="'+ad1+'"'+'\ninning='+str(innings))
    file1.close()
with open("/root/Scoring/input.txt", "r") as inputtxt:
    title=inputtxt.readline().strip()
    ad1=inputtxt.readline().strip()
    wait=inputtxt.readline().strip()
wait=int(wait)
team1=0
team2=0
switch=1
rounds=5
innings=1
update_data()
for i in range(0,6):
    for i in range(0,5):
        time.sleep(wait)
        rounds-=1
        update_data()
    score1=random.choice([-5,5,10,15,20])
    team1+=score1
    switch=0
    rounds=5
    update_data()
    for i in range(0,5):
        time.sleep(wait)
        rounds-=1
        update_data()
    score2=random.choice([-5,5,10,15,20])
    team2+=score2
    switch=1
    rounds=5
    innings+=1
    update_data()
switch=3
rounds="Score"
file1 = open("/root/Scoring/database.py", "w")
file1.write("team1="+str(team1)+"\nteam2="+str(team2)+"\nswitch="+str(switch)+'\nrounds="'+str(rounds)+'"\ntitle="'+title+'"'+'\nad1="'+ad1+'"'+'\ninning='+str(innings))
file1.close()
