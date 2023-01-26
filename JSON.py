import json


data_pers = {123456: ("Andrey", 27), 234567: ('Igor', 33), 345678: ('Naruto', 19), 456789: ('Kakashi', 43), 567890: ('Yuki', 14)}

with open("private_data", "w") as f:
    json.dump(data_pers, f, indent=2)

