from flask import Flask, render_template
import configparser

# read flask server properties file
config = configparser.ConfigParser()
config.read('server.properties')
        
# init flask
app = Flask(__name__)

# index route
@app.route('/')
def index():
    return render_template('index.html')

# signin page route
@app.route('/signin')
def signin():
    return render_template('signin.html')

# read server port from flask properties file
serverPort = config.get('server.general', 'serverPort')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=serverPort)