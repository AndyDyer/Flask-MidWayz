from flask import request, Flask
app = Flask(__name__)
@app.route('/two', methods=['GET', 'POST'])
def getModules():
    a = request.args.get('Apples')
    b = request.args.get('Bananas')
    print (a,b)
    return [a,b]

'''
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
'''
