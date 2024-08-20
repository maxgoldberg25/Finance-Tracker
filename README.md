# Finance Tracker

Finance Tracker is a web application designed to help users manage their finances efficiently. The app provides tools to track income, monitor spending, and use financial insights to optimize savings. Built with modern web technologies, it offers a user-friendly interface for personal financial management.

## Features

- **Income Tracking**: Easily record and categorize your income sources.
- **Expense Management**: Track and categorize your spending to see where your money goes.
- **Financial Insights**: Generate reports and visualizations to understand your financial patterns and make informed decisions.
- **Budget Planning**: Set and manage budgets to help you stay on track with your financial goals.
- **Savings Goals**: Define and track progress towards your savings goals.

## Technologies Used

### Backend
- **Flask**: A lightweight WSGI web application framework in Python.
- **SQLAlchemy**: A SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **Flask-SQLAlchemy**: SQLAlchemy integration with Flask.

### Frontend
- **HTML5**: The structure of the web pages.
- **CSS3**: Styling of the web pages.
- **JavaScript**: Dynamic behavior and interactions on the site.

## Installation

To get a local copy up and running, follow these steps:

### Prerequisites

- Python 3.x
- Flask
- SQLAlchemy
- Flask-SQLAlchemy

### Installation Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/maxgoldberg25/Finance-Tracker.git
    cd Finance-Tracker
    ```

2. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```

3. Activate the virtual environment:
    - **On Windows:**
      ```bash
      .\venv\Scripts\Activate
      ```
    - **On macOS/Linux:**
      ```bash
      source venv/bin/activate
      ```

4. Install the dependencies:
    ```bash
    pip install Flask SQLAlchemy Flask-SQLAlchemy
    ```

5. Set up the database:
    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

6. Run the application:
    ```bash
    flask run
    ```

7. Open your browser and visit `http://127.0.0.1:5000`.

## Usage

- Register as a new user or log in with your existing account.
- Record and categorize your income and expenses.
- View financial reports and insights.
- Set budgets and track your savings goals.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your proposed changes.
