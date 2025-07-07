import requests

def test_get_classes():
    response = requests.get('http://127.0.0.1:5000/classes')
    assert response.status_code == 200
    print(response.json())

def test_post_book():
    data = {
        "class_id": 1,
        "client_name": "Test User",
        "client_email": "test@example.com"
    }
    response = requests.post('http://127.0.0.1:5000/book', json=data)
    assert response.status_code == 201
    print(response.json())

def test_get_bookings():
    response = requests.get('http://127.0.0.1:5000/bookings?email=test@example.com')
    assert response.status_code == 200
    print(response.json())

if __name__ == '__main__':
    test_get_classes()
    test_post_book()
    test_get_bookings()
