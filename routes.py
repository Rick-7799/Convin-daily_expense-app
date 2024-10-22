from flask import Blueprint, request, jsonify
from models import db, User, Expense

routes_app = Blueprint('routes', __name__)

@routes_app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(email=data['email'], name=data['name'], mobile_number=data['mobile_number'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created", "user_id": new_user.id}), 201

@routes_app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"id": user.id, "email": user.email, "name": user.name, "mobile_number": user.mobile_number}), 200

@routes_app.route('/expenses', methods=['POST'])
def add_expense():
    data = request.get_json()
    
    new_expense = Expense(total_amount=data['total_amount'], split_type=data['split_type'], user_id=data['user_id'])
    db.session.add(new_expense)
    db.session.commit()
    return jsonify({"message": "Expense added", "expense_id": new_expense.id}), 201

@routes_app.route('/users/<int:user_id>/expenses', methods=['GET'])
def get_user_expenses(user_id):
    expenses = Expense.query.filter_by(user_id=user_id).all()
    return jsonify([{"id": exp.id, "amount": exp.total_amount, "split_type": exp.split_type} for exp in expenses]), 200

@routes_app.route('/expenses/overall', methods=['GET'])
def get_overall_expenses():
    expenses = Expense.query.all()
    total_expenses = sum(exp.total_amount for exp in expenses)
    
    return jsonify({"total_expenses": total_expenses}), 200

@routes_app.route('/balance_sheet', methods=['GET'])
def download_balance_sheet():
    expenses = Expense.query.all()
    balance_sheet_data = [{"id": exp.id, "amount": exp.total_amount, "split_type": exp.split_type} for exp in expenses]
    
    return jsonify(balance_sheet_data), 200
