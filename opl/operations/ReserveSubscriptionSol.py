import requests,json


def reserve_subscription_sol(req):
    reserve_url='http://localhost:8000/sol/reserve/subscription'
    response=requests.post(url=reserve_url,data=json.dumps(req),headers={'Content-type': 'application/json'})
    return response.json()
