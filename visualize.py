import matplotlib.pyplot as plt
from src.simulate_imu import raw_data
from src.simulate_imu import noised_data
from filtering import filtered_data

plt.figure(figsize=(10, 5))
plt.plot(raw_data.index, raw_data["accel_x"], label="Accel X", color='r')
plt.plot(raw_data.index, raw_data["accel_y"], label="Accel Y", color='g')
plt.plot(raw_data.index, raw_data["accel_z"], label="Accel Z", color='b')
plt.xlabel("Time (Index)")
plt.ylabel("Acceleration (m/s²)")
plt.title("Acceleration Over Time (Raw Data)")
plt.legend()
plt.grid(True)
plt.show()


plt.figure(figsize=(10,5))
plt.plot(noised_data.index, noised_data["accel_x"], label="Accel X", color='r')
plt.plot(noised_data.index, noised_data["accel_y"], label="Accel Y", color='g')
plt.plot(noised_data.index, noised_data["accel_z"], label="Accel Z", color='b')
plt.xlabel("Time (Index)")
plt.ylabel("Acceleration (m/s²)")
plt.title("Acceleration Over Time (Noisy Data)")
plt.legend()
plt.grid(True)
plt.show()


plt.figure(figsize=(10,5))
plt.plot(filtered_data.index, filtered_data["accel_x"], label="Accel X", color='r')
plt.plot(filtered_data.index, filtered_data["accel_y"], label="Accel Y", color='g')
plt.plot(filtered_data.index, filtered_data["accel_z"], label="Accel Z", color='b')
plt.xlabel("Time (Index)")
plt.ylabel("Acceleration (m/s²)")
plt.title("Acceleration Over Time (Filtered Data)")
plt.legend()
plt.grid(True)
plt.show()