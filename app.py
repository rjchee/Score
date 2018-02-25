from flask import Flask, jsonify, request

app = Flask(__name__)
app.secret_key = 'very secret key'

@app.route('/')
def index():
    return 'nothing to see here'

@app.route('/api/risk')
def compute_risk():
    try:
        data = request.get_json(force=True)
    except:
        return jsonify({'success': False}), 400

    print(data)
    return jsonify({'success': True, 'risky': data.get('risky', False)})

@app.route('/api/improvement_areas')
def get_factors():
    try:
        data = request.get_json(force=True)
    except:
        return jsonify({'success': False}), 400

    print(data)
    return jsonify({'success': True, 'improvement_areas': data.get('improvement_areas', ['nutrition', 'exercise_time', 'num_facebook_friends'])})

if __name__ == '__main__':
    app.run()
