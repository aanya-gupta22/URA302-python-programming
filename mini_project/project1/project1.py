import numpy as np
import csv

input_file = "sensor_data.csv"
output_file = "sensor_results.csv"

data = np.genfromtxt(input_file, delimiter=",", names=True, dtype=None, encoding="utf-8-sig")

timestamp = data['timestamp']
temperature = data['temperature']
distance = data['distance']
battery = data['battery']
humidity = data['humidity']

results = []

for sensor, values in [
    ('Temperature', temperature),
    ('Distance', distance),
    ('Battery', battery),
    ('Humidity', humidity)
]:
    avg = np.mean(values)
    min_val = np.min(values)
    max_val = np.max(values)
    results.append([sensor, f"{avg:.2f}", min_val, max_val])

max_temp_index = np.argmax(temperature)
max_temp_time = timestamp[max_temp_index]
results.append(["Max Temperature Time", max_temp_time, temperature[max_temp_index]])

low_battery_count = np.sum(battery < 30)
results.append(["Battery < 30% Count", low_battery_count])

with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Metric", "Value1", "Value2", "Value3"])
    writer.writerows(results)

print("result saved")