import firebase_admin
from firebase_admin import auth, firestore, storage, credentials
#------------------------------------firebase database---------------------------------------
cred = credentials.Certificate("/content/build-d6b43-firebase-adminsdk-2mh7i-8b5622d29c.json")
firebase_app = firebase_admin.initialize_app(cred)
store = firestore.client()
#---------------------------------Auth's Code-------------------------------------------------
user = auth.create_user(
    email='bharat@luc.to',
    email_verified=False,
    password='124353')
print('Sucessfully created new user: {0}'.format(user.uid))


#--------------------------------------login------------------------------------------------
def login(emailofuser,passwordofuser):
  uid = ""
  message = ""
  try:
      user = auth.get_user_by_email(emailofuser)
      message = "successfully created new user"
      uid = user.uid
  except:
      message = "user not there in firebase!"
     
  return{"uid":uid, "message":message}
 
 
#-----------------------------------------Sign Up---------------------------------------------

def signUp(emailOfUser,passwordOfUser):
uid = ""
message =""
try:
  user = auth.create_user(email=emailOfUser,
                          email_varified=False,
                          password=passwordOfUser)
                         
   message = "Successfully created new user"
   uid = user.uid
except:
   message = "User Already There"
   
   return {"uid":uid, "message":message}


 #----------------------------------update the user profile-----------------------------------------
 def updateUserData(uid,dit):
 
   dit_user_details = {}
   dit_user_details['name'] = dit["name"]
   dit_user_details['email'] = dit["email"]
   dit_user_details['number'] = dit["number"]
   dit_user_details['image'] = dit["image"]
   dit_user_details['desp'] = dit["desp"]
   dit_user_details['location'] = dit["location"]
   dit_user_details['dob'] = dit["dob"]
   dit_user_details['gender'] = dit["gender"]
   dit_user_details['passion'] = dit["passion"]
   dit_user_details['job'] = dit["job"]
   dit_user_details['company'] = dit["company"]    
  store.collection("users").document(uid).set(dit_user_details)
 
 dit = {}
 dit["name"] = "roshan"
 dit["email"] = "roshan00@gmail.com"
 dit["number"] = "9898010101"
 dit["image"] = ""
 dit["desp"] = "single"
 dit["location"] = {
                        "coordinate" : {"lat":12.3271, "lng":74.15450},
                        "city" : "mumbai",
                        "state" : "maharashtra",
                        "country" : "india"
                    }
 dit["dob"] = "06/07/1996"
 dit["gender"] = "male"
 dit["passion"] = "study"
 dit["job"] = "student"
 dit["company"] = "university"
 
 #---------------------------------Get the FEED-----------------------------------------------
 
 def getFeed(country, gender)
    docs = store.collection("user").where("gender","==",gender).stream()
dit =()
for doc in docs:
    if doc.to.\_dict().get("location").get("country") == country
        dit[doc.id] = doc.to_dict()
    return dit
    
 #--------------------------
 
def swaipeFun(uidA, uidB,isA_Yes, isB_Yes, firstTime):

    dit
    
    dit["UID_A"] = uidA
    dit["UID_B"] = uidB
    
    dit["isUserA_Yes"] = isA_Yes
    dit["isUserB_Yes"] = isB_Yes
    
    dit["isTheOtherUserShownProfileAtLeastOnce"] = firstTime
    dit["createdAt"] = firestore.SERVER_TIMESTAMP
    
    store.collection("swipes").add(dit)
    
 uidA = "1st user id"
 uidB = "2nd user id" 
    
 isA_Yes = True
 isB_Yes = False
 
 firstTime = False
 
 swaipeFun(uidA, uidB,isA_Yes, isB_Yes, firstTime)
 
 
 def matchfun(uid):
        docs = store.collection("swipes").stream()
   ditswipes = {}
   for doc in docs:
   
   if doc.to_dict.get("uid_A") == uid or doc.to_dict.get("uid_B") == uid:
       ditswipes[doc.id] = doc.to_dict{}
 
   return ditswipes 
   
    
    
    
    
    
    
    
