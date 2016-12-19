import math
import requests
import json
import urllib
import MathUtils
from pprint import pprint
from sets import Set

def Encoder(jsonResponse):
    aArray = [0] #was [0] why did i do that?
    for j in jsonResponse['routes']:
            for k in j['legs']:
                for l in k['steps']:
                    aArray.append(l['end_location']['lat'])
                    aArray.append(l['end_location']['lng'])
                    aArray.append(l['duration']['value'])
                aArray.insert(0,k['duration']['value'])
    aArray = list(map(float, aArray))
    return aArray
def transitEncoder(jsonResponse):
    aArray = [0] #was [0] why did i do that?
    for j in jsonResponse['routes']:
        for k in j['legs']:
            for l in k['steps']:
                aArray.append(l['end_location']['lat'])
                aArray.append(l['end_location']['lng'])
                aArray.append(l['duration']['value'])
                if 'steps' in l:
                    for index in range(len(l['steps'])):
                        aArray.append(l['steps'][index]['end_location']['lat'])
                        aArray.append(l['steps'][index]['end_location']['lng'])
                        aArray.append(l['steps'][index]['duration']['value'])
            aArray.insert(0,k['duration']['value'])
    aArray = list(map(float, aArray))
    return aArray
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
            print e
            break
    finalpair ={'lat': (list1[-3]+list2[-3])/2, 'lng': (list1[-2]+list2[-2])/2 }
    print finalpair, abset
    return finalpair
def googleTwoPoints(data,mathmid, travel1, travel2, key):
    url1 ="https://maps.googleapis.com/maps/api/directions/json?origin="+ str(data[0]) + ',' + str(data[1]) + "&destination=" + str(mathmid[0]) + ',' + str(mathmid[1]) +"&mode="+ travel1 + "&key=" + key
    url2 ="https://maps.googleapis.com/maps/api/directions/json?origin="+ str(data[2]) + ',' + str(data[3]) + "&destination=" + str(mathmid[0]) + ',' + str(mathmid[1]) +"&mode="+ travel2 + "&key=" + key
    Route1 = []
    googleResponse = urllib.urlopen(url1)
    jsonResponse = json.loads(googleResponse.read())
    if (travel1 == 'driving'):
        print ('driving')
        Route1 = Encoder(jsonResponse)
    if (travel1 == 'transit'):
        print ('transit')
        Route1 = transitEncoder(jsonResponse)
    if (travel1 == 'walking'):
        print ('walking')
        Route1 = Encoder(jsonResponse)
    if (travel1 == 'bicycling'):
        print ('bicycling')
        Route1 = Encoder(jsonResponse2)
    Route2 = []
    googleResponse2 = urllib.urlopen(url2)
    jsonResponse2 = json.loads(googleResponse2.read())
    if (travel2 == 'driving'):
        print ('driving')
        Route2 = Encoder(jsonResponse2)
    if (travel2 == 'transit'):
        print ('transit')
        Route2 = transitEncoder(jsonResponse2)
    if (travel2 == 'walking'):
        print ('walking')
        Route2 = Encoder(jsonResponse2)
    if (travel2 == 'bicycling'):
        print ('bicycling')
        Route2 = Encoder(jsonResponse2)
    twoList(Route1, Route2)
##Below is example data just to prove it works. Same as below request.
##http://127.0.0.1:5000/twoPoints?Lat1=42.004761,Lng1=-87.662874,Mode1=driving,Lat2=41.92246142342,Lng2=-87.637942343239,Mode2=driving
data = [42.004761, -87.662874, 41.92246142342, -87.637942343239]
mathmid = MathUtils.circleCenter(data[0],data[1],data[2],data[3])
googleTwoPoints(data, mathmid, "transit", "driving", mykey)
