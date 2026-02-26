from data.courier_data import COURIER_BODY
from data.order_data import ORDER_BODY

def modify_courier_body(key, value):

    body = COURIER_BODY.copy()
    body[key] = value
    return body

def modify_order_body(key, value):

    body = ORDER_BODY.copy()
    body[key] = value
    return body

def remove_field_from_courier_body(field):

    body = COURIER_BODY.copy()
    if field in body:
        del body[field]
    return body

def remove_field_from_order_body(field):

    body = ORDER_BODY.copy()
    if field in body:
        del body[field]
    return body

