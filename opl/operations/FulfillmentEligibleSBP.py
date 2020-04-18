import requests,json


def fulfillment_eligible_sbp(req):
    class DatetimeEncoder(
        json.JSONEncoder):  # this class is meant to serialize the date time to json format otherwise json.dumps will fail
        def default(self, obj):
            try:
                return super(DatetimeEncoder, obj).default(obj)
            except TypeError:
                return str(obj)
    reqs = json.dumps(req, cls=DatetimeEncoder)

    fe_url='http://localhost:8000/sol/fulfillment/holdrelease'

    response=requests.post(url=fe_url,data=reqs,headers={'Content-type': 'application/json'})
    return response.json()
