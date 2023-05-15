# import csv

# with open('NewAttributes/ATTRIBUTES.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         # Process each row
#         print(row[0],len(row))
        



import csv

# Read the CSV file and store the records
records = []
with open('NewAttributes/ATTRIBUTES.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        records.append(row)


# Write the updated records back to the CSV file

for row in records:
    
    if (int(len(row)<690)):
        max_insert = 690-int(len(row))
        for insert in range(max_insert):
            row.append(',')
    print(row[0],len(row))

with open('NewAttributes/ATTRIBUTES.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(records)
