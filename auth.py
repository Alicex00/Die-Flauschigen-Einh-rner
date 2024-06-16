from flask import Blueprint,render_template, request, redirect, url_for, flash
auth=Blueprint ('auth',__name__)



@auth.route('/login', methods = ['GET','POST'])
def login():
 data=request.form
 print(data)
 return render_template ("login.html", text="Testing")  
@auth.route('/home')
def home():
 return render_template ("home.html")

@auth.route ('/logout')
def logout():
 return redirect(url_for("auth.home"))

@auth.route('/sign-up', methods = ['GET','POST'])
def sign_up():
    return render_template("sign_up.html")

@auth.route ('/merkliste')
def merkliste():
 return render_template ("merkliste.html")

@auth.route('/kategorien')
def kategorien():
 return render_template ("kategorien.html")

@auth.route ('/account')
def account():
 return  render_template ("account.html")


@auth.route ('/rezept')
def rezept(rezeptname):
 return render_template("rezept.html")

@auth.route ('/rezeptUpload', methods=['GET','POST'])
def rezeptUpload():
 return render_template("rezeptUpload.html")