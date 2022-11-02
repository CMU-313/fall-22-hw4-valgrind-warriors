from asyncio.windows_events import NULL
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

#Missing parameters
#Missing 'studytime' input
def test_predict_score_missStudytime():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/score'
    response = client.get(url_for(url), 
                          headers=[('studytime', NULL),('failures', '2'), ('Dalc', '4'),
                                    ('Walc', '3'), ('health', '5'), ('absences','10'),
                                    ('G1', '17'), ('G2', '18')]) 
    assert response.status_code == 400

#Missing 'failure' input
def test_predict_score_missFailure():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/score'
    response = client.get(url_for(url), 
                          headers=[('studytime', '1'), ('failures', NULL),('Dalc', '4'),
                                    ('Walc', '3'), ('health', '5'), ('absences','10'),
                                    ('G1', '17'), ('G2', '18')]) #missing 'failure' input
    assert response.status_code == 400

#Missing 'G1' input 
def test_predict_score_missG1():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/score'
    response = client.get(url_for(url), 
                          headers=[('studytime', '1'), ('failures', '2'), ('Dalc', '4'),
                                    ('Walc', '1'), ('health', '5'), ('absences','10'),
                                    ('G1', NULL),('G2', '18')]) 
    assert response.status_code == 400

#Missing 'G2' input
def test_predict_score_missG2():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/score'
    response = client.get(url_for(url), 
                          headers=[('studytime', '1'), ('failures', '2'), ('Dalc', '4'),
                                    ('Walc', '1'), ('health', '5'), ('absences','10'),
                                    ('G1', '18'), ('G2', NULL)]) 
    assert response.status_code == 400

#Missing 'health' input 
def test_predict_score_missHealth():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/score'
    response = client.get(url_for(url), 
                          headers=[('studytime', '1'), ('failures', '2'), ('Dalc', '4'),
                                    ('Walc', '1'), ('health', NULL),('absences','10'),
                                    ('G1', '17'),('G2', '18')]) 
    assert response.status_code == 400

#Missing 'absences' input 
def test_predict_score_missAbscences():
    app = Flask(__name__)
    configure_routes(app) 
    client = app.test_client()
    url = '/predict/score'
    response = client.get(url_for(url), 
                          headers=[('studytime', '1'), ('failures', '2'), ('Dalc', '4'),
                                    ('Walc', '1'), ('health', '5'),('absences', NULL),
                                    ('G1', '17'),('G2', '18')]) 
    assert response.status_code == 400

#Missing 'Dalc' input
def test_predict_score_missDalc():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/score'
    response = client.get(url_for(url), 
                          headers=[('studytime', '1'), ('failures', '2'), ('Dalc', NULL),
                                    ('Walc', '1'), ('health', '5'),('absences', '10'),
                                    ('G1', '17'),('G2', '18')]) 
    assert response.status_code == 400



#invalid user input for the parameters 
#Missing 'Walc' input 
def test_predict_score_missWalc():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/score'
    response = client.get(url_for(url), 
                          headers=[('studytime', '1'), ('failures', '2'),('Dalc', '4'),
                                    ('health', '5'), ('absences','10'),
                                    ('G1', '18'), ('G2', '19')]) 
    assert response.status_code == 400

#invalid user input for incorrect Walc - 0 value
def test_predict_score_failWalcZero():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/score'
    response = client.get(url_for(url), 
                          headers=[('studytime', '1'), ('failures', '1'),('Dalc', '4'),
                                    ('Walc', '0'), ('health', '5'), ('absences','10'),
                                    ('G1', '17'), ('G2', '18')]) #'Walc' input is 0
    assert response.status_code == 400

#invalid user input for incorrect Walc - greater than 5 value
def test_predict_score_failWalcGreater():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/score'
    response = client.get(url_for(url), 
                          headers=[('studytime', '1'), ('failures', '2'),('Dalc', '4'),
                                    ('Walc', '6'), ('health', '5'), ('absences','10'),
                                    ('G1', '17'), ('G2', '18')]) #'Walc' input is 6
    assert response.status_code == 400

#invalid user input for incorrect absences - greater than 93
def test_predict_score_failAbsencesGreater():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/score'
    response = client.get(url_for(url), 
                          headers=[('studytime', '1'), ('failures', '2'),('Dalc', '4'),
                                    ('Walc', '5'), ('health', '5'), ('absences','94'),
                                    ('G1', '17'), ('G2', '18')]) #'absences' input is 94
    assert response.status_code == 400

#invalid user input for incorrect G1 - greater than 20
def test_predict_score_failG1Greater():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/score'
    response = client.get(url_for(url), 
                          headers=[('studytime', '1'), ('failures', '2'),('Dalc', '4'),
                                    ('Walc', '5'), ('health', '5'), ('absences','10'),
                                    ('G1', '21'), ('G2', '18')]) #'G1' input is 21
    assert response.status_code == 400

#invalid user input for incorrect G2 - greater than 20
def test_predict_score_failG2Greater():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/score'
    response = client.get(url_for(url), 
                          headers=[('studytime', '1'), ('failures', '2'),('Dalc', '4'),
                                    ('Walc', '5'), ('health', '5'), ('absences','10'),
                                    ('G1', '17'), ('G2', '21')]) #'G2' input is 21
    assert response.status_code == 400

#negative user input for studytime
def test_predict_score_failNegStudytime():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/score'
    response = client.get(url_for(url), 
                          headers=[('studytime', '-1'), ('failures', '2'),('Dalc', '4'),
                                    ('Walc', '5'), ('health', '5'), ('absences','10'),
                                    ('G1', '17'), ('G2', '18')]) #'studytime' input is -1
    assert response.status_code == 400

#negative user input for failures
def test_predict_score_failNegFailures():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/score'
    response = client.get(url_for(url), 
                          headers=[('studytime', '1'), ('failures', '-2'),('Dalc', '4'),
                                    ('Walc', '5'), ('health', '5'), ('absences','10'),
                                    ('G1', '17'), ('G2', '18')]) #'failures' input is -2
    assert response.status_code == 400

#negative user input for Dalc
def test_predict_score_failNegDalc():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/score'
    response = client.get(url_for(url), 
                          headers=[('studytime', '1'), ('failures', '2'),('Dalc', '-4'),
                                    ('Walc', '5'), ('health', '5'), ('absences','10'),
                                    ('G1', '17'), ('G2', '18')]) #'Dalc'input is -4 
    assert response.status_code == 400

#negative user input for Walc
def test_predict_score_failNegWalc():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/score'
    response = client.get(url_for(url), 
                          headers=[('studytime', '1'), ('failures', '2'),('Dalc', '4'),
                                    ('Walc', '-5'), ('health', '5'), ('absences','10'),
                                    ('G1', '17'), ('G2', '18')]) #'Walc' input is -5
    assert response.status_code == 400

#negative user input for health
def test_predict_score_failNegHealth():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/score'
    response = client.get(url_for(url), 
                          headers=[('studytime', '1'), ('failures', '2'),('Dalc', '4'),
                                    ('Walc', '5'), ('health', '-5'), ('absences','10'),
                                    ('G1', '17'), ('G2', '18')]) #'health' input is -5
    assert response.status_code == 400

#negative user input for absences
def test_predict_score_failNegAbsences():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/score'
    response = client.get(url_for(url), 
                          headers=[('studytime', '1'), ('failures', '2'),('Dalc', '4'),
                                    ('Walc', '5'), ('health', '5'), ('absences','-10'),
                                    ('G1', '17'), ('G2', '18')]) #'absences' input is -10
    assert response.status_code == 400

#negative user input for G1
def test_predict_score_failNegG1():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/score'
    response = client.get(url_for(url), 
                          headers=[('studytime', '1'), ('failures', '2'),('Dalc', '4'),
                                    ('Walc', '5'), ('health', '5'), ('absences','10'),
                                    ('G1', '-17'), ('G2', '18')]) #'G1' input is -17
    assert response.status_code == 400

#negative user input for G2
def test_predict_score_failNegG2():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/score'
    response = client.get(url_for(url), 
                          headers=[('studytime', '1'), ('failures', '2'),('Dalc', '4'),
                                    ('Walc', '5'), ('health', '5'), ('absences','10'),
                                    ('G1', '17'), ('G2', '-18')]) #'G2' input is -18
    assert response.status_code == 400
    
#successful user input - checking decision value is 'yes' or 'no'
def test_predict_decision():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/decision'

    response = client.get(url_for(url), 
                          headers = [('studytime', '4'), ('failures', '1'), ('Dalc', '4'),
                                    ('Walc', '3'), ('health', '3'), ('absences','8'),
                                    ('G1', '17'), ('G2', '18')])
    assert response.status_code == 200 
    decision = (str)(json.loads(response.data.decode('utf-8').get('decision')))
    assert decision == "yes" or decision == "no"

#Missing parameters 
#Missing parameter G1
def test_predict_decision_failG1():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/decision'
    response = client.get(url_for(url), 
                          headers = [('studytime', '4'), ('failures', '1'), ('Dalc', '4'),
                                    ('Walc', '3'), ('health', '3'), ('absences','8'),
                                    ('G2', '18')])
    assert response.status_code == 200 

#invalid user input for the parameters 
#studytime greater than 4 -- invalid 
def test_predict_decision_failStudytimeGreater():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/score'
    response = client.get(url_for(url), 
                          headers=[('studytime', '5'),('failures', '2'), ('Dalc', '4'),
                                    ('Walc', '3'), ('health', '5'), ('absences','10'),
                                    ('G1', '17'), ('G2', '18')]) 
    assert response.status_code == 400

#failures greater than 4 - invalid 
def test_predict_decision_failFailureGreater():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/score'
    response = client.get(url_for(url), 
                          headers=[('studytime', '1'),('failures', '5'), ('Dalc', '4'),
                                    ('Walc', '3'), ('health', '5'), ('absences','10'),
                                    ('G1', '17'), ('G2', '18')]) 
    assert response.status_code == 400

#dalc greater than 5- invalid 
def test_predict_decision_failDalcGreater():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/score'
    response = client.get(url_for(url), 
                          headers=[('studytime', '1'),('failures', '2'), ('Dalc', '7'),
                                    ('Walc', '3'), ('health', '5'), ('absences','10'),
                                    ('G1', '17'), ('G2', '18')]) 
    assert response.status_code == 400

#health greater than 5- invalid 
def test_predict_decision_failHealthGreater():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/score'
    response = client.get(url_for(url), 
                          headers=[('studytime', '1'),('failures', '2'), ('Dalc', '4'),
                                    ('Walc', '3'), ('health', '8'), ('absences','10'),
                                    ('G1', '17'), ('G2', '18')]) 
    assert response.status_code == 400
