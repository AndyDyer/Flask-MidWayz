from yelp import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from yelp.obj.search_response import SearchResponse

auth = Oauth1Authenticator(
    consumer_key=QKodnM4cvgney-eyscrl6g,
    consumer_secret=voK2W34WBrqReDvd8PZ_9WWFZ-k,
    token=hONXwy3QeD-Fd-uWQY0cuMeJOvTRTZZ5,
    token_secret=t-wyckuw6OvUktL8XAyPA4zckT4
)

client = Client(auth)
params = {
    'term': 'food, coffee',
    'limit': 10
}

response = client.search_by_coordinates(42.004761, -87.662874, **params)
