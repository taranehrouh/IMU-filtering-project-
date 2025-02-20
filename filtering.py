# We are going to apply the moving average method to eliminate the Gaussian Noise from our data

import numpy as np
from simulate_imu import noised_data


filtered_data = noised_data.copy()

size = 10

def moving_average(data, window_size):
    data = np.array(data)
    result = []
    moving_sum = sum(data[:window_size])
    result.append(moving_sum /window_size)

    for i in range (len(data)-window_size):
        moving_sum += data[i+window_size]-data[i]
        result.append(moving_sum /window_size)

    padding = [np.nan] * (window_size - 1)
    result = padding + result

    return np.array(result)


filtered_data['accel_x'] = moving_average(filtered_data['accel_x'], size)
filtered_data['accel_y'] = moving_average(filtered_data['accel_y'], size)
filtered_data['accel_z'] = moving_average(filtered_data['accel_z'], size)
filtered_data['gyro_x'] = moving_average(filtered_data['gyro_x'], size)
filtered_data['gyro_y'] = moving_average(filtered_data['gyro_y'], size)
filtered_data['gyro_z'] = moving_average(filtered_data['gyro_z'], size)


# print(noised_data.head())

print(filtered_data)
