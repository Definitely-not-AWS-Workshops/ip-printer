from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def unique_info():
    # Get the hostname and IP address of the container
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    # Create a response string containing the unique information
    response = f"Hostname: {hostname}\nIP Address: {ip_address}\n"

    return response


@app.route('/health')
def health_check_msg():
    return "I'm OK!"    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
