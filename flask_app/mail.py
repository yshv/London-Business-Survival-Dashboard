from flask import render_template
from flask_mail import Message

import mail


def send_email(user):
    token = user.get_reset_token(user.id)

    msg = Message('Hello', sender='COMP0034.reset@gmail.com', recipients=[user.email])
    msg.subject = "Reset email"
    msg.html = render_template('confirmed.html', user=user, token=token)

    mail.send(msg)
