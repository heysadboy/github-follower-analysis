import requests
import simplejson as json

username = "USERNAME"
password = "PASSWORD"
session = requests.Session()
session.auth = (username, password)

def get_followers():
    url = "https://api.github.com/users/heysadboy/followers"
    response = session.get(url)
    if response.status_code == 403:
        status = "API Limit reached"
        return status
    data = json.loads(response.text)

    followers = []
    try:
        for user in data:
            followers.append(user['login'])
    except Exception as e:
        print(e)
    
    return followers

def get_non_followers():
    followers = get_followers()
    url = "https://api.github.com/users/{}/following/heysadboy"
    non_followers = []
    for follower in followers:
        res = session.get(url.format(follower))
        print(follower, res.status_code)
        if res.status_code == 404:
            non_followers.append(follower)
    
    return non_followers

non_followers = get_non_followers()
print(non_followers)