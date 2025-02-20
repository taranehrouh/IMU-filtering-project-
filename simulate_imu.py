import numpy as np
import pandas as pd
import re

file_path = r"C:\Users\User\PycharmProjects\PythonProject\data\raw_data.txt"

with open(file_path, "r") as f:
    lines = f.readlines()

accel_x = []
accel_y = []
accel_z = []

gyro_x = []
gyro_y = []
gyro_z = []

temp = []


accel_pattern = re.compile(r"Acceleration X:\s*(-?\d+\.\d+),\s*Y:\s*(-?\d+\.\d+),\s*Z:\s*(-?\d+\.\d+)")
gyro_pattern = re.compile(r"Rotation X:\s*(-?\d+\.\d+),\s*Y:\s*(-?\d+\.\d+),\s*Z:\s*(-?\d+\.\d+)")
temp_pattern = re.compile(r"Temperature:\s*(-?\d+\.\d+)")

for line in range(len(lines)):
    accel_match = accel_pattern.search(lines[line])
    gyro_match = gyro_pattern.search(lines[line])
    temp_match = temp_pattern.search(lines[line])

    if accel_match:
        accel_x.append(float(accel_match.group(1)))
        accel_y.append(float(accel_match.group(2)))
        accel_z.append(float(accel_match.group(3)))

    if gyro_match:
        gyro_x.append(float(gyro_match.group(1)))
        gyro_y.append(float(gyro_match.group(2)))
        gyro_z.append(float(gyro_match.group(3)))

    if temp_match:
        temp.append(float(temp_match.group(1)))


raw_data = pd.DataFrame({
    "accel_x": accel_x,
    "accel_y": accel_y,
    "accel_z": accel_z,
    "gyro_x": gyro_x,
    "gyro_y": gyro_y,
    "gyro_z": gyro_z,
    "temp": temp,
})


# print(raw_data.head())

# print(raw_data.info())


#saving this raw data into a csv file for future calculations

raw_data.to_csv(r"C:\Users\User\PycharmProjects\PythonProject\data\parsed_sensor_data.csv", index=False)


parsed_data = pd.read_csv(r"C:\Users\User\PycharmProjects\PythonProject\data\parsed_sensor_data.csv")

# Gaussian noise which is also called the thermal noise comes from the random electron movement which has a bell-shaped
# curve

std = 0.2

noised_data = raw_data.copy()

noised_data['accel_x'] += np.random.normal(0, std, len(noised_data))
noised_data['accel_y'] += np.random.normal(0, std, len(noised_data))
noised_data['accel_z'] += np.random.normal(0, std, len(noised_data))
noised_data['gyro_x'] += np.random.normal(0, std, len(noised_data))
noised_data['gyro_y'] += np.random.normal(0, std, len(noised_data))
noised_data['gyro_z'] += np.random.normal(0, std, len(noised_data))

drift_rate = 0.001

drift_array = np.linspace(0, drift_rate*len(noised_data), len(noised_data))

# print(drift_array)

noised_data['accel_x'] += drift_array
noised_data['accel_y'] += drift_array
noised_data['accel_z'] += drift_array
noised_data['gyro_x'] += drift_array
noised_data['gyro_y'] += drift_array
noised_data['gyro_z'] += drift_array

# Quantization

adc_bits = 12
accel_range = 16
quantization_level = 2**16
quantization_step = accel_range/quantization_level

noised_data["accel_x"] = np.round(noised_data["accel_x"] / quantization_step) * quantization_step
noised_data["accel_y"] = np.round(noised_data["accel_y"] / quantization_step) * quantization_step
noised_data["accel_z"] = np.round(noised_data["accel_z"] / quantization_step) * quantization_step

gyro_range = 400
gyro_step = gyro_range/quantization_level

noised_data["gyro_x"] += np.round(noised_data["gyro_x"] / gyro_step) * gyro_step
noised_data["gyro_y"] += np.round(noised_data["gyro_y"] / gyro_step) / gyro_step
noised_data["gyro_z"] += np.round(noised_data["gyro_z"] / gyro_step) / gyro_step
