# Setting up classes for different devices
from abc import ABC, abstractmethod
import json

NETWORK_CONNECTION_MESSAGE = "is now connected to the network."

class SmartDevice(ABC):
    def __init__(self, name: str, manufacturer: str):
        self.__name = name
        self.__manufacturer = manufacturer

    def get_name(self):
        return self.__name
    
    def get_manufacturer(self):
        return self.__manufacturer 

    @abstractmethod
    def to_json(self):
        pass
    
    @abstractmethod
    def connect_to_network(self):
        pass
    
class LightBulb(SmartDevice):
    def __init__(self, name: str, manufacturer: str, brightness: float):
        super().__init__(name, manufacturer)
        self.__brightness = brightness

    def adjust_brightness(self, value: float):
        self.__brightness = value
        print("Brightness is set to: ", self.__brightness)

    def to_json(self):
        light_bulb_data = {
            'name': self.get_name(),
            'manufacturer': self.get_manufacturer(),
            'brightness': self.__brightness
        }
        return json.dumps(light_bulb_data)
    
    def connect_to_network(self):
        print(self.get_name(), NETWORK_CONNECTION_MESSAGE)

class Vacuum(SmartDevice):
    def __init__(self, name: str, manufacturer: str, battery: int):
        super().__init__(name, manufacturer)
        self.__battery = battery

    def battery_check(self, value: int):
        self.__battery = value
        print(self.get_name()," battery percentage is: ", self.__battery)

        while value < 20:
            print(self.__name," battery percentage is ", value, " consider returning device to charging dock.")

    def to_json(self):
        vacuum_data = {
            'name' : self.get_name(),
            'manufacturer' : self.get_manufacturer(),
            'battery' : self.__battery
        }
        return json.dumps(vacuum_data)
    
    def connect_to_network(self):
        print(self.get_name(), NETWORK_CONNECTION_MESSAGE)

class Thermostat(SmartDevice):
    def __init__(self, name: str, manufacturer: str, room: str, temp: int):
        super().__init__(name, manufacturer)
        self.__room = room
        self.__temp = temp


    def room_check(self, room):
        print(self.__name, "is regulating the temperature in: ", room)

    def to_json(self):
        thermostat_data = {
            'name': self.get_name(),
            'manufacturer': self.get_manufacturer(),
            'room': self.__room,
            'temperature': self.__temp
        }
        return json.dumps(thermostat_data)
    
    def connect_to_network(self):
        print(self.get_name(), NETWORK_CONNECTION_MESSAGE)


class Home:
    def __init__(self, address: str, zip: int, smart_devices=None):
        self.__address = address
        self.__zip = zip
        self.__smart_devices = smart_devices if smart_devices is not None else []

    def get_address(self):
        return self.__address
    
    def get_devices(self):
        return self.__smart_devices

    def add_device(self, device: SmartDevice):
        self.__smart_devices.append(device)
        device.connect_to_network()

    def print_devices(self):
        for device in self.__smart_devices:
            print(device.to_json())

    def to_json(self):
        home_data = {
            'address': self.__address,
            'zip_code': self.__zip,
            'smart_devices': [json.loads(device.to_json()) for device in self.__smart_devices]
        }
        return json.dumps(home_data) 


bulb = LightBulb("SmartBulb", "Philips", 50.5)
vacuum = Vacuum("SmartVacuum", "Dyson", 100)
thermostat = Thermostat("SmartThermostat", "Nest", "Master Bedroom", 72)
home = Home("135 N Bellfield Ave", 15213)
home.add_device(bulb)
home.add_device(vacuum)
home.add_device(thermostat)
home.print_devices()