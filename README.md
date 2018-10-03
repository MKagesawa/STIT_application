## STIT Backend Programming Challenge

Access from Here: <http://34.220.229.141/>

Deployed on AWS EC2

### Description
Implemented with Python Flask

4 endpoints supported:
 - */register*: For user to register. User should provide email, password, category, and genre. A session will start upon registration.
 - */login*: For user to login to use service. A new session will be started. Use should provide email and password.
 - */getEvents*: Display events corresponding to user's preferences. It will display according to the current session user's preferences.
 - */setPreferences*: Allow user to change preferences for events.
 - */logout*: For user to logout. Session will be ended.
### To run
```
git clone https://github.com/MKagesawa/STIT_application
cd STIT_application
python3 app.py
```
Then use Postman/Restlet to test API

### API
``` 
/login
POST
Params:
    Required:
    email = [alphanumeric]
    password = [alphanumeric]

Success Response:
{
"data":{"Welcome": 1},
"state": true
}

Error Response: 
{
"error":{
"errorCode": 106,
"errorMsg": "Wrong password"
},
"state": false
}
```
```
/register
POST
Params:
    Required:
    email = [alphanumeric]
    password = [alphanumeric]
    
    Optional:
    category = [alphanumeric]
    genre = [alphanumeric]

Success Response:
{
"data":{"Welcome": 1},
"state": true
}

Error Response: 
{
"error":{
"errorCode": 105,
"errorMsg": "User exists already"
},
"state": false
}
```
```
/getEvents
GET
No Params

Success Response:
[{}, {"name": "JAY-Z and BEYONC\u00c9 - OTR II", "type": "event", "dates": {"start": {"localDate": "2018-10-04", "localTime": "19:30:00", "dateTime": "2018-10-05T02:30:00Z", "dateTBD": false, "dateTBA": false, "timeTBA": false, "noSpecificTime": false}, "timezone": "America/Los_Angeles", "status": {"code": "onsale"}, "spanMultipleDays": false}, "info": "This event will take place rain or shine. There is an (8) ticket limit for the public onsale. The presale ticket limits are (6) for Citi Cardmember, (8)Eight for all VIP offers and (4) four for all other offers. If you exceed the ticket limit, you may have any or all of your orders and tickets canceled without notice at the venue or Ticketmaster's discretion. There are no refunds, exchanges, or upgrades. There is no re-entry into the venue. The venue observes a Clear Bag Policy. For more information on this policy, refer to the \"Please Note\" information on this page or visit centurylinkfield.com.", "classifications": [{"primary": true, "segment": {"id": "KZFzniwnSyZfZ7v7nJ", "name": "Music"}, "genre": {"id": "KnvZfZ7vAv1", "name": "Hip-Hop/Rap"}, "subGenre": {"id": "KZazBEonSMnZfZ7vaa1", "name": "French Rap"}, "type": {"id": "KZAyXgnZfZ7v7nI", "name": "Undefined"}, "subType": {"id": "KZFzBErXgnZfZ7v7lJ", "name": "Undefined"}, "family": false}]}]

Error Response: 
{
"error":{
"errorCode": 108,
"errorMsg": "User not logged In"
},
"state": false
}
```
```
/setPreferences
POST
Params:
    Optional:
    category = [alphanumeric]
    genre = [alphanumeric]

Success Response:
{
"data":{"Welcome": 1},
"state": true
}

Error Response: 
{
"error":{
"errorCode": 108,
"errorMsg": "User not logged In"
},
"state": false
}
```
```
/logout
GET, POST
No Params

Success Response:
{
"data":{"Welcome": 1},
"state": true
}

Error Response: 
{
"error":{
"errorCode": 0,
"errorMsg": ""
},
"state": false
}
```
