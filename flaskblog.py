from flask import Flask,redirect,url_for

app=Flask(__name__) #variable, module


@app.route("/") # goto diff pages- route decorators "/" represents root page
def home():
    return "Hello world <h1> FLASK</h>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    return redirect(url_for("user",name="Anushree"))

if __name__=="__main__":
    app.run()