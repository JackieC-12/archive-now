from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Comment, Archive, User

comment_routes = Blueprint('comments', __name__)

'''
GET all comments on an archive
'''
@comment_routes.route('/')
def get_comments(archive_id):

    res = []
    comments = Comment.query.filter(Comment.archiveId == archive_id).all()

    for comment in comments:
        user = User.query.get(comment.userId)

        res.append({
            'userId': comment.userId,
            'user': user.username,
            'message': comment.message,
            'created_at': comment.created_at
        })

    return res
