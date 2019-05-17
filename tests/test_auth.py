import unittest
from tests import app
from api.models.database import db_connection

class TestApi(unittest.TestCase):
    """
    Class inherits from unittest class. Used for testing app.
    """

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        with self.app.test_client() as client:
           db_connection.create_tables()
           self.test_user1 = {"user_name":"ambrosebyamu","email":"ambrose@gmail.com",\
                "password":"12safgerg34F@"}

    def tearDown(self):
        db_connection.drop_tables() 

    def test_can_sign_up(self):
        response = self.client.post('/v2/api/signup', json = self.test_user1)
        self.assertIn('you have created an account', str(response.data))
        self.assertEqual(response.status_code, 201)

    def test_can_fetch_all_users_not_prote(self):
        response = self.client.get('/v2/api/users')
        self.assertEqual(response.status_code, 200)
