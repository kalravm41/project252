# importing flask modules
from flask import Flask , request , render_template , jsonify

# importing firebase_admin module
import firebase_admin

# importing firestore.py module to create firestore client
from firebase_admin import firestore

# importing credentials.py module from firebase_admin folder
from firebase_admin import credentials

# creating authentication file
cred = credentials.Certificate(creds)
default_app = initialize_app(cred)

# connect this python script/app with firebase using the authentication credentials
firebase_admin.initialize_app(cred)

# creating firestore client
firebase_db = firestore.client()

# creating flask object
app = Flask(__name__)

# first api : index page, only GET requests allowed at this API 
@app.route("/add-data", methods=["POST"])

def add_data():
    try:
        temperature = request.json.get['Temperature']
        humidity = request.json.get['Humidity']   
        altitude = request.json.get['Altitude']   
        pressure = request.json.get['Pressure']


       doc_ref = firebase_db.collection("Data")
       add_values = doc_ref.document().create(dict(
           Temperature = temperature,
           Humidity = humidity
           Altitude = altitude,
           Pressure = pressure,
           Date = datetime.utcnow()
       ))
 
        return jsonify({
            "status": "success"
        }), 201
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

@app.route("/")
def index():
   try:
       doc_ref = firebase_db.collection("Data")
       data = doc_ref.order_by("Date", direction = "DESCENDING").limit(1).get()[0].to_dict()
       return render_template("/home/home.html", data= Data)
   
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": "No Data In The Database Yet !!!"
        }), 400





# start the server
if __name__  ==  "__main__":
    app.run(host = '192.168.0.1', port=5000, debug = True)

