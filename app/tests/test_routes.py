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
    url = 'predict_score'
    with app.app_context(), app.test_request_context():
        data = {
            'studytime': '1',
            'failures': '2',
            'Dalc': '4',
            'Walc': '3',
            'health': '5',
            'absences':'10',
            'G1': '17',
            'G2': '18'
        }
        response = client.get(url_for(url, **data))
        assert response.status_code == 200
        score = (int)(json.loads(response.data.decode('utf-8')).get("G3"))
        assert (0 <= score and score <= 20)



#Missing parameters
#Missing 'studytime' input
def test_predict_score_missStudytime():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'predict_score'
    with app.app_context(), app.test_request_context():
        data = {
            'studytime': None,
            'failures': '2',
            'Dalc': '4',
            'Walc': '3',
            'health': '5',
            'absences':'10',
            'G1': '17',
            'G2': '18'
        }
        response = client.get(url_for(url, **data)) 
        assert response.status_code == 400


#Missing 'failure' input
def test_predict_score_missFailure():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'predict_score'
    with app.app_context(), app.test_request_context():
        data = {
            'studytime': '1',
            'failures': None,
            'Dalc': '4',
            'Walc': '3',
            'health': '5',
            'absences':'10',
            'G1': '17',
            'G2': '18'
        }
        response = client.get(url_for(url, **data)) 
        assert response.status_code == 400 #missing 'failure' input

#Missing 'G1' input 
def test_predict_score_missG1():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'predict_score'
    with app.app_context(), app.test_request_context():
        data = {
            'studytime': '1',
            'failures': '2',
            'Dalc': '4',
            'Walc': '3',
            'health': '5',
            'absences':'10',
            'G1': None,
            'G2': '18'
        }
        response = client.get(url_for(url, **data)) 
        assert response.status_code == 400

#Missing 'G2' input
def test_predict_score_missG2():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'predict_score'
    with app.app_context(), app.test_request_context():
        data = {
            'studytime': '1',
            'failures': '2',
            'Dalc': '4',
            'Walc': '3',
            'health': '5',
            'absences':'10',
            'G1': '17',
            'G2': None
        }
        response = client.get(url_for(url, **data)) 
        assert response.status_code == 400

#Missing 'health' input 
def test_predict_score_missHealth():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'predict_score'
    with app.app_context(), app.test_request_context():
        data = {
            'studytime': '1',
            'failures': '2',
            'Dalc': '4',
            'Walc': '3',
            'health': None,
            'absences':'10',
            'G1': '17',
            'G2': '18'
        }
        response = client.get(url_for(url, **data)) 
        assert response.status_code == 400

#Missing 'absences' input 
def test_predict_score_missAbscences():
    app = Flask(__name__)
    configure_routes(app) 
    client = app.test_client()
    url = 'predict_score'
    with app.app_context(), app.test_request_context():
        data = {
            'studytime': '1',
            'failures': '2',
            'Dalc': '4',
            'Walc': '3',
            'health': '5',
            'absences': None,
            'G1': '17',
            'G2': '18'
        }
        response = client.get(url_for(url, **data)) 
        assert response.status_code == 400

#Missing 'Dalc' input
def test_predict_score_missDalc():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'predict_score'
    with app.app_context(), app.test_request_context():
        data = {
            'studytime': '1',
            'failures': '2',
            'Dalc': None,
            'Walc': '3',
            'health': '5',
            'absences':'10',
            'G1': '17',
            'G2': '18'
        }
        response = client.get(url_for(url, **data)) 
        assert response.status_code == 400



#invalid user input for the parameters 
#Missing 'Walc' input 
def test_predict_score_missWalc():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'predict_score'
    with app.app_context(), app.test_request_context():
        data = {
            'studytime': '1',
            'failures': '2',
            'Dalc': '4',
            'Walc': None,
            'health': '5',
            'absences':'10',
            'G1': '17',
            'G2': '18'
        }
        response = client.get(url_for(url, **data)) 
        assert response.status_code == 400

#invalid user input for incorrect Walc - 0 value
def test_predict_score_failWalcZero():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'predict_score'
    with app.app_context(), app.test_request_context():
        data = {
            'studytime': '1',
            'failures': '2',
            'Dalc': '4',
            'Walc': '0',
            'health': '5',
            'absences':'10',
            'G1': '17',
            'G2': '18'
        }#'Walc' input is 0
        response = client.get(url_for(url, **data)) 
        assert response.status_code == 400 

#invalid user input for incorrect Walc - greater than 5 value
def test_predict_score_failWalcGreater():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'predict_score'
    with app.app_context(), app.test_request_context():
        data = {
            'studytime': '1',
            'failures': '2',
            'Dalc': '4',
            'Walc': '6',
            'health': '5',
            'absences':'10',
            'G1': '17',
            'G2': '18'
        }#'Walc' input is 6
        response = client.get(url_for(url, **data)) 
        assert response.status_code == 400 

#invalid user input for incorrect absences - greater than 93
def test_predict_score_failAbsencesGreater():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'predict_score'
    with app.app_context(), app.test_request_context():
        data = {
            'studytime': '1',
            'failures': '2',
            'Dalc': '4',
            'Walc': '1',
            'health': '5',
            'absences':'94',
            'G1': '17',
            'G2': '18'
        }#'absences' input is 94
        response = client.get(url_for(url, **data)) 
        assert response.status_code == 400

#invalid user input for incorrect G1 - greater than 20
def test_predict_score_failG1Greater():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'predict_score'
    with app.app_context(), app.test_request_context():
        data = {
            'studytime': '1',
            'failures': '2',
            'Dalc': '4',
            'Walc': '1',
            'health': '5',
            'absences':'10',
            'G1': '21',
            'G2': '18'
        }
        response = client.get(url_for(url, **data))  #'G1' input is 21
        assert response.status_code == 400

#invalid user input for incorrect G2 - greater than 20
def test_predict_score_failG2Greater():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'predict_score'
    with app.app_context(), app.test_request_context():
        data = {
            'studytime': '1',
            'failures': '2',
            'Dalc': '4',
            'Walc': '1',
            'health': '5',
            'absences':'10',
            'G1': '17',
            'G2': '21'
        }
        response = client.get(url_for(url, **data))  #'G2' input is 21
        assert response.status_code == 400

#negative user input for studytime
def test_predict_score_failNegStudytime():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'predict_score'
    with app.app_context(), app.test_request_context():
        data = {
            'studytime': '-1',
            'failures': '2',
            'Dalc': '4',
            'Walc': '1',
            'health': '5',
            'absences':'10',
            'G1': '17',
            'G2': '18'
        }
        response = client.get(url_for(url, **data))  #'studytime' input is -1
        assert response.status_code == 400

#negative user input for failures
def test_predict_score_failNegFailures():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'predict_score'
    with app.app_context(), app.test_request_context():
        data = {
            'studytime': '1',
            'failures': '-2',
            'Dalc': '4',
            'Walc': '1',
            'health': '5',
            'absences':'10',
            'G1': '17',
            'G2': '18'
        }
        response = client.get(url_for(url, **data))  #'failures' input is -2
        assert response.status_code == 400

#negative user input for Dalc
def test_predict_score_failNegDalc():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'predict_score'
    with app.app_context(), app.test_request_context():
        data = {
            'studytime': '1',
            'failures': '2',
            'Dalc': '-4',
            'Walc': '1',
            'health': '5',
            'absences':'10',
            'G1': '17',
            'G2': '18'
        }
        response = client.get(url_for(url, **data))  #'Dalc'input is -4 
        assert response.status_code == 400

#negative user input for Walc
def test_predict_score_failNegWalc():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'predict_score'
    with app.app_context(), app.test_request_context():
        data = {
            'studytime': '1',
            'failures': '2',
            'Dalc': '4',
            'Walc': '-5',
            'health': '5',
            'absences':'10',
            'G1': '17',
            'G2': '18'
        }#'absences' input is 94
        response = client.get(url_for(url, **data))  #'Walc' input is -5
        assert response.status_code == 400

#negative user input for health
def test_predict_score_failNegHealth():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'predict_score'
    with app.app_context(), app.test_request_context():
        data = {
            'studytime': '1',
            'failures': '2',
            'Dalc': '4',
            'Walc': '1',
            'health': '-5',
            'absences':'10',
            'G1': '17',
            'G2': '18'
        }#'absences' input is 94
        response = client.get(url_for(url, **data)) #'health' input is -5
        assert response.status_code == 400

#negative user input for absences
def test_predict_score_failNegAbsences():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'predict_score'
    with app.app_context(), app.test_request_context():
        data = {
            'studytime': '1',
            'failures': '2',
            'Dalc': '4',
            'Walc': '1',
            'health': '5',
            'absences':'-10',
            'G1': '17',
            'G2': '18'
        }
        response = client.get(url_for(url, **data))  #'absences' input is -10
        assert response.status_code == 400

#negative user input for G1
def test_predict_score_failNegG1():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'predict_score'
    with app.app_context(), app.test_request_context():
        data = {
            'studytime': '1',
            'failures': '2',
            'Dalc': '4',
            'Walc': '1',
            'health': '5',
            'absences':'10',
            'G1': '-17',
            'G2': '18'
        }#'absences' input is 94
        response = client.get(url_for(url, **data))  #'G1' input is -17
        assert response.status_code == 400

#negative user input for G2
def test_predict_score_failNegG2():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'predict_score'
    with app.app_context(), app.test_request_context():
        data = {
            'studytime': '1',
            'failures': '2',
            'Dalc': '4',
            'Walc': '1',
            'health': '5',
            'absences':'10',
            'G1': '17',
            'G2': '-18'
        }#'absences' input is 94
        response = client.get(url_for(url, **data))  #'G2' input is -18
        assert response.status_code == 400
    
#successful user input - checking decision value is 'yes' or 'no'
def test_predict_decision():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'predict_decision'
    with app.app_context(), app.test_request_context():
        data = {
            'studytime': '1',
            'failures': '2',
            'Dalc': '4',
            'Walc': '1',
            'health': '5',
            'absences':'10',
            'G1': '17',
            'G2': '18'
        }
        response = client.get(url_for(url, **data))
        assert response.status_code == 200 
        decision = json.loads(response.data.decode('utf-8')).get('decision')
        assert (decision == "yes" or decision == "no")

#Missing parameters 
#Missing parameter G1
def test_predict_decision_failG1():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'predict_decision'
    with app.app_context(), app.test_request_context():
        data = {
            'studytime': '1',
            'failures': '2',
            'Dalc': '4',
            'Walc': '3',
            'health': '5',
            'absences':'10',
            'G1': None,
            'G2': '18'
        }
        response = client.get(url_for(url, **data)) 
        assert response.status_code == 400

#Missing parameter G2
def test_predict_decision_failG2():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'predict_decision'
    with app.app_context(), app.test_request_context():
        data = {
            'studytime': '1',
            'failures': '2',
            'Dalc': '4',
            'Walc': '3',
            'health': '5',
            'absences':'10',
            'G1': '17',
            'G2': None
        }
        response = client.get(url_for(url, **data)) 
        assert response.status_code == 400

#Missing parameter studytime
def test_predict_decision_failStudytime():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'predict_decision'
    with app.app_context(), app.test_request_context():
        data = {
            'studytime': None,
            'failures': '2',
            'Dalc': '4',
            'Walc': '3',
            'health': '5',
            'absences':'10',
            'G1': '17',
            'G2': '18'
        }
        response = client.get(url_for(url, **data)) 
        assert response.status_code == 400

#Missing parameter failures
def test_predict_decision_failFailures():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'predict_decision'
    with app.app_context(), app.test_request_context():
        data = {
            'studytime': '1',
            'failures': None,
            'Dalc': '4',
            'Walc': '3',
            'health': '5',
            'absences':'10',
            'G1': '17',
            'G2': '18'
        }
        response = client.get(url_for(url, **data)) 
        assert response.status_code == 400

#Missing parameter absences
def test_predict_decision_FailAbsences():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'predict_decision'
    with app.app_context(), app.test_request_context():
        data = {
            'studytime': '1',
            'failures': '2',
            'Dalc': '4',
            'Walc': '3',
            'health': '5',
            'absences':None,
            'G1': '17',
            'G2': '18'
        }
        response = client.get(url_for(url, **data)) 
        assert response.status_code == 400

#invalid user input for the parameters 
#studytime greater than 4 -- invalid 
def test_predict_decision_failStudytimeGreater():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'predict_decision'
    with app.app_context(), app.test_request_context():
        data = {
            'studytime': '5',
            'failures': '2',
            'Dalc': '4',
            'Walc': '3',
            'health': '5',
            'absences':'10',
            'G1': '17',
            'G2': '18'
        }
        response = client.get(url_for(url, **data)) 
        assert response.status_code == 400

#failures greater than 4 - invalid 
def test_predict_decision_failFailureGreater():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'predict_decision'
    with app.app_context(), app.test_request_context():
        data = {
            'studytime': '1',
            'failures': '5',
            'Dalc': '4',
            'Walc': '3',
            'health': '5',
            'absences':'10',
            'G1': '17',
            'G2': '18'
        }
        response = client.get(url_for(url, **data)) 
        assert response.status_code == 400

#dalc greater than 5- invalid 
def test_predict_decision_failDalcGreater():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'predict_decision'
    with app.app_context(), app.test_request_context():
        data = {
            'studytime': '1',
            'failures': '2',
            'Dalc': '6',
            'Walc': '3',
            'health': '5',
            'absences':'10',
            'G1': '17',
            'G2': '18'
        }
        response = client.get(url_for(url, **data)) 
        assert response.status_code == 400

#health greater than 5- invalid 
def test_predict_decision_failHealthGreater():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'predict_decision'
    with app.app_context(), app.test_request_context():
        data = {
            'studytime': '1',
            'failures': '2',
            'Dalc': '4',
            'Walc': '3',
            'health': '6',
            'absences':'10',
            'G1': '17',
            'G2': '18'
        }
        response = client.get(url_for(url, **data)) 
        assert response.status_code == 400

#health smaller than 1- invalid  
def test_predict_decision_failHealthSmaller():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'predict_decision'
    with app.app_context(), app.test_request_context():
        data = {
            'studytime': '1',
            'failures': '2',
            'Dalc': '4',
            'Walc': '3',
            'health': '0',
            'absences':'10',
            'G1': '17',
            'G2': '18'
        }
        response = client.get(url_for(url, **data)) 
        assert response.status_code == 400

#failures smaller than 1- invalid  
def test_predict_decision_failFailuresSmaller():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = 'predict_decision'
    with app.app_context(), app.test_request_context():
        data = {
            'studytime': '1',
            'failures': '0',
            'Dalc': '4',
            'Walc': '3',
            'health': '1',
            'absences':'10',
            'G1': '17',
            'G2': '18'
        }
        response = client.get(url_for(url, **data)) 
        assert response.status_code == 400


