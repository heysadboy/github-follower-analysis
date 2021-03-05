import requests
import simplejson as json

username = "username"
token = "token"
headers = {'Authorization': 'token ' + token}

def get_followers():
    url = "https://api.github.com/user/following?per_page=100"
    response = requests.get(url, headers = headers)
    if response.status_code == 403:
        status = "API Limit Reached"
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
    url = "https://api.github.com/users/{follower}/following/{username}"
    non_followers = []
    for (i, follower) in enumerate(followers):
        res = requests.get(url.format(follower = follower, username = username), headers = headers)
        if res.status_code == 404:
            non_followers.append(follower)
    return non_followers

non_followers = get_non_followers()

if len(non_followers) == 0:
    print("No non-followers")
else:
    print("Here is the list of traitors")
    for non_follower in non_followers:
        print(non_follower)