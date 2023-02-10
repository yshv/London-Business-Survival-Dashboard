import config
from __init__ import create_app, db
from flask import Flask, render_template, flash, request, redirect, url_for
from flask_login import current_user, login_required

from models import User, Post

from auth.forms import LoginForm, EditProfileForm, EmptyForm, PostForm

app = create_app(config.DevelopmentConfig)

@app.login_manager.user_loader
def load_user(user_id):
    """ Takes a user ID and returns a user object or None if the user does not exist"""
    if user_id is not None:
        return User.query.get(user_id)
    return None

@app.route("/")
def index():
    if not current_user.is_anonymous:
        name = current_user.first_name
        flash(f'Welcome {name}! ')
    return render_template('index.html', title="Home")

@app.route('/user/<user_name>')
@login_required
def user(user_name):
    user = User.query.filter_by(user_name=user_name).first_or_404()
    page = request.args.get('page', 1, type=int)
    posts = user.posts.order_by(Post.timestamp.desc()).paginate(
        page, app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('user', user_name=user.user_name, page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('user', user_name=user.user_name, page=posts.prev_num) \
        if posts.has_prev else None
    form = EmptyForm()
    return render_template('user.html', user=user, posts=posts.items,
                           next_url=next_url, prev_url=prev_url, form=form)

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.user_name = form.user_name.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.user_name.data = current_user.user_name
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form)


if __name__ == "__main__":
    app.run(debug = True)







