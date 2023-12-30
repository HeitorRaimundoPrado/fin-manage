from flask import Blueprint, current_app, request
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, jwt_required, decode_token
from flask_mail import Message
from werkzeug.security import generate_password_hash, check_password_hash
from api.extensions import db
from api.extensions import mail
    

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=["POST"])
def register():
    req = request.get_json()
    email = req.get('email')
    username = req.get('username', None)
    password = req.get('password',  None)

    from api import User
    
    user = User.query.filter_by(username=username).first()

    if user:
        return {'msg': 'username already taken'}, 401

    try:
        user = User(username=username, email=email, password=generate_password_hash(password))
        db.session.add(user)
        db.session.commit()

    except IntegrityError:
        return {'msg': 'email already used'}, 401

    if not user:
        return {'msg': 'error creating user'}, 500
    
    token = create_access_token(identity=user.email)
    
    frontend_url = current_app.config['FRONTEND_DOMAIN'] + '/confirm_email?token=' + token
    
    msg = Message('Confirm Your Account', recipients=[user.email])
    msg.body = 'Click the link to confirm your account: {}'.format(frontend_url)
    mail.send(msg)
    return {"msg": "success", 'token': token}, 200

@auth_bp.route('/confirm_email/<token>', methods=['POST'])
def confirm_email(token):
    try:
        email = decode_token(token)['sub']
        print(email)

        from api import User

        user = User.query.filter_by(email=email).first()
        if user is None:
            return {'msg': 'invalid token'}, 400
        
        user.is_confirmed = True
        
        from api.extensions import db
        db.session.commit()
        
    except Exception as e:
        print(e)
        return {'msg': 'the confirmation link is invalid or has expired'}, 400
    else:
        return {'msg': 'confirmed email', 'redirect_url': '/'}, 200


@auth_bp.route('/login', methods=["POST"])
def login():
    req = request.get_json()
    username = req.get("username", None)
    password = req.get("password", None)

    from api import User

    user = User.query.filter_by(username=username).first()

    if user is None or user.is_confirmed is False or check_password_hash(password, user.password) is False:
        return {'msg': 'no user found'}, 401

    token = create_access_token(identity=user.id)

    
    return {'msg': 'successful login', 'token': token}, 200

