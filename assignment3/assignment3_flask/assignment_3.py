from flask import Flask
import render_template

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)