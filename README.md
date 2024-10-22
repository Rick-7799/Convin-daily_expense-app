

```markdown
# Daily Expenses Sharing Application

This is a Flask-based web application designed for managing daily expenses and sharing costs among users. Users can add expenses, split them in various ways, and keep track of their financial contributions.

## Features

- **User Management**: Create and retrieve user profiles.
- **Expense Management**: Add expenses and retrieve individual user expenses.
- **Expense Splitting**: Split expenses using equal, exact, or percentage methods.
- **JWT Authentication**: Secure access to the application using JSON Web Tokens (JWT).
- **API Endpoints**: Interact with the application programmatically through RESTful API endpoints.

## Technologies Used

- Flask
- Flask-SQLAlchemy
- Flask-JWT-Extended
- SQLite (for database)

## Installation Instructions

Follow these steps to set up and run the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/daily_expenses_app.git
   cd daily_expenses_app
   ```

2. **Create a Virtual Environment**:
   It's a good practice to use a virtual environment to manage dependencies.
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install Dependencies**:
   Install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**:
   Start the Flask application:
   ```bash
   python app.py
   ```
   The application will be running at `http://127.0.0.1:5000`.

## Interacting with API Endpoints

You can interact with the application using various API endpoints. Below are some examples of how to use these endpoints:

### User Endpoints

1. **Create User**
   - **Endpoint**: `POST /users`
   - **Request Body**:
     ```json
     {
       "email": "user@example.com",
       "name": "John Doe",
       "mobile_number": "1234567890"
     }
     ```

2. **Retrieve User Details**
   - **Endpoint**: `GET /users/<user_id>`
   - Replace `<user_id>` with the actual user ID.

### Expense Endpoints

1. **Add Expense**
   - **Endpoint**: `POST /expenses`
   - **Request Body**:
     ```json
     {
       "total_amount": 3000,
       "split_type": "equal",
       "user_id": 1,
       "participants": ["user@example.com", "friend@example.com"]
     }
     ```

2. **Retrieve Individual User Expenses**
   - **Endpoint**: `GET /users/<user_id>/expenses`
   - Replace `<user_id>` with the actual user ID.

3. **Retrieve Overall Expenses**
   - **Endpoint**: `GET /expenses/overall`

4. **Download Balance Sheet**
   - **Endpoint**: `GET /balance_sheet`

### Authentication Endpoint

1. **Login**
   - **Endpoint**: `POST /login`
   - **Request Body**:
     ```json
     {
       "email": "user@example.com",
       "password": "your_password"
     }
     ```

## Running Tests

To run the automated tests for this application, execute:
```bash
python -m unittest test_app.py
```

```
