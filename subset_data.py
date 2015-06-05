# O3_hourly.csv and create daily average
import csv

with open('O3_hourly.csv', 'rb') as f:
    reader = csv.reader(f)
    fields = reader.next()
    # get daily min, max and avg values for each site

    site_vals = []
    count = 0
    #get current site
    for row in reader:
        while count == 0:
            site = row[1]
        if site == row[1]:
            site_vals.append(row[1])
            #


# import csv
# data = csv.reader(open('O3_hourly.csv'))
# # Read the column names from the first line of the file
# fields = data.next()
# for row in data:
#         # Zip together the field names and values
#     items = zip(fields, row)
#     item = {}
#         # Add the value to our dictionary
#     for (name, value) in items:
#         item[name] = value.strip()
#         print(item)
#
