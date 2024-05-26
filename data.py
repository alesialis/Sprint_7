# url и endpoint
URL = 'https://qa-scooter.praktikum-services.ru'
CREATE_COURIER_URL = '/api/v1/courier'
DELETE_COURIER_URL = '/api/v1/courier/'
LOGIN_COURIER_URL = '/api/v1/courier/login'
CREATE_ORDER_URL = '/api/v1/orders'
GET_ORDERS_URL = '/api/v1/orders'

# тексты в ответах на запросы
SUCCESSFUL_CREATE_COURIER = {'ok': True}
DUPLICATE_COURIER = 'Этот логин уже используется. Попробуйте другой.'
NOT_ENOUGH_DATA_CREATE_COURIER = 'Недостаточно данных для создания учетной записи'
NOT_FOUND_COURIER = 'Учетная запись не найдена'
NOT_ENOUGH_DATA_LOGIN_COURIER = 'Недостаточно данных для входа'
