import json
import os
from collections import OrderedDict
from controllers import app
import requests
from flask import request
import itertools
@app.route("/")
def hello_world():
    return "Server up and running at 5000"

@app.route('/users/', methods=['GET'])
def users():
    test_server_url = "http://20.244.56.144/test/"
     
    #getting acess token
    token_body = requests.post(f"{test_server_url}auth",
    data=json.dumps( {
        "companyName": "VainInnovations",
        "clientID": "6a1d938b-b358-464b-a276-ec11828e974a",
        "clientSecret": "FSYaEzhyibCtASiO",
        "ownerName": "Parag Gupta",
        "ownerEmail": "parag.24mca10062@vitbhopal.ac.in",
        "rollNo": "1"}))
    token = token_body.json()["access_token"]

    # Users
    users_data = requests.get(f"{test_server_url}users",headers={'Authorization': f'Bearer {token}'})

    user_dict = (users_data.json()["users"])
    new_dict = {}
    for i in range(1,6): new_dict[i]=user_dict[str(i)] #used this direct accessing way to get top 5

    return new_dict



@app.route('/posts/', methods=['GET'])
def posts():
    types = request.args.get('type') #latest,popular
    user = request.args.get('user') #as there is no mention of where to get user id to get posts we are taking that from query params

    test_server_url = "http://20.244.56.144/test/"
     
    #getting acess token
    token_body = requests.post(f"{test_server_url}auth",
    data=json.dumps( {
        "companyName": "VainInnovations",
        "clientID": "6a1d938b-b358-464b-a276-ec11828e974a",
        "clientSecret": "FSYaEzhyibCtASiO",
        "ownerName": "Parag Gupta",
        "ownerEmail": "parag.24mca10062@vitbhopal.ac.in",
        "rollNo": "1"}))
    token = token_body.json()["access_token"]
    if(types=="latest"):
        # posts
        posts_data = requests.get(f"{test_server_url}users/{user}/posts",headers={'Authorization': f'Bearer {token}'})

        return posts_data.json() # as we are getting five posts only we are not modifying
    
    else:
        posts_data_raw = requests.get(f"{test_server_url}users/{user}/posts",headers={'Authorization': f'Bearer {token}'})
        sorted_posts=[]
        posts_data=posts_data_raw.json()['posts']
        ranking = 0
        #Used loop based approtch as we dont have much time
        for i in posts_data:
            post_id = i['id']
            comments = requests.get(f"{test_server_url}posts/{post_id}/comments",headers={'Authorization': f'Bearer {token}'})
            comments_len = len(comments.json()["comments"])
            if(comments_len>ranking):
                sorted_posts.insert(0,i)
                ranking=comments_len
            else:
                sorted_posts.append(i)

        return sorted_posts
    