import pyrebase
from time import gmtime, strftime

config = {
  "apiKey": "AIzaSyAESWd_hdkEmyeMFvI7_hlQbXqp9--51kA",
  "authDomain": "coffeeplease-ab6a7.firebaseapp.com",
  "databaseURL": "https://coffeeplease-ab6a7.firebaseio.com",
  "storageBucket": "coffeeplease-ab6a7.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

# To get old time
value = db.child("time").get()
print("Old value: " + value.val())

# To set current time as string
db.child("time").set(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

# Now to check current time saved
value = db.child("time").get()
print("New value: " +value.val())