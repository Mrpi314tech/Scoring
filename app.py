from flask import Flask, render_template, Response, send_from_directory
import time
import importlib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def get_numbers():
    import random
    import time
    import database as db
    switch=db.switch
    team1=db.team1
    team2=db.team2
    rounds=db.rounds
    inning=db.inning
    sound=1
    trigger=switch
    while True:
        importlib.reload(db)
        switch=db.switch
        team1=db.team1
        team2=db.team2
        rounds=db.rounds
        title=db.title
        ad1=db.ad1
        inning=db.inning
        if not switch==trigger:
            sound=1
            trigger=switch
            print(str(sound))
        else:
            sound=0
        yield f"data: {team1},{team2},{switch},{rounds},{title},{ad1},{sound},{inning}\n\n"
        time.sleep(5)

@app.route('/numbers')
def stream():
    return Response(get_numbers(), mimetype='text/event-stream')

@app.route('/home')
def homepage():
    return render_template('home.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
