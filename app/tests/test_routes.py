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

def test_predict_score():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/score'
    response = client.get(url_for(url), 
                          headers=[('studytime', '1'), ('failures', '3'), ('Dalc', '4'),
                                    ('Walc', '3'), ('health', '5'), ('absences','10'),
                                    ('G1', '17'), ('G2', '18')])
    assert response.status_code == 200
    score = (int)(json.loads(response.data.decode('utf-8')).get("G3"))
    assert (0 <= score and score <= 20)
    
    response = client.get(url_for(url), 
                          headers=[('failures', '3'), ('Dalc', '4'),
                                    ('Walc', '3'), ('health', '5'), ('absences','10'),
                                    ('G1', '17'), ('G2', '18')])
    assert response.status_code == 400
    response = client.get(url_for(url), 
                          headers=[('studytime', '1'), ('Dalc', '4'),
                                    ('Walc', '3'), ('health', '5'), ('absences','10'),
                                    ('G1', '17'), ('G2', '18')])
    assert response.status_code == 400
    

def test_predict_decision():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/decision'
    #TODO: complete this test
