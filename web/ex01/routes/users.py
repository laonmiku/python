from flask import Blueprint, render_template,request
from dao import users
import json

bp = Blueprint('users', __name__,url_prefix='/users')

@bp.route('/login')
def login():
    return render_template('index.html', title="로그인", pageName="users/login.html")

@bp.route('/login', methods=['POST'])
def loginPost():
    req = json.loads(request.get_data())
    #print (req)
    uid=req['uid']
    upass=req.get('upass')
    row= users.read(uid)
    print(row)
    result=0
    if row:
        if row.get("upass")==upass:
            result=1
        else :
            result=2
    return str(result)
