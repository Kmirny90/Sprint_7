class URL:

    BASE_URL = "https://qa-scooter.praktikum-services.ru"
    COURIER_CREATE = f"{BASE_URL}/api/v1/courier"
    COURIER_LOGIN = f"{BASE_URL}/api/v1/courier/login"
    COURIER_DELETE = f"{BASE_URL}/api/v1/courier/"  # + id
    ORDERS_CREATE = f"{BASE_URL}/api/v1/orders"
    ORDERS_GET = f"{BASE_URL}/api/v1/orders"
    ORDERS_CANCEL = f"{BASE_URL}/api/v1/orders/cancel"
    ORDERS_FINISH = f"{BASE_URL}/api/v1/orders/finish/"
    ORDERS_ACCEPT = f"{BASE_URL}/api/v1/orders/accept/"
    ORDERS_TRACK = f"{BASE_URL}/api/v1/orders/track"
