from flask import Flask, request, session, jsonify
import requests
from util import query_fetch, query_mod, SuccessResponse, ErrorResponse
from config import DB, secret_key
from hashlib import md5
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key

url = 'https://yv1x0ke9cl.execute-api.us-east-1.amazonaws.com/prod/events'
my_token = 'Basic c3RpdGFwcGxpY2FudDp6dmFhRHNaSExOTEZkVVZaXzNjUUtucw=='

@app.route('/login', methods=['POST'])
def login_user():
    try:
        session.pop('user', None)
        email = request.headers.get('email')
        # Password encoded with utf-8 first then encoded with md5
        password = md5(request.headers.get('password').encode('utf-8')).hexdigest()
        sql = 'SELECT password FROM user WHERE Email = "{}"'.format(email)
        db_pwd = query_fetch(sql, DB)
        if db_pwd is None:
            response = ErrorResponse()
            err = "This user has not been registered"
            response.error['errorCode'] = 107
            response.error['errorMsg'] = err
        elif password == db_pwd['password']:
            response = SuccessResponse()
            session['user'] = email
        else:
            response = ErrorResponse()
            err = "Wrong password"
            response.error['errorCode'] = 106
            response.error['errorMsg'] = err
        return jsonify(response.__dict__)
    except Exception as e:
        response = ErrorResponse()
        return jsonify(response.__dict__)

@app.route('/register', methods=['POST'])
def register_user():
    try:
        email = request.headers.get('email')
        password = md5(request.headers.get('password').encode('utf-8')).hexdigest()
        category = request.headers.get('category')
        genre = request.headers.get('genre')
        sql_check = 'SELECT * FROM user WHERE email = "{}"'.format(email)
        user_exist = query_fetch(sql_check, DB)
        if user_exist is not None:
            response = ErrorResponse()
            response.error['errorCode'] = 105
            response.error['errorMsg'] = 'User exists already'
        else:
            response = SuccessResponse()
            sql = 'INSERT INTO user VALUES("{}", "{}", "{}", "{}")'.format(email, password, category, genre)
            query_mod(sql, DB)
            session['user'] = email
        return jsonify(response.__dict__)
    except Exception as e:
        response = ErrorResponse()
        return jsonify(response.__dict__)

@app.route('/getEvents', methods=['GET'])
def get_events():
    try:
        sql_classification = "SELECT Category FROM user WHERE email = '{}'".format(session['user'])
        sql_genre = "SELECT Genre FROM user WHERE email = '{}'".format(session['user'])
        classificationName = query_fetch(sql_classification, DB)['Category']
        genreId = query_fetch(sql_genre, DB)['Genre']
        response = requests.get(url, headers={'Authorization': my_token,
                                                   'classificationName': classificationName, 'genreId': genreId}).json()
        return json.dumps(response)
    except Exception as e:
        response = ErrorResponse()
        response.error['errorCode'] = 108
        response.error['errorMsg'] = 'User not logged In'
        return jsonify(response.__dict__)

@app.route('/setPreferences', methods=['POST'])
def set_preferences():
    try:
        category = request.headers.get('category')
        genre = request.headers.get('genre')
        sql = "UPDATE user SET Category = '{}', Genre = '{}' WHERE email = '{}'".format(category, genre, session['user'])
        query_mod(sql, DB)
        response = SuccessResponse()
        return jsonify(response.__dict__)
    except Exception as e:
        response = ErrorResponse()
        response.error['errorCode'] = 108
        response.error['errorMsg'] = 'User not logged In'
        return jsonify(response.__dict__)

@app.route('/logout', methods = ['GET', 'POST'])
def logout():
    try:
        session.pop('user', None)
        response = SuccessResponse()
        return jsonify(response.__dict__)
    except Exception as e:
        response = ErrorResponse()
        return jsonify(response.__dict__)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
