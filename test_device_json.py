
import json

class DeviceConfig:
    def __init__(self, data):
        self.serial = data["serial"]
        self.battery_level = data["battery_level"]
        self.network_type = data["network_type"]
        self.firmware_version = data["firmware_version"]

    def __eq__(self, other):
        return (
            self.serial == other.serial and
            self.battery_level == other.battery_level and
            self.network_type == other.network_type and
            self.firmware_version == other.firmware_version
        )

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def test_device_config_compare():
    expected = DeviceConfig(load_json("sample_device_expected.json"))
    actual = DeviceConfig(load_json("sample_device_actual.json"))

    assert expected == actual
