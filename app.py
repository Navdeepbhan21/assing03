from flask import Flask
import socket

app = Flask(_name_)
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

@app.route('/')
def hello_cloud():
  return ' Welcome to Navdeep bhan ECS cluster '
  


app.run(host='0.0.0.0', port=5000 )
