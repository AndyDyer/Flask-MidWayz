import math
import requests
import json

'''
def main(url, key):
    r = requests.get(url+key)    #IS this functional or just for future purposes?
    print (r.json())
'''

def mean(data):
    n = len(data)
    if n < 1:
        raise ValueError('mean requires at least one data point')
    return sum(data)/float(n) 
    
def sumSquares(data):
    """Return sum of square deviations of sequence data."""
    mu = mean(data)
    ss = sum((x-mu)**2 for x in data)
    return ss
    
def stdDev(data):
    n = len(data)
    if n < 2:
        raise ValueError('variance requires at least two data points')
    ss = sumSquares(data)
    pvar = ss/n # the population variance
    return pvar**0.5

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

def stdDevChecker(data) :
    n = data
    latArr = []
    lonArr = []
    for index in range(len(n)) :
        if index % 2 == 0:
            latArr.append(data[index])
        else:
            lonArr.append(data[index])
    if stdDev(latArr) > .0015:
        return False
    else:
        return True
        
def triangularCenter(data) : 
    while stdDevChecker(data) != True: 
        ab = circleCenter(data[0],data[1],data[2], data[3])
        bc = circleCenter(data[2],data[3],data[4], data[5])
        ad = circleCenter(data[4],data[5],data[0], data[1])
        del data[:] 
        data = ab + bc + ad 
    #print sanitizeArray(data)

def sanitizeArray(dirtyArr) :
    temp = dirtyArr
    for index in range(len(temp)) :
        if index % 2 == 0 :
            temp[index] = float("%.7f" % temp[index]) #Longitude
        else : 
            temp[index] = float("%.6f" % temp[index]) #Latitude
    return temp
    

