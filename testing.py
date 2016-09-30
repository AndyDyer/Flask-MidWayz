import math
import requests
import json
import urllib
from pprint import pprint


#AIzaSyBVLrwa5Xh3KV1I43rvDNNfT04kmEaNG6Q
 
 #http://stackoverflow.com/questions/4639311/parsing-json-file-with-python-google-map-api this guy is a god 
    
def googleTwoPoints(data,mathmid, travel1, travel2, key):
    
    
    
    
    url1 ="https://maps.googleapis.com/maps/api/directions/json?origin="+ str(data[0]) + ',' + str(data[1]) + "&destination=" + str(mathmid[0]) + ',' + str(mathmid[1]) +"&mode="+ travel1 + "&key=" + key
    url2 ="https://maps.googleapis.com/maps/api/directions/json?origin="+ str(data[2]) + ',' + str(data[3]) + "&destination=" + str(mathmid[0]) + ',' + str(mathmid[1]) +"&mode="+ travel2 + "&key=" + key
    googleResponse = urllib.urlopen(url1)
    jsonResponse = json.loads(googleResponse.read())
    #print jsonResponse
    print "heya, ", type(jsonResponse)
    print type(jsonResponse['routes'])
    print len(jsonResponse['routes'])
    print jsonResponse.keys(), " initial dictionary"
    for j in jsonResponse['routes']:
        print j.keys(), "  in loop with other keys"
        if 'legs' in  j.keys():
            print len(j['legs'])
            for k in j['legs']:
                print type(k)
                print k.keys()
                print k['steps']
                print type(k['steps'])
                for l in k['steps']:
                    print type(l)
                    print l
    #print dir(jsonResponse)
    #test = json.dumps([s['legs']for s in jsonResponse['routes']], indent=3)
   
    #test2 = json.loads(test)
    #Trying to access the steps level of this json. 
    #pprint (jsonResponse)
    
   
    
    
def circleCenter(lat1, lon1, lat2, lon2):
    rLat1 = math.radians(lat1)
    rLat2 = math.radians(lat2)
    rLon1 = math.radians(lon1)
    dLon  = math.radians(lon2 - lon1)
    Bx = math.cos(rLat2) * math.cos(dLon)
    By = math.cos(rLat2) * math.sin(dLon)
    finLat = math.atan2(math.sin(rLat1)+ math.sin(rLat2), 
                        math.sqrt((math.cos(rLat1) + Bx) * 
                        (math.cos(rLat1) + Bx) + By*By))
    finLon = rLon1 + math.atan2(By, math.cos(rLat1) + Bx)
    finLat = math.degrees(finLat)
    finLon = math.degrees(finLon)
    x = [finLat, finLon]
    return x

data = [41.946974234239, -87.659225234324, 41.92246142342, -87.637942343239,]
mathmid = circleCenter(data[0],data[1],data[2],data[3])

url = "https://maps.googleapis.com/maps/api/directions/json?origin=Toronto&destination=Montreal&key="
mykey = "AIzaSyBVLrwa5Xh3KV1I43rvDNNfT04kmEaNG6Q"

googleTwoPoints(data, mathmid, "driving", "transit", mykey)
