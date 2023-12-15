+------------------+
|    SmartDevice   |
|------------------|
| -name: str       |
| -manufacturer: str|
| -id: int         |
|------------------|
| +get_name(): str |
| +get_manufacturer(): str |
| +get_id(): int   |
| +to_json(): str  |
| +connect_to_network(): void|
+------------------+
         ^
         |
         |   +----------------+
         +---|   LightBulb    |
         |   |----------------|
         |   | -brightness: float|
         |   |----------------|
         |   | +adjust_brightness(value: float): void|
         |   +----------------+
         |
         |   +----------------+
         +---|    Vacuum      |
         |   |----------------|
         |   | -battery: int  |
         |   |----------------|
         |   | +battery_check(value: int): void |
         |   +----------------+
         |
         |   +----------------+
         +---|  Thermostat    |
             |----------------|
             | -room: str     |
             | -temp: int     |
             |----------------|
             | +room_check(room: str): void|
             +----------------+
 
+------------------+
|      Home        |
|------------------|
| -address: str    |
| -zip: int        |
| -smart_devices: List[SmartDevice] |
|------------------|
| +get_address(): str |
| +get_devices(): List[SmartDevice] |
| +add_device(device: SmartDevice): void |
| +print_devices(): void |
| +to_json(): str  |
+------------------+