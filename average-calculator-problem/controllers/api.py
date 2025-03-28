import json
import os
from controllers import app
import requests

@app.route("/")
def hello_world():
    return "Server up and running at 5000"

@app.route('/number/<qualified_id>', methods=['GET'])
def number(qualified_id):
    # Qualified id can be p for prime, f for fibonacci, e for even and r for random
    window_size = 10 # Static value 10
    test_server_url = "http://20.244.56.144/test/"
    param= "primes" if qualified_id == "p" else "fibo" if qualified_id == "f" else "rand" if qualified_id == "r" else "even"
    token_body = requests.post("http://20.244.56.144/test/auth",
    data=json.dumps( {
        "companyName": "VainInnovations",
        "clientID": "6a1d938b-b358-464b-a276-ec11828e974a",
        "clientSecret": "FSYaEzhyibCtASiO",
        "ownerName": "Parag Gupta",
        "ownerEmail": "parag.24mca10062@vitbhopal.ac.in",
        "rollNo": "1"}))
    
    token = token_body.json()["access_token"]
    print(token)


    numbers_body = requests.get(test_server_url+param,headers={'Authorization': f'Bearer {token}'})
    numbers = numbers_body.json()['numbers']
    print(numbers_body.json())
    print(numbers_body.json()['numbers'])

    with open("numbers.txt","w") as f:
        f.write(str(numbers))

    f= open("numbers.txt","r")
    windowPrevState=f.read()

    return {"windowPrevState": windowPrevState,"windowCurrstate": numbers,"numbers": numbers,"avg": sum(numbers)/len(numbers)}
