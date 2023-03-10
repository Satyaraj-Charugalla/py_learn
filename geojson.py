"""
The api or the json_url that is being used here needs a autentcation key.
Hence it is not retriving anydata.
The code is working fine but it is failng to authenticate.
"""
import urllib.request, urllib.parse, urllib.error
import json

json_url = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url= json_url + urllib.parse.urlencode({'address':address})
    #The urllib.parse.urlencode({'address':address}) will encode the spaces 
    # or any seperators to the url based searches.
    print(f'Retriving URL {url}')
    urlopen = urllib.request.urlopen(url)
    data = urlopen.read().decode()
    print(f'Data retrived is {len(data)} characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status']!= 'OK':
        # The above if condition is used to check if the status is 'OK' or not 
        # and if the data retrived has the key 'Status'. 
        # To know more use the above url and see the key pair values.
        print('---------Failed to retrive data---------')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]

    print(f'Latitude: {lat} and Longitude: {lng}')
    location = js['results'][0]['formattted_address']
    print(location)