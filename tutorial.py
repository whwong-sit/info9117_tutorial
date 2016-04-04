from flask import Flask,request

app = Flask(__name__)
host="localhost"
port="5000"
address="http://{host}:{port}".format(host=host,port=port)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login')
def login_page():
    pass

def serve_forever():
    app.run(host, port)

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()

if __name__ == '__main__':
    serve_forever()
