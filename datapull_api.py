import requests
import json
response_API = requests.get('https://api.covid19india.org/state_district_wise.json')
#print(response_API.status_code)
read_data = response_API.text
parse_json_file = json.loads(read_data)
active_cases = parse_json_file['Andhra Pradesh']['districtData']['East Godavari']['active']
print(active_cases)