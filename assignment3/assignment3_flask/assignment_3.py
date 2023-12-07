from flask import Flask, render_template, request, jsonify
import json

from model.smart_devices import Home
from model.smart_devices import SmartDevice
from model.smart_devices import LightBulb

app = Flask(__name__)

@app.route("/")
def index():
    home = Home("4200 Fifth Ave")
    bulb = LightBulb("SmartBulb2", "Philips", 75.5)

    home.add_device(bulb)

    return render_template("home.html", home=home)

@app.route('/add_lightbulb', methods=['POST'])
def add_lightbulb():
    data = request.json
    try:
        name = data['name']
        manufacturer = data['manufacturer']
        brightness = data['brightness']

        new_bulb = LightBulb(name, manufacturer, brightness)
        light_bulb_json = new_bulb.to_json()

        with open('light.json', 'w') as file:
            file.write(light_bulb_json)
            
        return jsonify({"message": "LightBulb added successfully"}), 200

    except KeyError:
        return jsonify({"error": "Missing data for creating a LightBulb"}), 400
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)