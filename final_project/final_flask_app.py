from flask import Flask, render_template, request, jsonify
import json
import requests
from devices import LightBulb, Vacuum, Thermostat, Home, NETWORK_CONNECTION_MESSAGE

WEATHER_API_KEY = "760557e4a0c14f868b7232036231412"
FILE_PATH = 'data/devices.json'
ADDRESS = "135 N Bellfield Ave"

devices = []
app = Flask(__name__)


def save_devices(devices):
    with open('data/devices.json', 'w') as file:
        json.dump(devices, file, indent=4)


@app.route('/', methods=['GET'])
def index():
    home2 = Home(ADDRESS, 15213)
    
    return render_template('home.html', home=home2)


@app.route('/devices', methods=['GET'])
def get_devices():
    bulb2 = LightBulb("SmartBulb", "Philips", 3, 50.5)
    vacuum2 = Vacuum("SmartVacuum", "Dyson", 4, 100)
    thermostat2 = Thermostat("SmartThermostat", "Nest", 5, "Master Bedroom", 72)
    home2 = Home(ADDRESS, 15213)
    
    home2.add_device(bulb2)
    home2.add_device(vacuum2)
    home2.add_device(thermostat2)

    return render_template('home.html', home=home2)


@app.route('/devices', methods=['POST'])
def add_device():
    data = request.form

    try:
        print(data)
        name = data['name']
        manufacturer = data['manufacturer']
        device_id = data['id']
        brightness = data['brightness']
        battery = data['battery']
        room = data['room']
        temp = data['temperature']

        new_thermostat = Thermostat(name, device_id, manufacturer, room, temp)
        thermostat_to_json = new_thermostat.to_json()
        
        with open(FILE_PATH, 'w') as file:
            json.dump(thermostat_to_json, file, indent=4)


        return jsonify({'message': 'Device added successfully.'}), 200
    
    except KeyError:
        return jsonify({'error': 'Missing data for creating a thermostat'}), 400
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/devices/<id>', methods=['GET'])
def update_page(id):
    home2 = Home(ADDRESS, 15213)
    return render_template('update.html', home=home2)
def update_device(name):
    data = request.json
    
    if name != devices:
        return jsonify({'error': 'Device not found'}), 404
    devices['name'] = data
    save_devices(devices)
    return jsonify({'message': 'Device updated successfully'})


@app.route('/devices/<id>', methods=['DELETE'])
def delete_page(id):
    home2 = Home(ADDRESS, 15213)
    return render_template('delete.html', home=home2)
def delete_device(name):
    if name != devices:
        return jsonify({'error': 'Device not found'}), 404
    
    del devices[name]
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