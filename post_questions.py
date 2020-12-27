"""
# You need use this example code in to the main folder
from __future__ import print_function
import time
import meli
from meli.rest import ApiException
from pprint import pprint
from config import * #TO USE TOKEN EVEN BUYER OR SELLER
from get_questions import pregunta2 as p2 #contenido de la pregunta 2 de 'get_questions.py'
# Defining the host is optional and defaults to https://api.mercadolibre.com
# See configuration.py for a list of all supported configuration parameters.
configuration = meli.Configuration(
    host = "https://api.mercadolibre.com"
)

# Enter a context with an instance of the API client
with meli.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = meli.RestClientApi(api_client)
    resource = '' #'items' # A resource like items, search, category etc
    access_token = ACCESS_TOKEN_VENDEDOR # Your access token.

    id_a_responder=11484245823
    texto_respuesta=('Recibido: ' + p2 + ' \n Y esto puesto a mano')

try:
    # Resource path GET
    api_response = api_instance.resource_post(resource, access_token)

except ApiException as e:
    print("Exception when calling RestClientApi->resource_get: %s\n" % e)

"""


from __future__ import print_function
import time
import meli
from meli.rest import ApiException
from pprint import pprint
from config import *
# Defining the host is optional and defaults to https://api.mercadolibre.com
# See configuration.py for a list of all supported configuration parameters.
configuration = meli.Configuration(
    host = "https://api.mercadolibre.com"
)


# Enter a context with an instance of the API client
with meli.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = meli.RestClientApi(api_client)
    resource = '/answers?access_token=' # str | 
    access_token = ACCESS_TOKEN_VENDEDOR # str | 
    body =  { # object | 
        'question_id':11484245823,
        'text':'Texto de respuesta hardcoded'
    }

    try:
        # Resourse path POST
        api_response = api_instance.resource_post(resource, access_token, body )
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RestClientApi->resource_post: %s\n" % e)