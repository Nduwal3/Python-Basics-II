# Find a package in the Python standard library for dealing with JSON. 
# Import the library module and inspect the attributes of the module. 
# Use the help function to learn more about how to use the module.
# Serialize a dictionary mapping 'name' to your name and 'age' to your age, to a JSON string.
# Deserialize the JSON back into Python. 

import json

json_data ={"name" : "Niru","age" : 23 }

python_to_json = json.dumps(json_data)
print(type(python_to_json))

json_to_python = json.loads(python_to_json)
print(type(json_to_python))


