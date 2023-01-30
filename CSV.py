import json
import csv

with open("private_data") as f:
    new_file = json.load(f)

print(new_file)

ocherednoe_name = [ 'name', 'age', 'id', 'phone']


spisok = []
for item in new_file:
    value = new_file[item]
    value.append(item)
    spisok.append(value)

spisok[0].append('555-555')
spisok[1].append('444-444')
spisok[2].append('333-333')
spisok[3].append('222-222')
spisok[4].append('111-111')

with open('data.csv', 'w', encoding='utf-8') as new_new_file:
    file_writer = csv.writer(new_new_file)
    file_writer.writerow(ocherednoe_name)
    for item in spisok:
        file_writer.writerow(item)

