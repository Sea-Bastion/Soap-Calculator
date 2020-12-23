import json
import csv

with open("Values.csv", newline='') as file:
	rawinput = csv.reader(file)

	header = rawinput.__next__()
	data = []
	for row in rawinput:

		tmp = {}
		for x, val in enumerate(row):
			tmp[header[x]] = val

		data.append(tmp)


with open("Values.json", 'w') as output:
	json.dump(data, output)
