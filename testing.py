import math
import requests
import json
import urllib
from pprint import pprint

#Ok so we get lat and lngs for every bit with time. so lat0 lng 1 time 2  we can access by two lists based off i%3 = 0,1 or 2
'''
so we are tracking these values and the total time it takes to get from A - M and B - M. 
If these things are fine ie difference > 180s(flexible) we do nothing
if we do need to change we look at the array for each point. 

We determine whether or not to look through A-Array or B-Array 
'''
#AIzaSyBVLrwa5Xh3KV1I43rvDNNfT04kmEaNG6Q
 
#TODO Try and Catch these requests
def drivingEncoder(jsonResponse):
    aArray = []
    for j in jsonResponse['routes']:
        if 'legs' in  j.keys():
            for k in j['legs']:
                for l in k['steps']:
                    #print l['end_location']['lat']
                    #print l['end_location']['lng']
                    #print l['duration']['value']
                    print ""
                #print k['duration']['value']
def transitEncoder(jsonResponse):
    aArray=[]
    pprint (jsonResponse)
    for j in jsonResponse['routes']:
        for k in j['legs']:
            for l in k['steps']:
              #  print l['end_location']['lat']
               # print l['end_location']['lng']
                #print l['duration']['value']
                print 'l',l.keys()
                print len(l)
                print 'k', k.keys()
                print len(k)
                
                #for n in l['steps']:
                    
                '''
[u'html_instructions', u'distance', u'travel_mode', u'start_location', u'polyline', u'transit_details', u'duration', u'end_location']
8
41.9636351
-87.6504004
406
[u'html_instructions', u'distance', u'travel_mode', u'start_location', u'polyline', u'duration', u'steps', u'end_location']
?
How do i access this second dict without touching the other one?
                
                    print n['end_location']['lat']
                    print n['end_location']['lng']
                    print n['duration']['value']
                '''
    
def googleTwoPoints(data,mathmid, travel1, travel2, key):
    url1 ="https://maps.googleapis.com/maps/api/directions/json?origin="+ str(data[0]) + ',' + str(data[1]) + "&destination=" + str(mathmid[0]) + ',' + str(mathmid[1]) +"&mode="+ travel1 + "&key=" + key
    url2 ="https://maps.googleapis.com/maps/api/directions/json?origin="+ str(data[2]) + ',' + str(data[3]) + "&destination=" + str(mathmid[0]) + ',' + str(mathmid[1]) +"&mode="+ travel2 + "&key=" + key
    
    googleResponse = urllib.urlopen(url1)
    jsonResponse = json.loads(googleResponse.read())
    if (travel1 == 'driving'):
        print 'driving'
        #drivingEncoder(jsonResponse)
    if (travel1 == 'transit'):
        print 'transit'
        #transitEncoder(jsonResponse)
    if (travel1 == 'walking'):
        print 'walking'
    if (travel1 == 'bicycling'):
        print 'bicycling'
        #transitEncoder(jsonResponse)    
    googleResponse2 = urllib.urlopen(url2)
    jsonResponse2 = json.loads(googleResponse2.read())
    if (travel2 == 'driving'):
        print 'driving'
        drivingEncoder(jsonResponse2)
    if (travel2 == 'transit'):
        print 'transit'
        transitEncoder(jsonResponse2)
    if (travel2 == 'walking'):
        print 'walking'
    if (travel2 == 'bicycling'):
        print 'bicycling'
   
    
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

data = [42.004761, -87.662874, 41.92246142342, -87.637942343239]
mathmid = circleCenter(data[0],data[1],data[2],data[3])
mykey = "AIzaSyBVLrwa5Xh3KV1I43rvDNNfT04kmEaNG6Q"

googleTwoPoints(data, mathmid, "driving", "transit", mykey)
