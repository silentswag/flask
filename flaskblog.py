from flask import Flask
app=Flask(__name__) #variable, module


@app.route("/") # goto diff pages- route decorators "/" represents root page
def hello():
    return "Hello"