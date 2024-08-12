from flask import Flask, request, jsonify
from datetime import datetime
import json

app = Flask(__name__)

data_store = []

def parse_data(data):
    parsed_data = json.loads(data)
    results = []
    for entry in parsed_data:
        result = {
            'id': entry.get('id'),
            'last_turn': entry.get('last_turn'),
            'tstamp_auth_start': datetime.fromtimestamp(entry.get('tstamp_auth_start')),
            'tstamp_auth_completion': datetime.fromtimestamp(entry.get('tstamp_auth_completion')),
            'getcannons_received': entry.get('getcannons_received'),
            'cannons': entry.get('cannons'),
            'getturn_received': entry.get('getturn_received'),
            'ship_moves': entry.get('ship_moves'),
            'shot_received': entry.get('shot_received'),
            'valid_shots': entry.get('valid_shots'),
            'sunk_ships': entry.get('sunk_ships'),
            'escaped_ships': entry.get('escaped_ships'),
            'remaining_life_on_escaped_ships': entry.get('remaining_life_on_escaped_ships'),
            'tstamp_completion': datetime.fromtimestamp(entry.get('tstamp_completion')),
            'auth': entry.get('auth')
        }
        results.append(result)
    return results

def analyze_statistics(results):
    total_ship_moves = sum(result['ship_moves'] for result in results)
    total_shot_received = sum(result['shot_received'] for result in results)
    total_sunk_ships = sum(result['sunk_ships'] for result in results)
    total_escaped_ships = sum(result['escaped_ships'] for result in results)
    total_remaining_life = sum(result['remaining_life_on_escaped_ships'] for result in results)

    return {
        "Total Ship Moves": total_ship_moves,
        "Total Shots Received": total_shot_received,
        "Total Sunk Ships": total_sunk_ships,
        "Total Escaped Ships": total_escaped_ships,
        "Total Remaining Life on Escaped Ships": total_remaining_life
    }

@app.route('/data', methods=['POST'])
def handle_data():
    data = request.data.decode('utf-8')
    parsed_results = parse_data(data)
    stats = analyze_statistics(parsed_results)
    return jsonify(stats)

if __name__ == "__main__":
    app.run(host='::', port=5000)  # Bind to all IPv6 addresses
