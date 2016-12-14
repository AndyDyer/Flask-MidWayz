import math
import requests
import json
import urllib
import MathUtils
from pprint import pprint
from sets import Set



#AIzaSyBVLrwa5Xh3KV1I43rvDNNfT04kmEaNG6Q

#TODO Try and Catch these requests
def bicyclingEncoder(jsonResponse):
    aArray = [0]
    for j in jsonResponse['routes']:
            for k in j['legs']:
                for l in k['steps']:
                    aArray.append(l['end_location']['lat'])
                    aArray.append(l['end_location']['lng'])
                    aArray.append(l['duration']['value'])
                aArray.insert(0,k['duration']['value'])
    aArray = list(map(float, aArray))
    return aArray
def walkingEncoder(jsonResponse):
    aArray = [0]
    for j in jsonResponse['routes']:
            for k in j['legs']:
                for l in k['steps']:
                    aArray.append(l['end_location']['lat'])
                    aArray.append(l['end_location']['lng'])
                    aArray.append(l['duration']['value'])
                aArray.insert(0,k['duration']['value'])
    aArray = list(map(float, aArray))
    return aArray
def drivingEncoder(jsonResponse):
    aArray = []
    for j in jsonResponse['routes']:
        if 'legs' in  j.keys():
            for k in j['legs']:
                for l in k['steps']:
                    aArray.append(l['end_location']['lat'])
                    aArray.append(l['end_location']['lng'])
                    aArray.append(l['duration']['value'])
                aArray.insert(0,k['duration']['value'])
    aArray = list(map(float, aArray))
    return aArray
'''
def transitEncoder(jsonResponse):
    aArray=[]
    pprint (jsonResponse)
    for j in jsonResponse['routes']:
        for k in j['legs']:
            for l in k['steps']:
              # print l['end_location']['lat']
               # print l['end_location']['lng']
                #print l['duration']['value']
                #print 'l',l.keys()
                #print len(l)
                #print 'k', k.keys()
                print (len(k))
                #for n in l['steps']:
'''
#TODO how do I make this smarter while verifying with gmaps.
def twoList(list1, list2):
    abset = Set()
    abval = abs(list1[0] - list2[0])
    while (abval > 4):
        abval = abs(list1[0] - list2[0])
        try:
            if (list1[0] > list2[0]):
                list2.append(list1[-3])
                list2.append(list1[-2])
                list2.append(list1[-1])
                list1[0] -= list1[-1]
                list2[0] += list1[-1]
                list1.pop()
                list1.pop()
                list1.pop()
            else:
                list1.append(list2[-3])
                list1.append(list2[-2])
                list1.append(list2[-1])
                list2[0] -= list1[-1]
                list1[0] += list1[-1]
                list2.pop()
                list2.pop()
                list2.pop()
            if abval in abset:
                raise Exception("Breaking Infinite Loop")
            else:
                abset.add(abval)
        except Exception as e:
            break
    finalpair ={'lat': (list1[-3]+list2[-3])/2, 'lng': (list1[-2]+list2[-2])/2 }
    return finalpair
def googleTwoPoints(data,mathmid, travel1, travel2, key):
    url1 ="https://maps.googleapis.com/maps/api/directions/json?origin="+ str(data[0]) + ',' + str(data[1]) + "&destination=" + str(mathmid[0]) + ',' + str(mathmid[1]) +"&mode="+ travel1 + "&key=" + key
    url2 ="https://maps.googleapis.com/maps/api/directions/json?origin="+ str(data[2]) + ',' + str(data[3]) + "&destination=" + str(mathmid[0]) + ',' + str(mathmid[1]) +"&mode="+ travel2 + "&key=" + key

    Route1 = []

    googleResponse = urllib.urlopen(url1)
    jsonResponse = json.loads(googleResponse.read())
    if (travel1 == 'driving'):
        print ('driving')
        Route1 = drivingEncoder(jsonResponse)
    if (travel1 == 'transit'):
        print ('transit')
        #Route1 = transitEncoder(jsonResponse)
    if (travel1 == 'walking'):
        print ('walking')
        Route1 = walkingEncoder(jsonResponse)
    if (travel1 == 'bicycling'):
        print ('bicycling')
        Route1 = bicyclingEncoder(jsonResponse2)

    Route2 = []
    googleResponse2 = urllib.urlopen(url2)
    jsonResponse2 = json.loads(googleResponse2.read())
    if (travel2 == 'driving'):
        print ('driving')
        Route2 = drivingEncoder(jsonResponse2)
    if (travel2 == 'transit'):
        print ('transit')
        #transitEncoder(jsonResponse2)
    if (travel2 == 'walking'):
        print ('walking')
        Route2 = walkingEncoder(jsonResponse2)
    if (travel2 == 'bicycling'):
        print ('bicycling')
        Route2 = bicyclingEncoder(jsonResponse2)
    else:
        raise Exception("invalid mode of transport")
    except Exception as e:
        break

    twoList(Route1, Route2)

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

##Below is example data just to prove it works. Same as below request.
##http://127.0.0.1:5000/twoPoints?Lat1=42.004761,Lng1=-87.662874,Mode1=driving,Lat2=41.92246142342,Lng2=-87.637942343239,Mode2=driving

data = [42.004761, -87.662874, 41.92246142342, -87.637942343239]
mathmid = MathUtils.circleCenter(data[0],data[1],data[2],data[3])
mykey = "AIzaSyBVLrwa5Xh3KV1I43rvDNNfT04kmEaNG6Q"
googleTwoPoints(data, mathmid, "driving", "driving", mykey)
