from flask import Flask, request
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/webhook", methods=['POST'])
def webhook():
    payload=request.get_json(force=True)

    logging.info('Useful message')
    logging.info('Useful message')
    return "called webhook with params: {}".format(payload)

if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=true)