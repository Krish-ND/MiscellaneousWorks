import json

#Read JSON file
with open("data.json", "r") as f:
    data = json.load(f)
    print("Original Data:")
    print(data)

#Modify data (example: add a new key)
data["status"] = "processed"

#Write to a new JSON file
with open("updated_data.json", "w") as f:
    json.dump(data, f, indent=4)

print("\nUpdated JSON saved!")