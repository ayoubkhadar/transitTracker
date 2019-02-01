import urllib.request
import json

destination = input("Where are you heading? ").replace(" ","+")
origin = input("Where are you right now? ").replace(" ","+")
mode = input("Are you driving, biking, or transit? ").replace(" ","+")
departure = input("What time are you leaving? ").replace(" ","+")
key = "ENTER_YOUR_MAPS_API_KEY_HERE"

data = urllib.request.urlopen(f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origin}&destinations={destination}&mode={mode}&language=en-EN&departure_time={departure}&units=imperial&key={key}").read()
distance = json.loads(data)["rows"][0]["elements"][0]["distance"]["text"]
transitTime = json.loads(data)["rows"][0]["elements"][0]["duration"]["text"]
traffic = json.loads(data)["rows"][0]["elements"][0]["duration_in_traffic"]["text"]

print(f"Your transit time is {transitTime} and the distance is {distance}. You can expect to spend about {traffic} in traffic. you can find your direct route here https://www.google.com/maps/dir/{origin}/{destination}/")



