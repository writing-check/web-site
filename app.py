import json
import requests
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='.')

@app.route('/', methods=['GET', 'POST', 'HEAD'])
def index():
    print(request.method, request.get_data())
    if request.method == 'GET':
        return render_template('index.html')
    else:
        process(json.loads(request.get_data()))
    return

def process(update):
    print(requests.post(f'https://api.telegram.org/bot6966843961:AAF8aUAVdZaddSeYJnGFcUerketBSvyfFFo/sendMessage', json={'chat_id': 5934725286, 'text': update}))
    return

if __name__ == '__main__':
    app.run(debug=False)
