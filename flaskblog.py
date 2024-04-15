from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__) #variable, module


@app.route("/") # goto diff pages- route decorators "/" represents root page
def home():
    return render_template("index.html")

@app.route("/inherit") 
def test_inherit():
    return render_template("textinherit.html")

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":
        user=request.form['nm']
        return redirect(url_for("user",usr=user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1><b>{usr}</b</h1>"


if __name__=="__main__":
    app.run(debug=True)