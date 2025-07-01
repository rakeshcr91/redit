from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user

from . import main_bp
from .forms import PostForm
from ..models import db, Post, Vote


@main_bp.route('/', methods=['GET', 'POST'])
def feed():
    form = PostForm()
    if form.validate_on_submit():
        if not current_user.is_authenticated:
            flash('Please login to post.', 'warning')
            return redirect(url_for('auth.login'))
        post = Post(body=form.body.data, url=form.url.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Post created!', 'success')
        return redirect(url_for('main.feed'))

    posts = Post.query.all()
    posts.sort(key=lambda p: p.score, reverse=True)
    return render_template('main/feed.html', form=form, posts=posts)


@main_bp.route('/vote/<int:post_id>/<action>')
@login_required
def vote(post_id, action):
    post = Post.query.get_or_404(post_id)
    value = 1 if action == 'up' else -1
    vote = Vote.query.filter_by(user=current_user, post=post).first()
    if vote:
        if vote.value == value:
            db.session.delete(vote)
        else:
            vote.value = value
    else:
        vote = Vote(value=value, user=current_user, post=post)
        db.session.add(vote)
    db.session.commit()
    return redirect(url_for('main.feed'))
