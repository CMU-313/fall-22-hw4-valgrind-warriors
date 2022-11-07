import this
from flask import Flask, abort, jsonify, request
import joblib
import pandas as pd
import numpy as np
import os

def configure_routes(app):

    this_dir = os.path.dirname(__file__)
    model_path = os.path.join(this_dir, "linear_regression_model.pkl")
    clf = joblib.load(model_path)

    @app.route('/')
    def hello():
        return "welcome to ML microservice"


    @app.route('/predict/score')
    def predict_score():
        #use entries from the query string here but could also use json
        studytime = int(request.args.get('studytime'))
        failures = int(request.args.get('failures'))
        Dalc = int(request.args.get('Dalc'))
        Walc = int(request.args.get('Walc'))
        health = int(request.args.get('health'))
        absences = int(request.args.get('absences'))
        G1 = int(request.args.get('G1'))
        G2 = int(request.args.get('G2'))

        #check if user input is valid
        if studytime < 0 or studytime > 4:
            abort(400, "invalid studytime input")
            
        if failures < 1 or failures == 3 or failures > 4:
            abort(400, "invalid failures input")
        
        if Dalc < 1 or Dalc > 5:
            abort(400, "invalid Dalc input")

        if Walc < 1 or Walc > 5:
            abort(400, "invalid Walc input")

        if health < 1 or health > 5:
            abort(400, "invalid health input")

        if absences < 0 or absences > 93:
            abort(400, "invalid absences input")

        if G1 < 0 or G1 > 20:
            abort(400, "invalid G1 input")

        if G2 < 0 or G2 > 20:
            abort(400, "invalid G2 input")
            
        
        query_df = pd.DataFrame({
            'Dalc': pd.Series([Dalc]),
            'G1': pd.Series([G1]),
            'G2': pd.Series([G2]),
            'Walc': pd.Series([Walc]),
            'absences': pd.Series([absences]),
            'failures': pd.Series([failures]),
            'health': pd.Series([health]),
            'studytime': pd.Series([studytime]),
        })
        query = pd.get_dummies(query_df)
        prediction = round(clf.predict(query)[0])
        return jsonify(G3=str(prediction))

    @app.route('/predict/decision')
    def predict_decision():
        #use entries from the query string here but could also use json
        studytime = int(request.args.get('studytime'))
        failures = int(request.args.get('failures'))
        Dalc = int(request.args.get('Dalc'))
        Walc = int(request.args.get('Walc'))
        health = int(request.args.get('health'))
        absences = int(request.args.get('absences'))
        G1 = int(request.args.get('G1'))
        G2 = int(request.args.get('G2'))

        #check if user input is valid
        if studytime < 0 or studytime > 4:
            abort(400, "invalid studytime input")
            
        if failures < 1 or failures == 3 or failures > 4:
            abort(400, "invalid failures input")
        
        if Dalc < 1 or Dalc > 5:
            abort(400, "invalid Dalc input")

        if Walc < 1 or Walc > 5:
            abort(400, "invalid Walc input")

        if health < 1 or health > 5:
            abort(400, "invalid health input")

        if absences < 0 or absences > 93:
            abort(400, "invalid absences input")

        if G1 < 0 or G1 > 20:
            abort(400, "invalid G1 input")

        if G2 < 0 or G2 > 20:
            abort(400, "invalid G2 input")
        
        query_df = pd.DataFrame({
            'Dalc': pd.Series([Dalc]),
            'G1': pd.Series([G1]),
            'G2': pd.Series([G2]),
            'Walc': pd.Series([Walc]),
            'absences': pd.Series([absences]),
            'failures': pd.Series([failures]),
            'health': pd.Series([health]),
            'studytime': pd.Series([studytime]),
        })
        query = pd.get_dummies(query_df)
        prediction = round(clf.predict(query)[0])
        
        decision = "yes" if prediction >= 15 else "no"
        return jsonify(decision=str(decision))

