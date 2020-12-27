from pprint import pprint

from ApiCaller import ApiCaller


def quedarse_con_pedientes(preguntas):
    return preguntas['status'] == 'UNANSWERED'

seller_id = '644411786'  # seller_prueba_user2
order_id='4043504868'

api = ApiCaller()

response = api.call_get_questions(seller_id)
questions = response['questions']
for question in questions:
    item = api.call_get_item_by_id(question['item_id'])
    #pprint(item)

    category = api.call_get_category_attributes_by_id(item[0]['body']['category_id'])
    pprint(category[22]['attribute_group_name'])





"""
#SECCION PARA INFORMACION DE LAS ORDENES DE COMPRA
order=api.get_order_info(order_id)
print(order['buyer']['nickname'])
"""


"""
#SECCION PARA LA MENSAJERIA DESPUES DE LA COMPRA
messages= api.get_messages_after_sale(order_id,seller_id)
print(messages['messages'][0]['text'])
#------------------------------
"""
