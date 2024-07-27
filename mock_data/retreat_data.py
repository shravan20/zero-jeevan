import requests
import json

API_URL = 'http://127.0.0.1:5000/retreats'
HEADERS = {
    'Content-Type': 'application/json'
}

# Sample retreat data
retreat_data = [
    {
        "title": "Yoga for Stress Relief",
        "description": "A weekend retreat focused on yoga and meditation to relieve stress.",
        "date": "2024-08-15",
        "location": "Goa",
        "price": 200.0,
        "type": "Signature",
        "condition": "Stress Relief",
        "image": "https://cdn.midjourney.com/a287f9bc-d0fb-4e78-a0fa-e8136d3c408a/0_0.jpeg",
        "tag": ["relaxation", "meditation", "weekend"],
        "duration": 3
    },
    {
        "title": "Meditation Retreat for Beginners",
        "description": "A week-long retreat to introduce you to the basics of meditation.",
        "date": "2024-09-10",
        "location": "Dharamshala",
        "price": 350.0,
        "type": "Beginner",
        "condition": "Meditation Introduction",
        "image": "https://example.com/meditation-retreat.jpg",
        "tag": ["meditation", "beginners", "week"],
        "duration": 7
    },
    {
        "title": "Advanced Wellness and Detox",
        "description": "An intensive wellness retreat focusing on detox and advanced wellness practices.",
        "date": "2024-10-01",
        "location": "Rishikesh",
        "price": 500.0,
        "type": "Advanced",
        "condition": "Detox",
        "image": "https://example.com/wellness-detox.jpg",
        "tag": ["wellness", "detox", "intensive"],
        "duration": 5
    }
]

def add_retreat(retreat):
    response = requests.post(API_URL, headers=HEADERS, data=json.dumps(retreat))
    if response.status_code == 201:
        print(f"Retreat '{retreat['title']}' added successfully.")
    else:
        print(f"Failed to add retreat '{retreat['title']}': {response.status_code} - {response.text}")

for retreat in retreat_data:
    add_retreat(retreat)
