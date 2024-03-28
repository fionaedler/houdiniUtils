import csv

points = [
    [1, 1.2, 3.4, 5.6],
    [2, 7.8, 9.1, 2.3]
    ]

filename = "points.csv"

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "X", "Y", "Z"])
    for point in points:
        writer.writerow(point)

print(f"Data written to: {filename}")