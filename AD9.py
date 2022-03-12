import requests
import json

main_api = "https://api.publicapis.org/entries?category="
user_input = input("Enter a category: ")
url = main_api + user_input


response = requests.get(url)

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
    

jprint(response.json())