# You need use this example code in to the main folder
from __future__ import print_function
import time
import meli
from meli.rest import ApiException
from pprint import pprint
from get_access_token import *
# Defining the host is optional and defaults to https://api.mercadolibre.com
# See configuration.py for a list of all supported configuration parameters.
configuration = meli.Configuration(
    host = "https://api.mercadolibre.com"
)


# Enter a context with an instance of the API client
with meli.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = meli.RestClientApi(api_client)
    resource = 'users/me?access_token=' # A resource example like items, search, category, etc.
    access_token = token # Your access token.

try:
    # Resource path GET
    api_response = api_instance.resource_get(resource, access_token)
    #pprint(api_response["nickname"])
    print("Nickname: " + str(api_response["nickname"]))
except ApiException as e:
    print("Exception when calling RestClientApi->resource_get: %s\n" % e)