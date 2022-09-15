 
import os
import csv
import json

 

url_link="http://hostname.com/wp-json/wp/v2/posts/?per_page=100"

from urllib.request import urlopen

import requests



url = f'https://puntacanavilla.com/wp-json/wp/v2/properties?per_page=100'
listingss = requests.get(url).json()
 

# Write data to file
# filename = "posts json1.txt"
# file_ = open(filename, 'wb')
# file_.write(data)
# file_.close()

def get_image(img_id):

 
  url = f'https://puntacanavilla.com/wp-json/wp/v2/media/{img_id}'
  res = requests.get(url)
  
  
  img_url = res.json()['source_url']
  
  return img_url
  


def save_to_file (fn, row, fieldnames):
    
         if (os.path.isfile(fn)):
             m="a"
         else:
             m="w"
  
         
         with open(fn, m, encoding="utf8", newline='' ) as csvfile: 
           
             writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
             if (m=="w"):
                 writer.writeheader()
             writer.writerow(row)

# with open(filename) as json_file:
#     json_data = json.load(json_file)
    
 
'item_id,heading,propertyId,private_note,price,status,latitude,longitude,title,type,bedrooms,bathrooms,garage,garage_size,square_footage,land_size,size_postfix,image1,details,year_build,listing_date'
 
 
 
 
for n in listingss:  
 
  r={}
  
  
   
  
  
  
  r["item_id"] = n['id']
  r["heading"] = n['title']['rendered']
  r["propertyId"] = n['property_meta']['fave_property_id'][0]
  try:
    private_note = n['property_meta']['fave_private_note'][0]
  except:
    private_note = None
  r["private_note"] = private_note
  r["price"] = n['property_meta']['fave_property_price'][0]
  status = n['property_status'][0]
  if status == 145:
    status = "For sale"
  else:
    status = "For Rent"
 
  r["status"] = status
  r["country"] = n['property_country'][0]
  r["city"] = n['property_city'][0]
  r["address"] = n['property_meta']['fave_property_address'][0]
  r["state"] = n['property_state'][0]
  r["google_map"] = n['property_meta']['fave_property_map_street_view'][0]
  
  
  r["latitude"] = n['property_meta']['houzez_geolocation_lat'][0]
  r["longitude"] = n['property_meta']['houzez_geolocation_long'][0]
  r["title"] = n['content']
  type = n['property_type'][0]

  if type == 187:
    type = 'Punta Cana condos for sale'
  elif type == 180:
    type = 'Punta Cana Villas for Sale'
  elif type == 170:
    type = 'Residential'
  elif type == 186:
    type = 'Punta Cana Apartments for sale'
  elif type == 188:
    type = 'Punta Cana town-houses for sale'
        
  elif type == 245:
    type = 'Punta Cana houses for sale'
  elif type == 141:
    'Commercial'
  r["type"] = type
  
  r["bedrooms"] = n['property_meta']['fave_property_bedrooms'][0]
  r["bathrooms"] = n['property_meta']['fave_property_bathrooms'][0]
  try:
    garage = n['property_meta']['fave_property_garage'][0]
  except:
    garage = None
  r["garage"] = garage
  try:
    garage_size = n['property_meta']['fave_property_garage_size'][0]
  except:
    garage_size = None
            
  r["garage_size"] = garage_size
  
  r["square_footage"] = n['title']['rendered']
  r["land_size"] = n['property_meta']['fave_property_size'][0]
  r["size_postfix"] = n['property_meta']['fave_property_size_prefix'][0]
  featured_media = n['featured_media']
    
  img_url = get_image(featured_media)
     
  r["image1"] = img_url
  r['img_lists'] = n['property_meta']['fave_property_images']
  r["details"] = n['content']['rendered']
  try:
    year_build = n['property_meta']['fave_property_year'][0]
  except:
    year_build = None
  r["year_build"] = year_build
  
  r["listing_date"] = n['date']
   
  
  
  save_to_file("posts1.csv", r, ['item_id','heading','propertyId','private_note','price','status','country','city','address','state','google_map','latitude','longitude','title','type','bedrooms','bathrooms','garage','garage_size','square_footage','land_size','size_postfix','image1','img_lists','details','year_build','listing_date']) 