from flask import Flask, request, redirect, url_for, render_template
from werkzeug.datastructures import ImmutableMultiDict
from warsey import manager
from waitress import serve
import flask_login
import json, os
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["25000 per day", "2000 per hour"]
)
app.secret_key = os.environ['VENDOR_SECRET']
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

class User(flask_login.UserMixin):
    pass

@login_manager.user_loader
def user_loader(username):
    if manager.userexists(username) != True:
        return
    user = User()
    user.id = username
    return user

@login_manager.request_loader
def request_loader(request):
    username = request.form.get('user')
    if manager.userexists(username) != True:
        return
    user = User()
    user.id = user
    return user

@app.route('/', methods=['GET', 'POST'])
@limiter.limit("18 per hour")
def login():
    if flask_login.current_user.is_authenticated:
        return redirect(url_for('vendorcreate'))
    if request.method == 'GET':
        return render_template("login.html", error = 'hidden')
    username = request.form['username']
    if manager.userexists(username) and manager.userpass(username, request.form['password']):
        user = User()
        user.id = username
        flask_login.login_user(user)
        if manager.isadmin(flask_login.current_user.id):
            return redirect(url_for('admindash'))
        return redirect(url_for('vendorcreate'))
    return render_template("login.html", error = 'error')

@app.route('/getcode', methods=['POST'])
@limiter.limit("80 per hour")
@flask_login.login_required
def generatecode():
    data = request.form.to_dict(flat=False)
    jsondata = {
        "vendor": flask_login.current_user.id,
        "firstname": str(data["FirstName"])[2:-2],
        "lastname": str(data["LastName"])[2:-2],
        "email": str(data["Email"])[2:-2],
        "phonenumber": str(data["phonenumber"])[2:-2],
        "model": str(data["model"])[2:-2],
        "size": str(data["size"])[2:-2],
        "moreinfo": str(data["moreinfo"])[2:-2],
        "date": manager.timenow()
    }
    try:
        code = manager.generatecode(jsondata)
    except:
        return "Error"
    return code

@app.route('/create')
@flask_login.login_required
def vendorcreate():
    return render_template("vendorcreate.html", user = flask_login.current_user.id)

@app.route('/codeinfo/<code>')
@flask_login.login_required
def vendorcode(code):
    return render_template("vendorcode.html", code = code, user = flask_login.current_user.id)

@app.route("/logout")
@flask_login.login_required
def logout():
    flask_login.logout_user()
    return redirect(url_for("login"))

@app.route("/vendor")
def vendor():
    return redirect(url_for("login"))

# Admin

@app.route("/root")
@flask_login.login_required
def admindash():
    if not manager.isadmin(flask_login.current_user.id):
        return render_template("error.html", errorcode = 403, errormsg = "Not enough privileges.")
    return render_template("adminpanel.html", user = flask_login.current_user.id)

@app.route("/root/refreshdata", methods=['POST'])
@limiter.limit("180 per hour")
@flask_login.login_required
def adminrefreshdata():
    if not manager.isadmin(flask_login.current_user.id):
        return render_template("error.html", errorcode = 403, errormsg = "Not enough privileges.")
    try:
        manager.updateadmindata()
    except:
        return "Internal Server Error"
    return "Data refreshed succesfully."

@app.route('/root/newuser', methods=['POST'])
@limiter.limit("70 per hour")
@flask_login.login_required
def newuser():
    if not manager.isadmin(flask_login.current_user.id):
        return render_template("error.html", errorcode = 403, errormsg = "Not enough privileges.")
    username = request.form['username']
    if len(username) > 16:
        return render_template("error.html", errorcode = "NON-HTTP", errormsg = "Username too long.")
    if manager.userexists(username):
        return render_template("error.html", errorcode = "NON-HTTP", errormsg = "User Exists. | Username already in use.")
    try:
        password = manager.createuser(username)
    except:
        return render_template("error.html", errorcode = "500", errormsg = "Error while creating user.")
    msg = f"Username: {username}"
    msg2 = f"Password: {password}"
    return render_template("adminnotif.html", notif = msg, notif2 = msg2, user = flask_login.current_user.id)

@app.route('/root/deluser', methods=['POST'])
@limiter.limit("70 per hour")
@flask_login.login_required
def deluser():
    if not manager.isadmin(flask_login.current_user.id):
        return render_template("error.html", errorcode = 403, errormsg = "Not enough privileges.")
    username = request.form['username']
    if len(username) > 16:
        return render_template("error.html", errorcode = "NON-HTTP", errormsg = "Username too long.")
    if not manager.userexists(username):
        return render_template("error.html", errorcode = "NON-HTTP", errormsg = "User Does Not Exists.")
    try:
        password = manager.deleteuser(username)
    except:
        return render_template("error.html", errorcode = "500", errormsg = "Error while deleting user.")
    msg = f"{username} deleted succesfully."
    return render_template("adminnotif.html", notif = msg, user = flask_login.current_user.id)

# End of Admin

@login_manager.unauthorized_handler
def unauthorized_handler():
    return redirect(url_for('login'))

@app.errorhandler(429)
def not_found(e):
    return render_template("error.html", errorcode = "429 | Too Many Requests", errormsg = "You have made too many requests in the past hour, please try again later.")

@app.errorhandler(404)
def not_found(e):
  return render_template("error.html", errorcode = 404, errormsg = "The page you are looking for doesn't exists.")

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=6001)