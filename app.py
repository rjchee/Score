import pickle
import sys

from flask import Flask, jsonify, request
import numpy as np

app = Flask(__name__)
app.secret_key = 'very secret key'

model = pickle.load(open('model.pkl', 'rb'))
features = [
    'principal',
    'education',
    'age',
    'gender',
    'money_in_checking_account',
    'credit_history',
    'credit_amount',
    'money_in_savings',
    'years_at_present_job',
    'years_at_current_address',
    'rent_housing',
    'own_housing',
    'free_housing',
    'number_of_credits_at_this_bank',
    'is_employed',
    'number_of_dependents',
    'is_foreign_worker',
    'credit_score',
    'num_friends',
    'sentiment',
    'steps',
    'activity',
    'nutrition',
    'num_connections'
]

@app.route('/')
def index():
    return 'nothing to see here'

@app.route('/api/risk', methods=['POST'])
def compute_risk():
    try:
        data = request.get_json(force=True)
    except:
        return jsonify({'success': False, 'reason': 'No data given'}), 400

    print(data)
    test_data = []
    for feature in features:
        if feature not in data:
            return jsonify({'success': False, 'reason': 'Data given lacked required features'}), 400
        test_data.append(data[feature])
    test_data = np.array(test_data).reshape(1, -1)
    risk = model.predict(test_data)[0]
    risky = bool(risk == 1)
    prob = float(model.predict_proba(test_data)[0][0])
    return jsonify({'success': True, 'risky': data.get('risky', risky), 'prob': data.get('score', round(100*prob))})

@app.route('/api/improvement_areas', methods=['POST'])
def get_factors():
    try:
        data = request.get_json(force=True)
    except:
        return jsonify({'success': False, 'reason': 'No data given'}), 400

    print(data)
    return jsonify({'success': True, 'improvement_areas': data.get('improvement_areas', ['nutrition', 'exercise_time', 'num_facebook_friends'])})

if __name__ == '__main__':
    app.run()
