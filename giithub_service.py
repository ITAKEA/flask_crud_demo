import requests
from dotenv import load_dotenv
import os
from db import read_all

# indlæs alle miljøvariabler fra .env filen
load_dotenv()

def get_repos(username):
    url = f'https://api.github.com/users/{username}/repos'
    req = requests.get(url)
    
    if req.status_code == 200:
        try:
            data = req.json()
            return [i['name'] for i in data]
        except ValueError:
            print("Invalid JSON response")
            return []
    else:
        return []


def merge_data():
    students = read_all()
    for i, v in enumerate(students):
        students[i]['repos'] = get_repos(v['github_username'])
    return students

