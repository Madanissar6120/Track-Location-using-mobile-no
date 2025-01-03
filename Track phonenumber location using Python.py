import phonenumbers
from phonenumbers import geocoder
from location import number    
import folium

key="6d6f969fd9024ac8afde957f0c86a5ba"

number=input("Enter  valid Phone number with country code :")
#location
check_number=phonenumbers.parse(number)
number_location=geocoder.description_for_number(check_number,"en")
print(number_location)

# Sim operator(carrier)
from phonenumbers import carrier
service_provider=phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))


from opencage.geocoder import OpenCageGeocode 
geocoder = OpenCageGeocode(key)

query = str(number_location)
results=geocoder.geocode(query)


lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(f"Lattitude :{lat}\nLongitude :{lng}")


map_location=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=number_location).add_to(map_location)
map_location.save("Location5.html")