import unittest
from app import app, db

class ExpenseAppTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_user(self):
        response = self.app.post('/users', json={'email': 'test@example.com', 'name': 'Test User', 'mobile_number': '1234567890'})
        self.assertEqual(response.status_code, 201)

    def test_add_expense(self):
        self.app.post('/users', json={'email': 'test@example.com', 'name': 'Test User', 'mobile_number': '1234567890'})
        response = self.app.post('/expenses', json={'total_amount': 1000, 'split_type': 'equal', 'user_id': 1})
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
