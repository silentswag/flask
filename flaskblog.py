from flask import Flask,redirect,url_for,render_template,request,session,flash
from datetime import timedelta
app=Flask(__name__) #variable, module
app.secret_key="practice"
app.permanent_session_lifetime=timedelta(minutes=1)


@app.route("/") # goto diff pages- route decorators "/" represents root page
def home():
    return render_template("index.html")

@app.route("/inherit") 
def test_inherit():
    return render_template("textinherit.html")

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":
        session.permanent=True
        user=request.form['nm']
        session['user']=user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user=session['user']
        return f"<h1><b>{user}</b</h1>"
    else:
        return redirect(url_for("login"))

@app.route("/logout") #remove data after useer session
def logout():
    session.pop("user",None)
    flash("you logged out","info")
    return redirect(url_for("login"))

if __name__=="__main__":
    app.run(debug=True)