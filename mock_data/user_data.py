import requests

user_data = [
    {"name": "Alice", "email": "alice@example.com", "phone": "123-456-7890"},
    {"name": "Bob", "email": "bob@example.com", "phone": "234-567-8901"},
    {"name": "Charlie", "email": "charlie@example.com", "phone": "345-678-9012"},
]

url = 'http://127.0.0.1:5000/users'

for user in user_data:
    response = requests.post(url, json=user)
    if response.status_code == 201:
        print(f"Successfully added user: {user['name']}")
    else:
        print(f"Failed to add user: {user['name']} with status code {response.status_code}")
