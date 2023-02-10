from datetime import timedelta
from urllib.parse import urlparse, urljoin

from urllib.parse import urlparse, urljoin
from flask import Blueprint, render_template, flash, redirect, url_for, request, abort, request
from flask_login import login_user, login_required
from flask_login import logout_user
from sqlalchemy.exc import IntegrityError


from flask_login import login_manager
from __init__ import db
from auth.forms import SignupForm, LoginForm, EditProfileForm,  ResetForm
from models import User
from mail import send_email

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/auth')
def auth():
   return "This is the authentication section of the web app"


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)
    if form.validate_on_submit():
        user = User(first_name=form.first_name.data, last_name=form.last_name.data, user_name=form.user_name.data, email=form.email.data)
        user.set_password(form.password.data)
        try:
            db.session.add(user)
            db.session.commit()
            flash(f"Hello, {user.first_name} {user.last_name}. Signed up!.")
        except IntegrityError:
            db.session.rollback()
            flash(f'Error, {form.email.data} is unable to register.', 'Check email details.')
            return redirect(url_for('auth.signup'))
        return redirect(url_for('index'))
    return render_template('signup.html', title='Sign Up', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        login_user(user, remember=login_form.remember.data, duration=timedelta(minutes=1))
        next = request.args.get('next')
        return redirect(next or url_for('index'))
    return render_template('login.html', title='Login', form=login_form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@auth_bp.route('/password_reset', methods=['GET', 'POST'])
def password_reset():
    form = ResetForm()

    if request.method == 'GET':
        return render_template('password_reset.html', title='Reset', form=form)

    if request.method == 'POST':

        email = request.form.get('email')
        user = User.verify_email(email)

        if user:
            send_email(user)
            flash('Email sent.')

        return redirect(url_for('auth.login'))


@auth_bp.route('/resetverified/<token>', methods=['GET', 'POST'])
def reset_verified(token):
    form = AfterConfirmation()
    user = User()
    userr = User.verify_reset_token(token)

    if not userr:
        flash('Not found')
        return redirect(url_for('auth.signup'))

    password = request.form.get('Password')
    if password:
        if form.password.data == form.password_repeat.data:
            user.set_password(form.password.data)
        else:
            return redirect(url_for('auth.login'))

    return render_template('layout.html')




def is_safe_url(target):
    host_url = urlparse(request.host_url)
    redirect_url = urlparse(urljoin(request.host_url, target))
    return redirect_url.scheme in ('http', 'https') and host_url.netloc == redirect_url.netloc


def get_safe_redirect():
    url = request.args.get('next')
    if url and is_safe_url(url):
        return url
    url = request.referrer
    if url and is_safe_url(url):
        return url
    return '/'