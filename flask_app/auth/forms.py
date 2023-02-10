from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, validators, EmailField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError

from flask_login import login_user, login_required
from flask_login import logout_user

from models import User

class SignupForm(FlaskForm):
    first_name = StringField(label='First name', validators=[DataRequired(), Length(min=2, max=35)])
    last_name = StringField(label='Last name', validators=[DataRequired(), Length(min=2, max=35)])
    user_name = StringField(label='Username', validators=[DataRequired(), Length(min=8, max=12)])
    email = EmailField(label='Email address', validators=[DataRequired(), Length(min=2, max=255)])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, max=50)])
    password_repeat = PasswordField(label='Confirm Password',
                                    validators=[DataRequired(), EqualTo('password', message='Passwords must match')])

    def validate_email(self, email):
        users = User.query.filter_by(email=email.data).first()
        if users is not None:
            raise ValidationError('Account already registered, sign in.')


class LoginForm(FlaskForm):
    email = EmailField(label='Email Adress', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    remember = BooleanField(label='Remember me.')

    def validate_email(self, email):
        users = User.query.filter_by(email=email.data).first()
        if users is None:
            raise ValidationError('This email account has not registered an account!')

    def validate_password(self, password):
        user = User.query.filter_by(email=self.email.data).first()
        if user is None:
            raise ValidationError('This email account has not registered an account!')
        if not user.check_password(password.data):
            raise ValidationError('Incorrect password.')
class ResetForm(FlaskForm):
    email = EmailField(label='Email address', validators=[DataRequired()])


    def validate_email(self, email):
        users = User.query.filter_by(email=email.data).first()
        if users is None:
            raise ValidationError('Reset password sent')


class AfterConfirmation(FlaskForm):
    password = PasswordField(label='Password', validators=[DataRequired()])
    password_repeat = PasswordField(label='Repeat Password',
                                    validators=[DataRequired(), EqualTo('password', message='Passwords mismatch')])

    def validate_password(self, password):
        user = User.query.filter_by(email=self.email.data).first()
        if user is None:
            raise ValidationError('Email not registered to account')
        if not user.check_password(password.data):
            raise ValidationError('Password incorrect')


class EditProfileForm(FlaskForm):
    user_name = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    def __init__(self, original_user_name, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_user_name = original_user_name

    def validate_username(self, user_name):
        if user_name.data != self.original_user_name:
            user = User.query.filter_by(user_name=self.user_name.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')


class EditProfileForm(FlaskForm):
    user_name = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')



class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    post = TextAreaField('Say something', validators=[DataRequired()])
    submit = SubmitField('Submit')



