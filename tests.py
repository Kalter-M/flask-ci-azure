import unittest
import simpleapi


class Tests(unittest.TestCase):

    def setUp(self):
        self.app = simpleapi.app.test_client()
        self.app.testing = True

    def test_status_code(self):
        response = self.app.get('/1')
        self.assertEqual(response.data, b'value1')
        self.assertEqual(response.status_code, 201)

    def test_long_resp(self):
        response = self.app.get('/long')
        self.assertEqual(response.status_code, 200)

    def test_bad_resp(self):
        response = self.app.get('/bad')
        self.assertEqual(response.status_code, 500)


if __name__ == '__main__':
    unittest.main()
