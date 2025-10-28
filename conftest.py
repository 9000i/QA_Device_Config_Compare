
from test_device_json import DeviceConfig

def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, DeviceConfig) and isinstance(right, DeviceConfig) and op == "==":
        diffs = ["Comparing DeviceConfig objects:"]
        if left.serial != right.serial:
            diffs.append(f"  Serial differs: {left.serial} != {right.serial}")
        if left.battery_level != right.battery_level:
            diffs.append(f"  Battery differs: {left.battery_level} != {right.battery_level}")
        if left.network_type != right.network_type:
            diffs.append(f"  Network differs: {left.network_type} != {right.network_type}")
        if left.firmware_version != right.firmware_version:
            diffs.append(f"  Firmware differs: {left.firmware_version} != {right.firmware_version}")
        return diffs

