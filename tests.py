import json

from simpleapi import app
with app.test_client() as c:
    response = c.get('/')
    assert response.data != b''
    assert response.status_code == 200

    response = c.get('/1')
    assert response.data == b'value1'
    assert response.status_code == 200

    # response = c.post('/', data=json.dumps({'val': 'valueeee45', 'id': '7'}))

    response = c.get('/long')
    assert response.data == b'end long'
    assert response.status_code == 200

    response = c.get('/bad')
    assert response.status_code == 500

    print("TESTS DONE")