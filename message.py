from flask import(
Blueprint,flash,g,redirect,render_template,request,url_for
)
from werkzeug.exceptions import abort

from webchat.auth import login_required


bp = Blueprint('message',__name__,url_prefix='/message')

@bp.route('/session')
def session():
    return render_template('message/session.html')
