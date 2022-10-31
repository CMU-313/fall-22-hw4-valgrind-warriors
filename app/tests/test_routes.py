from random import randrange
from flask import Flask, url_for
import json
from app.handlers.routes import configure_routes


def test_base_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)

    assert response.status_code == 200
    assert response.get_data() == b'welcome to ML microservice'

#successful user input - checking score value in range
def test_predict_score():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/score'
    response = client.get(url_for(url), 
                          headers=[('studytime', '1'), ('failures', '2'), ('Dalc', '4'),
                                    ('Walc', '3'), ('health', '5'), ('absences','10'),
                                    ('G1', '17'), ('G2', '18')])
    assert response.status_code == 200
    score = (int)(json.loads(response.data.decode('utf-8')).get("G3"))
    assert (0 <= score and score <= 20)

#invaild user input for missing 'studytime' input
def test_predict_score_failStudytime():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/score'
    response = client.get(url_for(url), 
                          headers=[('failures', '2'), ('Dalc', '4'),
                                    ('Walc', '3'), ('health', '5'), ('absences','10'),
                                    ('G1', '17'), ('G2', '18')]) 
    assert response.status_code == 400

#invaild user input for missing 'failure' input
def test_predict_score_failFailure():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/score'
    response = client.get(url_for(url), 
                          headers=[('studytime', '1'), ('Dalc', '4'),
                                    ('Walc', '3'), ('health', '5'), ('absences','10'),
                                    ('G1', '17'), ('G2', '18')]) #missing 'failure' input
    assert response.status_code == 400

#invaild user input for missing G1 input 
def test_predict_score_failG1():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/score'
    response = client.get(url_for(url), 
                          headers=[('studytime', '1'), ('Dalc', '4'),
                                    ('Walc', '1'), ('health', '5'), ('absences','10'),
                                    ('G2', '18')]) #'Walc' input is negative
    assert response.status_code == 400

#invaild user input for incorrect Walc - 0 value
def test_predict_score_failWalcZero():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/score'
    response = client.get(url_for(url), 
                          headers=[('studytime', '1'), ('Dalc', '4'),
                                    ('Walc', '0'), ('health', '5'), ('absences','10'),
                                    ('G1', '17'), ('G2', '18')]) #'Walc' input is 0
    assert response.status_code == 400

#invaild user input for incorrect Walc - greater than 5 value
def test_predict_score_failWalcGreater():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/score'
    response = client.get(url_for(url), 
                          headers=[('studytime', '1'), ('Dalc', '4'),
                                    ('Walc', '6'), ('health', '5'), ('absences','10'),
                                    ('G1', '17'), ('G2', '18')]) #'Walc' input is 6
    assert response.status_code == 400


    
#successful user input - checking decision value is 'yes' or 'no'
def test_predict_decision():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/decision'

    #TODO: complete this test
    response = client.get(url_for(url), 
                          headers = [('studytime', '4'), ('failures', '1'), ('Dalc', '4'),
                                    ('Walc', '3'), ('health', '3'), ('absences','8'),
                                    ('G1', '17'), ('G2', '18')])
    assert response.status_code = 200 
    decision = (str)(json.loads(response.data.decode('utf-8').get('decision')))
    assert decision == "yes" or decision == "no"
