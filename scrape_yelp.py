import json
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

# load my keys
with open('.yelp_api_key.json') as f:
    api_key = json.load(f)

auth = Oauth1Authenticator(**api_key)
client = Client(auth)
