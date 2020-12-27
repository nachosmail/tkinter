# You need use this example code in to the main folder
#from __future__ import print_function
#import time
import meli
from meli.rest import ApiException
from pprint import pprint
from config import * #TO USE TOKEN EVEN BUYER OR SELLER
# Defining the host is optional and defaults to https://api.mercadolibre.com
# See configuration.py for a list of all supported configuration parameters.
configuration = meli.Configuration(
    host = "https://api.mercadolibre.com"
)

seller_id='644411786' #seller_prueba_user2

# Enter a context with an instance of the API client
with meli.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = meli.RestClientApi(api_client)
    resource = 'questions/search?seller_id=' + seller_id + '&access_token=' # A resource example like items, search, category, etc.
    access_token = ACCESS_TOKEN_VENDEDOR # Your access token.
try:
    # Resource path GET
    # TODO --> crear filtro que solamente traiga las que tienen estado 'UNANSWERED'
    api_response = api_instance.resource_get(resource, access_token)
    # pprint(api_response)
    cantidad_de_preguntas=api_response['total']
    # pprint(cantidad_de_preguntas) #--> arroja el numero de preguntas disponibles TOTAL
    pprint("Contenido de la pregunta: " + str(api_response['questions'][0]['text']))
    pprint("Contenido de la pregunta: " + str(api_response['questions'][1]['text']))
    pprint("Contenido de la pregunta: " + str(api_response['questions'][2]['text']))

    #-----pasar a variable las respuesta para jugar en la respuesta-----
    pregunta1=api_response['questions'][0]['text']
    pregunta2=api_response['questions'][1]['text']
    pregunta3=api_response['questions'][2]['text']
    #print (pregunta1,pregunta2)
    #--------------------------------------------------------------------

except ApiException as e:
    print("Exception when calling RestClientApi->resource_get: %s\n" % e)