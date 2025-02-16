from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This App is deployed on AWS ECS'

@app.route('/health')
def health():
    return 'Server is up and running'
