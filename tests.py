from hello import app
with app.test_client() as c:
    response = c.get('/')
    assert response.data == b'Hello World!'
    assert response.status_code == 200

    response = c.get('/long')
    assert response.data == b'end long'
    assert response.status_code == 200

    response = c.get('/bad')
    assert response.status_code == 500