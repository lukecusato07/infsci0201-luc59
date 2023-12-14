from flask import Flask, render_template, request, jsonify
import json
import requests

from devices import LightBulb, Vacuum, Thermostat, Home, NETWORK_CONNECTION_MESSAGE

WEATHER_API_KEY = "a3fJhWTXjyT0t8xP649BXVzaWEIdX5Rq"

app = Flask(__name__)

def load_devices():
    try:
        with open('data/devices.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    

def save_devices(devices):
    with open('data/devices.json', 'w') as file:
        json.dump(devices, file, indent=4)


@app.route('/')
def home():
    devices = load_devices()
    return render_template('home.html', devices=devices)


@app.route('/devices', methods=['GET'])
def get_devices():
    devices = load_devices()
    return jsonify(devices)


@app.route('/devices', methods=['POST'])
def add_device():
    data = request.json
    devices = load_devices()
    devices.append(data)
    save_devices(devices)
    return jsonify({'message': 'Device added successfully'})


@app.route('/devices/<int:device_id>', methods=['PUT'])
def update_device(device_id):
    data = request.json
    devices = load_devices()
    if device_id < 0 or device_id >= len(devices):
        return jsonify({'error': 'Device not found'}), 404
    devices[device_id] = data
    save_devices(devices)
    return jsonify({'message': 'Device updated successfully'})


@app.route('/devices/<int:device_id>', methods=['DELETE'])
def delete_device(device_id):
    devices = load_devices()
    if device_id < 0 or device_id >= len(devices):
        return jsonify({'error': 'Device not found'}), 404
    
    del devices[device_id]
    save_devices(devices)
    return jsonify({'message': 'Device deleted successfully'})

@app.route('/temperature_check', methods=['GET'])
def temp_check():
    zip_code = request.args.get('zip_code')
    weather_url = f'https://api.weatherstack.com/current?access_key={WEATHER_API_KEY}&query={zip_code}'
    
    response = requests.get(weather_url)
    if response.status_code == 200:
        outside_temp = response.json()['temperature']
        home_temp = 72
        temp_difference = home_temp - outside_temp
        return jsonify({'temperature difference' : temp_difference})
    
    else:
        return jsonify({'error': 'Failed to fetch external temperature'}), 500
    


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)