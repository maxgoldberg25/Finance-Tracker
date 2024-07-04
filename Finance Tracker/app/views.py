from flask import render_template, redirect, url_for, request, flash, Blueprint
from flask_login import login_user, login_required, logout_user, current_user
from .forms import LoginForm, RegisterForm
from .models import User, db
from werkzeug.security import generate_password_hash, check_password_hash

def init_views(app):
    
    @app.route('/')
    def home():
        return render_template('home.html')
    
    @app.route('/dashboard')
    @login_required
    def about():
        return render_template('dashboard.html')

    
    @app.route('/users')
    # @login_required  # Optional: Remove this decorator if you want the page to be accessible without authentication
    def users():
        all_users = User.query.all()  # Get all users from the database
        return render_template('users.html', users=all_users)
    
    @app.route('/clear-users', methods=['POST'])
    def clear_users():
        try:
            db.session.query(User).delete()  # This will delete all users from your User table
            db.session.commit()
            
        except Exception as e:
            db.session.rollback()
            flash(f'Error clearing users: {e}')
        flash('All users have been cleared.') 
        print('All users have been cleared.')
        return redirect(url_for('users'))


    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('home'))
        
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            user = User.query.filter_by(username=username).first()
            
            if user and check_password_hash(user.password, password):
                login_user(user)
                next_page = request.args.get('next') or url_for('home')
                return redirect(next_page)
            else:
                flash('Login Unsuccessful. Please check username and password', 'danger')
        
        return render_template('login.html')

    @app.route('/logout')
    def logout():
        logout_user()
        flash('You have been logged out', 'info')
        print('User logged out')
        return redirect(url_for('login'))

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if current_user.is_authenticated:
            return redirect(url_for('home'))
        
        if request.method == 'POST':
            username = request.form['username']
            email = request.form['email']  # Retrieve the email from the form data

            # Check if the username already exists
            existing_user = User.query.filter_by(username=username).first()

            if existing_user is not None:
                flash('An account with this username already exists.', 'warning')
                return render_template('register.html')  # Redirecting back to register.html

            # Proceed with new user registration if username is unique
            password = generate_password_hash(request.form['password'])
            user = User(username=username, email=email, password=password)
            db.session.add(user)
            db.session.commit()
            flash('Your account has been created! You are now able to log in', 'success')
            return redirect(url_for('login'))

        # GET request or no form submission yet
        return render_template('register.html')
    return app

