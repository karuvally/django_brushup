import subprocess
import json

def get_sensor_data():
    process = subprocess.Popen(
        ["sensors", "-j"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    process.wait()
    sensor_data = json.loads(process.communicate()[0].decode())
    return sensor_data
