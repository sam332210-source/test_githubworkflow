import os
import json

my_data = {"name": "Tarun kumar", "age": 32, "Occupation": "Engineer", "Place": "cheeka"}

path = "./build/data.json"
if not os.path.exists("./build"):
    os.makedirs("./build")
with open(path, "w") as file:
    print(my_data)
    json.dump(my_data, file)
