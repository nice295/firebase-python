import pyrebase

config = {
  "apiKey": "AIzaSyAESWd_hdkEmyeMFvI7_hlQbXqp9--51kA",
  "authDomain": "coffeeplease-ab6a7.firebaseapp.com",
  "databaseURL": "https://coffeeplease-ab6a7.firebaseio.com",
  "storageBucket": "coffeeplease-ab6a7.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

def stream_handler(message):
    #print(message["event"]) # put
    #print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    #print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}

    if message["data"] == "idle":
        print("Robot is waiting...")
    else:
        if message["data"] == "moving":           
            print("Robot is moving...")
        else:
            print("Robot is thinking...")   

my_stream = db.child("event").stream(stream_handler)

print("Event listening...")