from flask import request, Flask
import GmapsEncoder, MathUtils, json
app = Flask(__name__)
mykey = "AIzaSyBVLrwa5Xh3KV1I43rvDNNfT04kmEaNG6Q"

@app.route('/twoPoints', methods=['GET'])
def getTwo():
    #Flask does not like negative floats as params
    #http://127.0.0.1:5000/twoPoints?Lat1=42.004761&Lng1=-87.662874&Mode1=driving&Lat2=41.92246142342&Lng2=-87.637942343239&Mode2=driving
    lat1 = request.args.get('a')

    lng1 = str(request.args.get('b'))
    '''
    mode1 = str(request.args.get('Mode1'))
    lng2 = str(request.args.get('Lng2'))
    lat2 = str(request.args.get('Lat2'))
    mode2 = str(request.args.get('Mode2'))
    '''
    print lat1
    print 'space'
    print lng1

    return lng1
    '''
    Mid = MathUtils.circleCenter(lat1,lng1,lat2,lng2)
    cordpairs = [lat1, lng1, lat2, lng2]
    MidDict = GmapsEncoder.googleTwoPoints(cordpairs,Mid,mode1,mode2,cordpairs)
    return flask.jsonify(**MidDict)
    '''
#Take these and calculate and Jsonify
