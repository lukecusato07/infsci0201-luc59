# Part 1 Implement Class given Class Diagram
from abc import ABC, abstractmethod
import json

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
        print(self.get_name(), "is now connected to the network")

class Home:
    def __init__(self, address: str, smart_devices=None):
        self.__address = address
        self.__smart_devices = smart_devices if smart_devices is not None else []

    def add_device(self, device: SmartDevice):
        self.__smart_devices.append(device)
        device.connect_to_network()

    def print_devices(self):
        for device in self.__smart_devices:
            print(device.to_json())

    def to_json(self):
        home_data = {
            'address': self.__address,
            'smart_devices': [json.loads(device.to_json()) for device in self.__smart_devices]
        }
        return json.dumps(home_data) 


bulb = LightBulb("SmartBulb", "Amazon", 5)
home = Home("135 N Bellfield Ave")
home.add_device(bulb)
home.print_devices()