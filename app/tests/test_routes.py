from flask import Flask

from app.handlers.routes import configure_routes


def test_base_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)

    assert response.status_code == 200
    assert response.get_data() == b'try the predict route it is great!'

def test_predict_score():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/score?studytime=1&failures=1&Dalc=1&Walc=1&health=1&absences=0&G1=0&G2=0' #min values for all
    url2 = '/predict/score?studytime=1&failures=1&Dalc=1&Walc=1&health=1&absences=93&G1=0&G2=0' #max value for absences
    url3 = '/predict/score?studytime=1&failures=1&Dalc=1&Walc=1&health=1&absences=93&G1=20&G2=20' #max values for absences and G1 & G2
    url4 = '/predict/score?studytime=4&failures=4&Dalc=5&Walc=5&health=5&absences=93&G1=20&G2=20' #max values for all  


    #TODO: complete this test
    response = client.get(url)
    response2 = client.get(url2)
    response3 = client.get(url3)
    response4 = client.get(url4)
    assert response.status_code == 200
    assert response2.status_code == 200
    assert response3.status_code == 200
    assert response4.status_code == 200

     

def test_predict_decision():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict/decision?studytime=1&failures=1&Dalc=1&Walc=1&health=1&absences=1&G1=0&G2=0'

    #TODO: complete this test
    response = client.get(url)
    assert response.status_code == 200
