from flask import Flask
app = Flask(__name__)
class Device():
    def __init__(self, name, id, value):
        self.__name__ = name
        self.__id__ = id
        self.__value__ = value

    # API endpoints
    @app.route("/")
    def index_page(self):
        return '''
        <h1>This is the index page for my SmartHome API site</h1>
        <h3>Here you can alter endpoints to get to different pages of the site</h3>
        '''

    @app.route("/home")
    def home_page(self):
        return '''
        <h1>This is the home page</h1>
        <p>Welcome to my SmartHome API site! Here you can see my final project for INFSCI0201.</p>
        '''

    @app.route("/thermostat")
    def thermostat(self):
        return "<h1>This is the thermostat page</h1>"

    @app.route("/light_bulbs")
    def light_bulbs(self):
        return "<h1>This is the light bulbs page</h1>"

    @app.route("/smart_vacuum")
    def smart_vacuum(self):
        return "<h1>This is the smart vacuum page</h1>"

    @app.route("/edit_devices")
    def edit_devices(self):
        return "<h1>Here you can add or remove SmartHome devices</h1>"

    @app.route("/history")
    def history(self):
        return "<h1>Here you can view your past actions history</h1>"


        
        
thermostat = Device('Thermostat', 0, 72)
light_bulb = Device('Light bulb', 1, True)
smart_vacuum = Device('Smart vacuum', 2, True)


