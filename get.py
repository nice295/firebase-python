import pyrebase

config = {
  "apiKey": "AIzaSyAESWd_hdkEmyeMFvI7_hlQbXqp9--51kA",
  "authDomain": "coffeeplease-ab6a7.firebaseapp.com",
  "databaseURL": "https://coffeeplease-ab6a7.firebaseio.com",
  "storageBucket": "coffeeplease-ab6a7.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

value = db.child("x").get()
print(value.val())
