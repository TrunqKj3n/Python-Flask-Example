from flask import request
from flask import Flask
import requests
import json

app = Flask(__name__)


@app.route('/')
def index():
    return "<p>Simple Flask app</p>"

@app.route('/short')
def short():
    url = request.args.get('url')
    if url == None:
        return "No url"
    elif url == "":
        return "No url"
    else:
        res = requests.get(f"https://thieutrungkien.dev/shorturl?url={url}")
        return json.loads(res.text) 
        
if __name__ == '__main__':
    app.run(debug=True)
