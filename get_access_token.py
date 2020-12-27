# You need use this example code in to the main folder
from __future__ import print_function
import time
import meli
from meli.rest import ApiException
from pprint import pprint
from config import *
# Defining the host, defaults to https://api.mercadolibre.com
# See configuration.py for a list of all supported configuration parameters.
configuration = meli.Configuration(
    host = "https://api.mercadolibre.com"
)

def get_token():
	# Enter a context with an instance of the API client
	with meli.ApiClient() as api_client:
	# Create an instance of the API class
	    api_instance = meli.OAuth20Api(api_client)
	    grant_type = 'refresh_token' # 'authorization_code' or 'refresh_token' if you need get one new token --- 
	    client_id = APP_ID # Your client_id
	    client_secret = SECRET_KEY # Your client_secret
	    redirect_uri = 'https://mercadolibre.com.ar' # Your redirect_uri
	    code = '' # The parameter CODE, empty if your send a refresh_token
	    refresh_token = 'TG-5f5bcda6f5fd560006724234-114567020' # Your refresh_token

	try:
	    # Request Access Token
	    api_response = api_instance.get_token(grant_type=grant_type, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, code=code, refresh_token=refresh_token)
	    #print (api_response)
	    #print(api_response["access_token"]) #get token
	    token=api_response["access_token"]
	    #pprint(api_response)
	except ApiException as e:
	    print("Exception when calling OAuth20Api->get_token: %s\n" % e)
	return token

token=get_token()
#print(token)