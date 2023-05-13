import requests

status = 'available'

res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus={status}", headers={'accept': 'application/json'})
print(res.text)

res_post = requests.post(
    'https://petstore.swagger.io/v2/pet',
    headers={'accept': 'application/json', 'Content-Type': 'application/json'},
    json={'name': 'cat', 'photoUrls': ['урл_фотографии']})
print(res_post.text)

res_put = requests.put(
    'https://petstore.swagger.io/v2/pet',
    headers={'accept': 'application/json', 'Content-Type': 'application/json'},
    json={'id': 9223372036854775807, 'name': 'cheburashka', 'photoUrls': ['урл_фотографии'], 'tags': []})
print(res_put.text)

res_delete = requests.delete(
    'https://petstore.swagger.io/v2/pet/9223372036854775807',
    headers={'accept': 'application/json'},
    json={'id': 9223372036854775807})
print(res_delete.text)
