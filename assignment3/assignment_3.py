# Part 1 Implement Class given Class Diagram
from abc import ABC, abstractmethod
import json

class SmartDevice(ABC):
    def __init__(self, name: str, manufacturer: str):
        self.__name__ = name
        self.__manufacturer__ = manufacturer

    @abstractmethod
    def to_json(self):
        smart_device_data = {
            'name': self.__name__,
            'manufacturer': self.__manufacturer__
        }
        return json.dumps(smart_device_data)
    
    @abstractmethod
    def connect_to_network(self):
        pass
    
class LightBulb(SmartDevice):
    def __init__(self, name: str, manufacturer: str, brightness: int):
        self.__name__: name
        self.__manufacturer__: manufacturer
        self.__brightness__ = brightness

    def adjust_brightness(self, value: float):
        self.__value__: value
        print("Brightness is set to: ", self.__brightness__)

    def to_json(self):
        light_bulb_data = {
            'name': self.__name__,
            'manufacturer': self.__manufacturer__,
            'brightness': self.__brightness__
        }
        return json.dumps(light_bulb_data)
    
    def connect_to_network(self):
        print(self.__name__, " is now connected to the network")

class Home:
    def __init__(self, address: str, smart_devices: list):
        self.__address__ = address
        self.__smart_devices__ = smart_devices

    def add_device(self, device: SmartDevice):
        self.__smart_devices__.append(device)
        device.connect_to_network()

    def print_devices(self):
        for device in self.__smart_devices__:
            print(device.to_json())

    def to_json(self):
        home_data = {
            'address': self.__address__,
            'smart_devices': [device.to_json for device in self.__smart_devices__]
        }
        return json.dumps(home_data) 

bulb = LightBulb("SmartBulb", "Amazon", 0.5)
home = Home("135 N Bellfield Ave", [])
home.add_device(bulb)
home.print_devices()