import numpy as np
import csv

input_file = "robot_path.csv"
output_file = "robot_results.csv"

data = np.genfromtxt(input_file, delimiter=",", names=True, dtype=float, encoding="utf-8")

x = np.nan_to_num(data["x"], nan=0.0)
y = np.nan_to_num(data["y"], nan=0.0)

dx = np.diff(x)
dy = np.diff(y)
step_distances = np.sqrt(np.clip(dx*2 + dy*2, 0, None))
total_distance = np.sum(step_distances)

distances_from_origin = np.sqrt(np.clip(x*2 + y*2, 0, None))
farthest_index = np.argmax(distances_from_origin)
farthest_point = (x[farthest_index], y[farthest_index])
farthest_distance = distances_from_origin[farthest_index]

positions = np.column_stack((x, y))
unique_positions = np.unique(positions, axis=0)
revisited = len(unique_positions) < len(positions)

results = [
    ["Total Distance Traveled", f"{total_distance:.2f}"],
    ["Farthest Point (x,y)", f"({farthest_point[0]}, {farthest_point[1]})"],
    ["Farthest Distance from Origin", f"{farthest_distance:.2f}"],
    ["Revisited Any Position", "Yes" if revisited else "No"],
]

with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Metric", "Value"])
    writer.writerows(results)
