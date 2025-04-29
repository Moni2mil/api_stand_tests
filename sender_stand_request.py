import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

#def get_users_table():
 #   return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH,  # inserta la dirección URL completa
#                         headers=data.headers)  # inserta los encabezados

response = post_new_user(data.user_body)
#response2 = get_users_table()
print(response.status_code)
print(response.json())
#print(response2.status_code)
#print(response2.json())