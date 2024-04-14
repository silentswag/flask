from flask import Flask,redirect,url_for,render_template

app=Flask(__name__) #variable, module


@app.route("/<name>") # goto diff pages- route decorators "/" represents root page
def home(name):
    return render_template("index.html",content=name)


if __name__=="__main__":
    app.run()