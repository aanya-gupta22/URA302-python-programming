sensor_data = {1: 2.3, 2: 4.5, 3: 1.8, 4: 3.6}

sensor_ids_above_3 = []

for sensor_id in sensor_data:
    reading = sensor_data[sensor_id]
    if reading > 3.0:
        sensor_ids_above_3.append(sensor_id)

print("Sensor IDs with reading above 3.0:", sensor_ids_above_3)
