import meli
from meli.rest import ApiException
from Profile import Profile


class ApiCaller(Profile):
    api_instance = ''

    configuration = meli.Configuration(
        host="https://api.mercadolibre.com"
    )

    def __init__(self):
        with meli.ApiClient() as api_client:
            self.api_instance = meli.RestClientApi(api_client)

    def call_get_questions(self, seller_id):
        resource = 'questions/search?seller_id=' + seller_id + '&access_token='
        try:
            api_response = self.api_instance.resource_get(resource, self.access_token)
            return api_response
        except ApiException as e:
            print("Exception when calling RestClientApi->resource_get: %s\n" % e)

    def call_post_answer(self, question):
        resource = '/answers?access_token='

        body = {  # object |
            'question_id': question['id'],
            'text': 'Texto de respuesta hardcoded'
        }

        try:
            api_response = self.api_instance.resource_post(resource, self.access_token, body)
            return api_response
        except ApiException as e:
            print("Exception when calling RestClientApi->resource_post: %s\n" % e)

    def call_get_item_by_id(self, item_id):
        resource = '/items?ids=' + item_id + '&access_token='
        try:
            api_response = self.api_instance.resource_get(resource, self.access_token)
            return api_response
        except ApiException as e:
            print("Exception when calling RestClientApi->resource_get: %s\n" % e)

    def call_get_category_attributes_by_id(self, category_id):
        resource = '/categories/' + category_id + '/attributes'
        try:
            api_response = self.api_instance.resource_get(resource, self.access_token)
            return api_response
        except ApiException as e:
            print("Exception when calling RestClientApi->resource_get: %s\n" % e)
            
    def get_order_info(self,order_id):
            resource='orders/' + order_id + '?access_token=' # A resource example like items, search, category, etc.
                                #PACK_ID --> al ser null se pone el ORDER_ID
            try:
                api_response=self.api_instance.resource_get(resource,self.access_token)
                #pprint(api_response)
                return api_response
            except ApiException as e:
                print("Exception when calling RestClientApi->resource_get: %s\n" % e)
            
    def get_messages_after_sale(self,order_id,seller_id):
        resource='messages/packs/' + order_id + '/sellers/' + seller_id + '?access_token='
        try:
            api_response=self.api_instance.resource_get(resource,self.access_token)
            return api_response
        except ApiException as e:
            print("Exception when calling RestClientApi->resource_get: %s\n" % e)
