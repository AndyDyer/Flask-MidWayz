/*
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
*/

function circleCenter(lat1,lon1, lat2, lon2){
    var rLat1 = lat1 * (Math.PI/180);
    console.log(rLat1)
    var rLat2 = lat2 * (Math.PI/180);
    var rLon1 = lon1 * (Math.PI/180);
    var dLon = (lon2-lon1) * (Math.PI/180);
    var Bx = Math.cos(rLat2) * Math.cos(dLon);
    var By = Math.cos(rLat2) * Math.sin(dLon);
    
    var finLat = Math.atan2((Math.sin(rLat1) +Math.sin(rLat2)), Math.sqrt((Math.cos(rLat1) + Bx)*(Math.cos(rLat1) + Bx) +By*By))
    var finLon = rLon1 + Math.atan2(By,Math.cos(rLat1) +Bx)
    //radians * (180/pi)
    finLat = finLat * (180/Math.PI)
    finLon = finLon * (180/Math.PI)
    console.log(finLat)
    console.log(finLon)
}
circleCenter(41.946974234239, -87.659225234324, 41.92246142342, -87.637942343239)