from flask import Flask
from flask_cors import CORS, cross_origin
import db
from bson.json_util import loads, dumps

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/scrapedData')
@cross_origin()
def getScrapedData():
    # data is returned from the db in BSON format
    # BSON data encodes types like objectIDs. This cannot be serialized by json.dumps
    # serialize means to convert the object to a string
    scrapingData = db.scrapingResultColl.find()
    
    # bson library is used to serialize the BSON object
    response = dumps(scrapingData)
    return response

if __name__ == '__main__':
    app.run(port=8000)