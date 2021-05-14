from projekt.models import User
from projekt.forms import LoginForm,RegisterForm
from flask import render_template, url_for,flash, redirect
from projekt import app, db, bcrypt
from flask_login import login_user

@app.route('/home')
def witam():
	return "<p>Udao ci sie zalogowac</p>"

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user= User.query.filter_by(username=form.username.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user)
			return redirect(url_for('witam'))
		else:
			flash(f'Nie udane logowanie sprawdz dane')
	return render_template('login.html',title='Login',form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
			secured_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
			user = User(username=form.username.data, email=form.email.data, password=secured_password)
			db.session.add(user)
			db.session.commit()
			flash('udalo sie')
			return redirect(url_for('login'))
	return render_template('register.html',title='Login',form=form)

@app.route('/')
def hello_world():
	return render_template('sukces.html')