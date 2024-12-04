import requests
import json
import urllib
import os

headers = {
        'User-Agent': 'MyApp/1.0 (contact@example.com)', 
        'Accept': 'application/json',  
    }

def send_get_for_osm_id(headers,search_parameter,city,category):

    encoded_query_parameter = urllib.parse.quote(search_parameter)
    
    url = f'https://nominatim.openstreetmap.org/search.php?q={encoded_query_parameter}&format=jsonv2'
   
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if(len(data) > 1):
            for entry in data:
                if city in entry['display_name'] and category in entry['category']:
                    osm_id = entry['osm_id']
        elif(len(data) == 1):
            osm_id = data[0]['osm_id']
        else:
            osm_id = None
        return osm_id
    else:
        print(f'Błąd: {response.status_code}')
        return None
        
def get_geojson_data(headers,osm_id):
    url = f'https://polygons.openstreetmap.fr/get_geojson.py?id={osm_id}&params=0'
   
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Błąd: {response.status_code}')
        return None

with open('dzielnice.json','r',encoding='utf-8') as names:
    data = json.load(names)

    city = data.get('city', '')
    category = data.get('category', '')
    
    names_list = data.get('names', [])
    
    for name in names_list:
        osm_id = send_get_for_osm_id(headers,name,city,category)
        if(osm_id == None):
            print(f" failure: {name}")
            
            continue
        geodata_for_district = get_geojson_data(headers,osm_id)
        if(geodata_for_district == None):
            print(f" failure: {name}")
            continue
        print(f"success: {name}")
        
    
        file_path = f'./districts/{name.replace(" ", "_").lower()}.geojson'
        
        if not os.path.exists('./districts'):
            os.makedirs('./districts')

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(geodata_for_district, file, ensure_ascii=False, indent=4)

        print(f'\t Geodata saved to file: {file_path}')


    
    
