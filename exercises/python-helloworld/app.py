from flask import Flask, json
import logging

app = Flask(__name__)
logging.basicConfig(filename="app.log", level=logging.DEBUG)

@app.route("/")
def hello():
    logging.info("/ endpoint was reached")
    return "Hello World!"

@app.route("/status")
def status():
    res = app.response_class(
        response = json.dumps({"result": "OK - healthy"}),
        status = 200,
        mimetype = "application/json"
    )
    logging.info("Status endpoint was reached")
    return res

@app.route("/metrics")
def metrics():
    res = app.response_class(
        response = json.dumps({"data": {"UserCount": 140, "UserCountActive": 23}}),
        status = 200,
        mimetype = "application/json"
    )
    logging.info("Metrics endpoint was reached")
    return res

if __name__ == "__main__":
    app.run(host='0.0.0.0')
