from flask import Flask, render_template, request, jsonify
import json
import requests
from devices import LightBulb, Vacuum, Thermostat, Home, NETWORK_CONNECTION_MESSAGE

WEATHER_API_KEY = "760557e4a0c14f868b7232036231412"
FILE_PATH = 'data/devices.json'

devices = []
app = Flask(__name__)


def save_devices(devices):
    with open('data/devices.json', 'w') as file:
        json.dump(devices, file, indent=4)


@app.route('/', methods=['GET'])
def index():
    home2 = Home("135 N Bellfield Ave", 15213)
    
    return render_template('home.html', home=home2)


@app.route('/devices', methods=['GET'])
def get_devices():
    bulb2 = LightBulb("SmartBulb", "Philips", 50.5)
    vacuum2 = Vacuum("SmartVacuum", "Dyson", 100)
    thermostat2 = Thermostat("SmartThermostat", "Nest", "Master Bedroom", 72)
    home2 = Home("135 N Bellfield Ave", 15213)
    
    home2.add_device(bulb2)
    home2.add_device(vacuum2)
    home2.add_device(thermostat2)

    return render_template('home.html', home=home2)


@app.route('/devices', methods=['POST'])
def add_device():
    data = request.form
    print(data)

    try:
        print(data)
        name = data['name']
        manufacturer = data['manufacturer']
        brightness = data['brightness']
        battery = data['battery']
        room = data['room']
        temp = data['temperature']

        new_thermostat = Thermostat(name, manufacturer, room, temp)
        thermostat_to_json = new_thermostat.to_json()
        
        with open(FILE_PATH, 'w') as file:
            json.dump(thermostat_to_json, file, indent=4)


        return jsonify({'message': 'Device added successfully.'}), 200
    
    except KeyError:
        return jsonify({'error': 'Missing data for creating a thermostat'}), 400
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/devices/<int:device_id>', methods=['PUT'])
def update_device(device_id):
    data = request.json
    
    if device_id < 0 or device_id >= len(devices):
        return jsonify({'error': 'Device not found'}), 404
    devices[device_id] = data
    save_devices(devices)
    return jsonify({'message': 'Device updated successfully'})


@app.route('/devices/<int:device_id>', methods=['DELETE'])
def delete_device(device_id):
    
    if device_id < 0 or device_id >= len(devices):
        return jsonify({'error': 'Device not found'}), 404
    
    del devices[device_id]
    save_devices(devices)
    return jsonify({'message': 'Device deleted successfully'})


@app.route('/temperature_check', methods=['GET'])
def temp_check():
    zip_code = request.args.get('zip_code')
    weather_url = f'http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={zip_code}&aqi=no'


    response = requests.get(weather_url)

    if response.status_code == 200:
        data = response.json()
        outside_temp = data['current']['temp_f']
        print(outside_temp)
        home_temp = 72
        temp_difference = home_temp - outside_temp
        return jsonify({'temperature difference' : temp_difference})
    
    else:
        return jsonify({'error': 'Failed to fetch external temperature'}), 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)