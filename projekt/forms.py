from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from projekt.models import User

class LoginForm(FlaskForm):
	username = StringField('username',
						 	validators=[DataRequired(),Length(min=2,max=20)])
	password = PasswordField('password',
								validators=[DataRequired()])
	submit = SubmitField('Login')



class RegisterForm(FlaskForm):
	username = StringField('username',
						validators=[DataRequired(),Length(min=2,max=20)])
	password = PasswordField('password',
						validators=[DataRequired(),Length(min=5,max=40)])
	confirm_password = PasswordField('confirm_password',
						validators=[DataRequired(),EqualTo('password')])
	email = EmailField('email',
						validators=[DataRequired()])
	submit = SubmitField('register')

	def validate_username(self,username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('Nazwa zajeta')

	def validate_email(self,email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Email zajety')